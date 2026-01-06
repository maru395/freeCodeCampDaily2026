def vowel_case(s):
  newS = ""
  for c in s:
    if c.upper() in "AEIOU":
      newS += c.upper()
    else:
      newS += c
  return newS
