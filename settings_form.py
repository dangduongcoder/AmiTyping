import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QHBoxLayout

class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumWidth(300)

        self.layout = QVBoxLayout(self)

        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)

        self.char_name = QLineEdit("Ami")
        self.form_layout.addRow("Character Name:", self.char_name)

        # Buttons at bottom
        self.button_layout = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.accept)
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.reject)
        self.button_layout.addWidget(self.save_btn)
        self.button_layout.addWidget(self.close_btn)
        self.layout.addLayout(self.button_layout)

        # Author label
        self.author_label = QLabel("Author: Trương Đăng Dương")
        self.layout.addWidget(self.author_label)
