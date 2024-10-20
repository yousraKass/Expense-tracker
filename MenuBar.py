from PyQt5.QtWidgets import (
    QMenuBar, QMenu
)


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_menu_bar()

    def setup_menu_bar(self):
        file_menu = QMenu("File", self)
        edit_menu = QMenu("Edit", self)
        help_menu = QMenu("Help", self)
        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(help_menu)