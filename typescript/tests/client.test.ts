import { afterEach, describe, expect, it, vi } from "vitest"

import { DEFAULT_BASE_URL, Touchmark, TouchmarkError } from "../src/index.js"

type Call = { url: URL; init: RequestInit }

function json(
  status: number,
  body: unknown,
  headers: Record<string, string> = {},
) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", ...headers },
  })
}

function fakeFetch(...answers: (Response | Error)[]) {
  const calls: Call[] = []
  const fetch = async (url: URL | RequestInfo, init?: RequestInit) => {
    calls.push({ url: new URL(String(url)), init: init ?? {} })
    const answer = answers.shift()
    if (answer === undefined) throw new Error("no answer left")
    if (answer instanceof Error) throw answer
    return answer
  }
  return { calls, fetch: fetch as typeof globalThis.fetch }
}

function problem(
  status: number,
  code: string,
  headers: Record<string, string> = {},
) {
  return json(
    status,
    {
      type: "about:blank",
      title: code,
      status,
      detail: `${code} detail`,
      code,
    },
    { "x-request-id": "req_123", ...headers },
  )
}

afterEach(() => {
  vi.unstubAllEnvs()
  vi.useRealTimers()
})

describe("configuration", () => {
  it("reads the key from TOUCHMARK_API_KEY", async () => {
    vi.stubEnv("TOUCHMARK_API_KEY", "vld_live_env")
    const { calls, fetch } = fakeFetch(
      json(200, { credit_balance: 5, tier: 0 }),
    )
    await new Touchmark({ fetch }).account.get()
    expect(calls[0]?.init.headers).toMatchObject({
      Authorization: "Bearer vld_live_env",
    })
    expect(calls[0]?.url.toString()).toBe(`${DEFAULT_BASE_URL}/v1/account`)
  })

  it("refuses to start without a key", () => {
    vi.stubEnv("TOUCHMARK_API_KEY", "")
    expect(() => new Touchmark()).toThrow(/TOUCHMARK_API_KEY/)
  })

  it("takes another base URL", async () => {
    const { calls, fetch } = fakeFetch(json(200, {}))
    await new Touchmark({
      apiKey: "k",
      baseUrl: "http://localhost:8000/",
      fetch,
    }).account.get()
    expect(calls[0]?.url.toString()).toBe("http://localhost:8000/v1/account")
  })
})

describe("methods", () => {
  const cases: [
    string,
    (tm: Touchmark) => Promise<unknown>,
    string,
    string,
    unknown,
  ][] = [
    [
      "email.validate",
      (tm) => tm.email.validate({ email: "a@b.co" }),
      "POST",
      "/v1/email/validate",
      { email: "a@b.co" },
    ],
    [
      "email.validateBatch",
      (tm) => tm.email.validateBatch({ emails: ["a@b.co"] }),
      "POST",
      "/v1/email/validate/batch",
      { emails: ["a@b.co"] },
    ],
    [
      "email.verify",
      (tm) => tm.email.verify({ email: "a@b.co" }),
      "POST",
      "/v1/email/verify",
      { email: "a@b.co" },
    ],
    [
      "domain.senderReadiness",
      (tm) => tm.domain.senderReadiness({ domain: "b.co" }),
      "POST",
      "/v1/domain/sender-readiness",
      { domain: "b.co" },
    ],
    [
      "ip.lookup",
      (tm) => tm.ip.lookup({ ip: "203.0.113.7" }),
      "POST",
      "/v1/ip/lookup",
      { ip: "203.0.113.7" },
    ],
    [
      "ip.lookupBatch",
      (tm) => tm.ip.lookupBatch({ ips: ["203.0.113.7"] }),
      "POST",
      "/v1/ip/lookup/batch",
      { ips: ["203.0.113.7"] },
    ],
    [
      "phone.validate",
      (tm) => tm.phone.validate({ phone: "+44 20 7946 0000" }),
      "POST",
      "/v1/phone/validate",
      { phone: "+44 20 7946 0000" },
    ],
    [
      "phone.validateBatch",
      (tm) =>
        tm.phone.validateBatch({ phones: ["+44 20 7946 0000"], country: "GB" }),
      "POST",
      "/v1/phone/validate/batch",
      { phones: ["+44 20 7946 0000"], country: "GB" },
    ],
  ]

  it.each(cases)(
    "%s sends its request",
    async (_, call, method, path, body) => {
      const { calls, fetch } = fakeFetch(json(200, { ok: true }))
      const answer = await call(new Touchmark({ apiKey: "k", fetch }))
      expect(answer).toEqual({ ok: true })
      expect(calls[0]?.init.method).toBe(method)
      expect(calls[0]?.url.pathname).toBe(path)
      expect(JSON.parse(String(calls[0]?.init.body))).toEqual(body)
      expect(calls[0]?.init.headers).toMatchObject({
        "Content-Type": "application/json",
      })
    },
  )

  it("email.getVerification passes the id and wait", async () => {
    const { calls, fetch } = fakeFetch(json(200, { status: "done" }))
    await new Touchmark({ apiKey: "k", fetch }).email.getVerification("a/b", {
      wait: 5,
    })
    expect(calls[0]?.url.pathname).toBe("/v1/email/verify/a%2Fb")
    expect(calls[0]?.url.searchParams.get("wait")).toBe("5")
    expect(calls[0]?.init.body).toBeUndefined()
  })
})

