import re

pattern= r"(\d| ){,14}$"
pattern2= r"\d{4} \d{4} \d{4}$"
inp=input()

print(re.match(pattern,inp))
print(re.match(pattern2,inp))
aad=re.match(pattern2,inp)
if aad!= None:
    print("Valid Aadhar")

