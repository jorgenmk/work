from flash import Flasher
from intelhex import IntelHex as ih
import time

for i in range(10):
    a = ih()
    a.loadhex('sd.hex')
    a.loadhex('app.hex')
    image_size = len(a)
    a.puts(image_size+1, "TestImage"+str(i))
    a.write_hex_file('test.hex')
    f = Flasher()
    f.flash('test.hex')
    time.sleep(1)
    string = f.memrd(image_size+1, 15)
    print ''.join(chr(x) for x in string)
