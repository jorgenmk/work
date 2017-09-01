from flash import Flasher
from intelhex import IntelHex as ih
import time
import os
import sys

for f in os.listdir('.'):
    if f.startswith('bootloader'):
        for string in (['var1', 'var2', 'var3']):
            a = ih(f)
            #a.loadhex('sd.hex')
            #a.loadhex('app.hex')

            #image_size = a.addresses()[-5] + 1
            #print format(image_size, '08X')
            #a.puts(image_size, string)
            a.write_hex_file(string+"_"+f)
    #f = Flasher(681598975)
    #f.flash('test.hex')
    #time.sleep(1)
    #string = f.memrd(image_size+1, 15)
    #print ''.join(chr(x) for x in string)
    
    # Comment
