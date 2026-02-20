#22. Printer Interface

class Printer:
    def print_file(self):
       print("Generic printing")

class InkjetPrinter(Printer):
     def print_file(self):
       print("Inkjet printing...")

class LaserPrinter(Printer):  
     def print_file(self):
        print("Laser printing...")

def start_printing(printer):
    printer.print_file()

start_printing(InkjetPrinter())
start_printing(LaserPrinter())