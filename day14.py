import re

def parse_link(markdown):
  link_text = re.search(r"\[(.*?)\]", markdown).group(1)
  link_url  = re.search(r"\((.*?)\)", markdown).group(1)
  return f"'<a href=\"{link_url}\">{link_text}</a>'"
