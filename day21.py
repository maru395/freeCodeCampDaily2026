import re

def parse_inline_code(markdown):
    markdown = re.sub(r'`([^`]*)`', r'<code>\1</code>', markdown)
    return markdown
