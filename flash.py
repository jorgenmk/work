from pynrfjprog import API, Hex

class Flasher(object):
    def __init__(self, snr=682163995):
        self.snr = snr
        
    def flash(self, *hexfiles):
        self._open()
        self.api.erase_all()
        for i in hexfiles:
            app = Hex.Hex(i)
            for i in app:
                self.api.write(i.address, i.data, True)
        self.api.sys_reset()
        self.api.go()
        self._close()

    def memrd(self, addr, size):
        self._open()
        a = self.api.read(addr, size)
        self._close()
        return a


    def _open(self):
        self.api = API.API(API.DeviceFamily.NRF51)
        self.api.open()
        self.api.connect_to_emu_with_snr(self.snr)
        try:
            device_version = self.api.read_device_version()
        except API.APIError as e:
            if e.err_code == API.NrfjprogdllErr.WRONG_FAMILY_FOR_DEVICE: 
		self.api.close()
                self.api = API.API(API.DeviceFamily.NRF52)
                self.api.open()
                self.api.connect_to_emu_with_snr(self.snr)
    def _close(self):
        self.api.close()

if __name__ == '__main__':
    f = Flasher()
    f.flash('sd.hex','app.hex')
