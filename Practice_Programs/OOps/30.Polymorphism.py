#30. Document Exporters

class Exporter:
    def export(self):
        pass

class PDFExporter(Exporter):
     def export(self):
         print("Exporting to PDF...")

class CSVExporter(Exporter):
     def export(self):
         print("Exporting to CSV...")


for tool in [PDFExporter(), CSVExporter()]:
    tool.export()