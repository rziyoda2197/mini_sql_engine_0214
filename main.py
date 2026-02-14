from app.service import DBService
from app.parser import parse_insert, parse_delete, parse_find

service = DBService()

print("MiniSQL DB started")
print("Commands:")
print("INSERT name=Ali age=20")
print("SELECT *")
print("DELETE 1")
print("FIND name=Ali")
print("EXIT")

while True:
    cmd = input("\nSQL> ").strip()

    if cmd.startswith("INSERT"):
        data = parse_insert(cmd)
        service.insert(data)

    elif cmd == "SELECT *":
        service.select_all()

    elif cmd.startswith("DELETE"):
        row_id = parse_delete(cmd)
        service.delete(row_id)

    elif cmd.startswith("FIND"):
        k, v = parse_find(cmd)
        service.find(k, v)

    elif cmd == "EXIT":
        break

    else:
        print("Unknown command")
