import struct
try:
    with open("data.txt","w+") as f:
        f.write(input("Enter text: "))
        f.seek(0)
        print("File Contents:\n"+f.read())

except:
    print("File already exists!")

with open("binary.dat","w+b") as b:
    int_list = [10,20,30,40,50,60,70]
    for i in int_list:
        b.write(struct.pack("h",i))
    b.seek(0)
    res = []
    r = b.read(2)
    while r:
        res.append(struct.unpack("h",r)[0])
        r = b.read(2)
    print("Binary File Content:\n",res)