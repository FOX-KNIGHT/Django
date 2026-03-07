"""s="abc"
print(s[::-1])

print("".join(reversed(s)))

for i in reversed(s):
    print(i,end='')
print()

s1=""
for i in s[::-1]:
    s1=s1+i
print(s1)

for i in s:
    s1=i+s1
print(s1)
"""

s="abc def ghi"
"""for i in reversed(s.split()):
    print(i, end=" ")

print()

s1=list(reversed(s.split()))
for i in s1:
    print(i, end=" ")"""

print()

"""s2=s.split()
for i in s2:
    print("".join(reversed(i)),end=" ")"""

"""s='A1B2C3'
s1=""
s2=""
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(s1+s2)"""


s1="a5b4c3"
s3=""
s2=""
for i in s1:
    if i.isalpha():
        s2=i
    else:
        s3=s2*int(i)
        print(s3, end="")