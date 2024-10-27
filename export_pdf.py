from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget

class PDFReportApp(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def generate_pdf_report(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF Report", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if file_name:
            data = self.db.getAll()
            report_generator = PDFReportGenerator(file_name)
            report_generator.generate_report(data)

class PDFReportGenerator:
    def __init__(self, file_name):
        self.file_name = file_name

    def generate_report(self, data):
        c = canvas.Canvas(self.file_name, pagesize=letter)
        width, height = letter

        y = height - 40
        for record in data:
            c.drawString(30, y, str(record))
            y -= 20
            if y < 40:
                c.showPage()
                y = height - 40

        c.save()
