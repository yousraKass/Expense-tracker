from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel
)

class TotalDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.total_value = QLabel("0.00")
        self.setup_total_layout()

    def setup_total_layout(self):
        layout = QHBoxLayout(self)
        total_label = QLabel("Total:")
        layout.addWidget(total_label)
        layout.addWidget(self.total_value)

    def update_total(self, total):
        self.total_value.setText(f"{total:.2f}")
