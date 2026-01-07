import re

def parse_unordered_list(markdown):
  words = []
  for md in markdown:
    md = re.sub(r"[-\s]", "", md)
    words.append(md)
  formatted = []
  for w in words:
    f = re.sub(r'^(.*)$', r'<li>\1</li>', w)
    formatted.append(f)
  return formatted
