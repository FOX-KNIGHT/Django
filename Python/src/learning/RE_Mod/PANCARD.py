import re

pattern= r"[A-Z]{5}\d{4}[A-Z]"
inp=input("This is my PANCARD NO:")

print(re.search(pattern,inp))
print(re.findall(pattern,inp))

pan=re.match(pattern,inp)
if pan!= None:
    print("Valid PANCARD")