s1='abc'
s2='def'
s3='sidd'
s4=""
l=['a','b','c']
for i in s1, s2 , s3:
    for j in i:
        '''print(i, end=" ")'''
        s4+=j+" "

print(s4)

print(' '.join(s1))
print('1'.join(s1))
print(' '.join(l))