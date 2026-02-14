def parse_insert(cmd: str):
    # INSERT name=Ali age=20
    cmd = cmd.replace("INSERT ", "")
    parts = cmd.split()
    data = {}
    for p in parts:
        k, v = p.split("=")
        data[k] = v
    return data


def parse_delete(cmd: str):
    # DELETE 1
    _, num = cmd.split()
    return int(num)


def parse_find(cmd: str):
    # FIND name=Ali
    cmd = cmd.replace("FIND ", "")
    k, v = cmd.split("=")
    return k, v
