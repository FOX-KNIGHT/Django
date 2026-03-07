import re

pattern= r"c[aeiou]t$"
pattern2= r"c[a-z]t$"
inp=input()

print(re.match(pattern,inp))