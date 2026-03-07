import re

pattern=r'(ab)c+$'
pattern2=r'a(bc)+$'
pattern3=r'abc+$'

inp=input()

print(re.match(pattern,inp))
print(re.match(pattern2,inp))
print(re.match(pattern3,inp))