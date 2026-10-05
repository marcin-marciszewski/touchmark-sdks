import json
from pathlib import Path
from typing import Any

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


def fixture(name: str) -> dict[str, Any]:
    """A real API answer, captured from the API (request ids replaced)."""
    data: dict[str, Any] = json.loads((FIXTURES / f"{name}.json").read_text())
    return data


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(autouse=True)
def no_key_in_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("TOUCHMARK_API_KEY", raising=False)


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Records retry waits instead of sleeping (both clients)."""
    waited: list[float] = []

    async def fake_async_sleep(seconds: float) -> None:
        waited.append(seconds)

    monkeypatch.setattr("touchmark._client.time.sleep", waited.append)
    monkeypatch.setattr("touchmark._client.anyio.sleep", fake_async_sleep)
    return waited
