import re

def extract_attributes(element):
    return [f"{n}, {v}" for n, v in re.findall(r'(\w+)="([^"]*)"', element)]
