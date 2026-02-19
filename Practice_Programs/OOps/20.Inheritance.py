#20. Device and Laptop

class Device:
    def power_on(self):
        print("Device is powered on.")


class Laptop(Device):
    def open_ide(self):
        print("IDE opened.")

l = Laptop()
l.power_on()
l.open_ide()