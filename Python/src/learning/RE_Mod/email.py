import re

pattern= r".*@.*(.com)|(.org)|(.in)$"
pattern2=r'.*@((gmail)|(yahoo)|(reddif))((.com)|(.org)|(.in))$'
inp=input()

print(re.match(pattern,inp))
print(re.match(pattern2,inp))
