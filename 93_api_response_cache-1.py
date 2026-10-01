"""93 - API Response Cache with TTL"""
from dataclasses import dataclass
from time import monotonic
from typing import Any, Callable

@dataclass
class CacheEntry:
    value: Any
    expires_at: float

class TTLCache:
    def __init__(self, ttl_seconds=60):
        if ttl_seconds <= 0:
            raise ValueError("TTL must be greater than zero")
        self.ttl_seconds = ttl_seconds
        self._cache = {}

    def set(self, key, value):
        self._cache[key] = CacheEntry(
            value, monotonic() + self.ttl_seconds
        )

    def get(self, key):
        entry = self._cache.get(key)
        if entry is None:
            return None
        if monotonic() >= entry.expires_at:
            del self._cache[key]
            return None
        return entry.value

    def get_or_set(self, key, factory: Callable[[], Any]):
        cached = self.get(key)
        if cached is not None:
            return cached
        value = factory()
        self.set(key, value)
        return value

    def clear(self):
        self._cache.clear()

    def size(self):
        return len(self._cache)

def fake_api_call():
    print("Calling API...")
    return {"status": "success", "source": "API"}

def main():
    cache = TTLCache(ttl_seconds=10)
    print("First:", cache.get_or_set("user:1", fake_api_call))
    print("Second:", cache.get_or_set("user:1", fake_api_call))
    print("Cache entries:", cache.size())

if __name__ == "__main__":
    main()
