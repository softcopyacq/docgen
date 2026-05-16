"""
Sample project file to demonstrate DocGen.
Run: python main.py ./sample_project
"""

from typing import List, Optional
import math


class DataProcessor:
    """Handles raw data ingestion and transformation."""

    def __init__(self, name: str, max_records: int = 1000):
        self.name = name
        self.max_records = max_records
        self._data: List[dict] = []

    def load(self, records: List[dict]) -> bool:
        if len(records) > self.max_records:
            raise ValueError(f"Exceeds max_records limit of {self.max_records}")
        self._data = records
        return True

    def filter(self, key: str, value) -> List[dict]:
        return [r for r in self._data if r.get(key) == value]

    def summarise(self) -> dict:
        return {"name": self.name, "count": len(self._data)}


def normalise(values: List[float], scale: float = 1.0) -> List[float]:
    if not values:
        return []
    min_v, max_v = min(values), max(values)
    if min_v == max_v:
        return [0.0] * len(values)
    return [(v - min_v) / (max_v - min_v) * scale for v in values]


async def fetch_remote(url: str, timeout: int = 30) -> Optional[dict]:
    """Fetches JSON data from a remote URL asynchronously."""
    import asyncio
    await asyncio.sleep(0)  # placeholder
    return {"url": url, "timeout": timeout}


def compute_stats(data: List[float]) -> dict:
    if not data:
        return {}
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return {
        "count": n,
        "mean": round(mean, 4),
        "std": round(math.sqrt(variance), 4),
        "min": min(data),
        "max": max(data),
    }
