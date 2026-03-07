import re

pattern= r'\d{1,3}(?:,\d{3})*(?:\.\d*)?\b'
s="1,324,432,546  is my salary for the year"
lst=re.findall(pattern,s)

print(lst)
for item in lst:
    print(item)
