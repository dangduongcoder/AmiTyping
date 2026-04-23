import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout

class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Setting")
        self.setMinimumWidth(300)
        
        self.layout = QVBoxLayout(self)
        
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        
        self.char_name = QLineEdit("Ami")
        self.form_layout.addRow("Character Name:", self.char_name)
        
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.accept)
        self.layout.addWidget(self.save_btn)
