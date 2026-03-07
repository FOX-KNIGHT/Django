import re
  
pattern= r"([a-zA-Z]*: )(?:[\+\s]*91|0091|\(91\))[ -]*([1-9]{5})[ -]*([0-9]{5})"
s="Contact: +91-9876543210, Office: (91) 98765 43210, Home: 0091 9876543210"
lst=re.findall(pattern,s)

print(lst)
for i in lst:
    print(i[0]+"+91-"+i[1]+i[2])