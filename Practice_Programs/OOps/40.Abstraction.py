#40. Abstract Report Generator

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
   @abstractmethod
   def generate(self):
       pass

class ExcelReport(ReportGenerator):
    def generate(self):
        print("Generating Excel report")

r = ExcelReport()
r.generate()