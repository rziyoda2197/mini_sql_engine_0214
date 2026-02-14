import json
import os
from typing import List, Dict

FILE = "storage.json"


class Storage:
    def __init__(self):
        self.data: List[Dict] = self._load()

    def _load(self):
        if not os.path.exists(FILE):
            return []
        with open(FILE, "r") as f:
            return json.load(f)

    def _save(self):
        with open(FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def all(self):
        return self.data

    def insert(self, row: dict):
        row["id"] = (self.data[-1]["id"] + 1) if self.data else 1
        self.data.append(row)
        self._save()
        return row

    def delete(self, row_id: int):
        for r in self.data:
            if r["id"] == row_id:
                self.data.remove(r)
                self._save()
                return True
        return False

    def filter(self, key: str, value: str):
        return [r for r in self.data if str(r.get(key)) == value]
