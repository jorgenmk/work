from flash import Flasher
from intelhex import IntelHex as ih
import time

a = ih()
a.loadhex('sd.hex')
a.loadhex('app.hex')
b = len(a)
print b+1

a.puts(b+1, "String here")
a.write_hex_file('test.hex')


f = Flasher()
f.flash('test.hex')
time.sleep(1)
string = f.memrd(b+1, 11)
print ''.join(chr(x) for x in string)
