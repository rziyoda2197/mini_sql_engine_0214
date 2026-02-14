from app.db import Storage


class DBService:
    def __init__(self):
        self.storage = Storage()

    def insert(self, data: dict):
        row = self.storage.insert(data)
        print("✔ inserted:", row)

    def select_all(self):
        rows = self.storage.all()
        if not rows:
            print("Empty table")
            return
        for r in rows:
            print(r)

    def delete(self, row_id: int):
        if self.storage.delete(row_id):
            print("🗑 deleted")
        else:
            print("Not found")

    def find(self, key: str, value: str):
        rows = self.storage.filter(key, value)
        for r in rows:
            print(r)
        if not rows:
            print("No results")