describe("errors and retries", () => {
  it("turns a problem document into TouchmarkError", async () => {
    const { fetch } = fakeFetch(problem(402, "insufficient_credits"))
    const error = await new Touchmark({ apiKey: "k", fetch }).email
      .validate({ email: "a@b.co" })
      .catch((e: unknown) => e)
    expect(error).toBeInstanceOf(TouchmarkError)
    expect(error).toMatchObject({
      status: 402,
      code: "insufficient_credits",
      detail: "insufficient_credits detail",
      requestId: "req_123",
      retryAfter: null,
    })
  })

  it("names an answer that is not a problem document by its status", async () => {
    const { fetch } = fakeFetch(
      new Response("<html>bad gateway</html>", { status: 502 }),
    )
    await expect(
      new Touchmark({ apiKey: "k", fetch }).account.get(),
    ).rejects.toMatchObject({ status: 502, code: "http_502", detail: null })
  })

  it("retries a 429 after Retry-After, at most twice", async () => {
    const { calls, fetch } = fakeFetch(
      problem(429, "rate_limited", { "retry-after": "0" }),
      problem(429, "rate_limited", { "retry-after": "0" }),
      json(200, { ok: true }),
    )
    await expect(
      new Touchmark({ apiKey: "k", fetch }).account.get(),
    ).resolves.toEqual({ ok: true })
    expect(calls).toHaveLength(3)
  })

  it("gives up after two retries", async () => {
    const { calls, fetch } = fakeFetch(
      problem(429, "rate_limited", { "retry-after": "0" }),
      problem(429, "rate_limited", { "retry-after": "0" }),
      problem(429, "rate_limited", { "retry-after": "0" }),
    )
    await expect(
      new Touchmark({ apiKey: "k", fetch }).account.get(),
    ).rejects.toMatchObject({
      code: "rate_limited",
      retryAfter: 0,
    })
    expect(calls).toHaveLength(3)
  })

  it("waits before retrying a 503 without Retry-After", async () => {
    vi.useFakeTimers()
    const { calls, fetch } = fakeFetch(
      problem(503, "upstream_unavailable"),
      json(200, { ok: true }),
    )
    const pending = new Touchmark({ apiKey: "k", fetch }).email.validate({
      email: "a@b.co",
    })
    await vi.advanceTimersByTimeAsync(1000)
    await expect(pending).resolves.toEqual({ ok: true })
    expect(calls).toHaveLength(2)
  })

  it.each([
    ["a 500", problem(500, "internal_error")],
    ["a 402", problem(402, "insufficient_credits")],
    ["any other 503", problem(503, "maintenance")],
  ])("does not retry %s", async (_, answer) => {
    const { calls, fetch } = fakeFetch(answer, json(200, {}))
    await expect(
      new Touchmark({ apiKey: "k", fetch }).email.validate({ email: "a@b.co" }),
    ).rejects.toBeInstanceOf(TouchmarkError)
    expect(calls).toHaveLength(1)
  })

  it("does not retry a network error", async () => {
    const { calls, fetch } = fakeFetch(
      new TypeError("network down"),
      json(200, {}),
    )
    await expect(
      new Touchmark({ apiKey: "k", fetch }).email.validate({ email: "a@b.co" }),
    ).rejects.toThrow("network down")
    expect(calls).toHaveLength(1)
  })

  it("does not follow a redirect", async () => {
    const { calls, fetch } = fakeFetch(
      new Response(null, {
        status: 307,
        headers: { location: "https://elsewhere.example" },
      }),
    )
    const error = await new Touchmark({ apiKey: "k", fetch }).account
      .get()
      .catch((e) => e)
    expect(error).toBeInstanceOf(TouchmarkError)
    expect(error.status).toBe(307)
    expect(error.code).toBe("http_307")
    expect(calls).toHaveLength(1)
    expect(calls[0]?.init.redirect).toBe("manual")
  })

  it("maxRetries: 0 turns retries off", async () => {
    const { calls, fetch } = fakeFetch(
      problem(429, "rate_limited", { "retry-after": "0" }),
    )
    await expect(
      new Touchmark({ apiKey: "k", fetch, maxRetries: 0 }).account.get(),
    ).rejects.toBeInstanceOf(TouchmarkError)
    expect(calls).toHaveLength(1)
  })
})

describe("waitForVerification", () => {
  it("polls until the check is done", async () => {
    const { calls, fetch } = fakeFetch(
      json(200, { id: "v1", status: "queued" }),
      json(200, { id: "v1", status: "running" }),
      json(200, { id: "v1", status: "done", result: "valid" }),
    )
    const answer = await new Touchmark({
      apiKey: "k",
      fetch,
    }).email.waitForVerification("v1")
    expect(answer).toMatchObject({ status: "done", result: "valid" })
    expect(calls).toHaveLength(3)
    for (const call of calls) {
      const wait = Number(call.url.searchParams.get("wait"))
      expect(wait).toBeGreaterThanOrEqual(0)
      expect(wait).toBeLessThanOrEqual(10)
    }
  })

  it("returns the last answer when the time is up", async () => {
    const { calls, fetch } = fakeFetch(
      json(200, { id: "v1", status: "queued" }),
    )
    const answer = await new Touchmark({
      apiKey: "k",
      fetch,
    }).email.waitForVerification("v1", {
      timeoutSeconds: 0,
    })
    expect(answer).toMatchObject({ status: "queued" })
    expect(calls).toHaveLength(1)
  })
})
