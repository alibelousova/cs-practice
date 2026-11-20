import json


def csv_to_records(text):
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    head = lines[0].split(',')
    data = []
    for line in lines[1:]:
        values = line.split(',')
        data.append(dict(zip(head, values)))
    return data


def _convert(value):
    value = value.strip()
    low = value.lower()
    if low in ('true', 'yes'):
        return True
    if low in ('false', 'no'):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def parse_settings(lines):
    settings = {}
    current_list = None
    for line in lines:
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        if line.startswith('-'):
            if current_list is not None:
                current_list.append(_convert(line[1:]))
            continue
        key, _, value = line.partition(':')
        key = key.strip()
        value = value.strip()
        if value == '':
            current_list = []
            settings[key] = current_list
        else:
            current_list = None
            settings[key] = _convert(value)
    return settings


def merge_by_key(rows, extra, key='id'):
    result = []
    for row in rows:
        info = extra.get(row.get(key))
        if info is None:
            info = extra.get(str(row.get(key)), {})
        result.append({**info, **row})
    return result


def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)


if __name__ == '__main__':
    print(csv_to_records("id,город\n1,Азов\n2,Шахты\n"))
    print(parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1",
                          "active: true", "columns:", "  - город", "  - цена"]))
    print(merge_by_key([{"id": "1", "город": "Азов"}],
                       {"1": {"регион": "Ростовская"}}, "id"))
    print(records_to_json([{"id": "1", "город": "Азов"}]))