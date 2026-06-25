import re

def parse_frontmatter(md: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---", md, re.DOTALL)
    if not match:
        return {}

    result = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif re.fullmatch(r"\d+", value):
                value = int(value)
            elif re.fullmatch(r"\d+\.\d+", value):
                value = float(value)
            result[key] = value

    return result
