import re
S = input()
S = re.sub(r"[\w+]", "x", S)
print(S)
