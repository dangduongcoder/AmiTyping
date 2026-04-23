import sys
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFormLayout,
    QSlider,
    QHBoxLayout,
    QApplication,
)
from PyQt6.QtCore import Qt

class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumWidth(300)

        # Main layout
        self.layout = QVBoxLayout(self)



        self.size_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_slider.setRange(100, 400)  # size in pixels
        self.size_slider.setValue(200)  # default size matches base_size
        self.size_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.size_slider.setTickInterval(50)
        self.layout.addWidget(QLabel("Kích thước nhân vật:"))
        self.layout.addWidget(self.size_slider)
        self.size_slider.valueChanged.connect(self.on_size_changed)

        self.button_layout = QHBoxLayout()
        self.save_btn = QPushButton("Lưu")
        self.save_btn.clicked.connect(self.accept)
        self.close_btn = QPushButton("Đóng")
        self.close_btn.clicked.connect(self.reject)
        self.kill_btn = QPushButton("Thoát")
        self.kill_btn.clicked.connect(self.kill_application)
        self.button_layout.addWidget(self.save_btn)
        self.button_layout.addWidget(self.close_btn)
        self.button_layout.addWidget(self.kill_btn)
        self.layout.addLayout(self.button_layout)


        # Author label
        self.author_label = QLabel()
        self.author_label.setText('<a href="https://github.com/dangduongcoder">Trương Đăng Dương - D24CE01</a>')
        self.author_label.setOpenExternalLinks(True)
        self.layout.addWidget(self.author_label)

    def on_size_changed(self, value):
        """Handle slider value change and update character size in parent window."""
        if self.parent() is not None:
            try:
                self.parent().set_character_size(value)
            except Exception:
                pass

    def kill_application(self):
        """Terminate the entire application."""
        from PyQt6.QtWidgets import QApplication
        QApplication.instance().quit()
