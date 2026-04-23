import sys
import os
from PyQt6.QtWidgets import (QMainWindow, QLabel, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QApplication)
from PyQt6.QtCore import Qt, QPoint, QSize, QTimer, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPixmap, QCursor, QMouseEvent, QIcon
from settings_form import SettingsForm

class CharacterWindow(QMainWindow):
    key_pressed_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        
        self.image_dir = os.path.join(os.path.dirname(__file__), "images")
        self.current_scale = 1.0
        self.base_size = QSize(200, 200) 
        
        self.init_ui()
        self.load_image("static")
        
        icon_path = os.path.join(self.image_dir, "static.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            
        self.drag_position = QPoint()

    def init_ui(self):
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Window
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.image_label)
        
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(5, 0, 5, 5)
        self.buttons_layout.setSpacing(5)
        self.layout.addLayout(self.buttons_layout)
        
        # self.zoom_btn = QPushButton()
        # self.zoom_btn.setFixedSize(30, 30)
        # self.zoom_btn.setStyleSheet("background: transparent; border: none;")
        # self.zoom_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # zoom_pixmap = QPixmap(os.path.join(self.image_dir, "button_zoom.png"))
        # if not zoom_pixmap.isNull():
        #     self.zoom_btn.setIcon(QIcon(zoom_pixmap.scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)))
        #     self.zoom_btn.setIconSize(QSize(24, 24))
        # self.zoom_btn.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # self.zoom_btn.clicked.connect(self.zoom_out)
        # self.zoom_btn.customContextMenuRequested.connect(self.zoom_in)
        # self.buttons_layout.addWidget(self.zoom_btn)
        
        self.setting_btn = QPushButton()
        self.setting_btn.setFixedSize(30, 30)
        self.setting_btn.setStyleSheet("background: transparent; border: none;")
        self.setting_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        setting_pixmap = QPixmap(os.path.join(self.image_dir, "button_setting.png"))
        if not setting_pixmap.isNull():
            self.setting_btn.setIcon(QIcon(setting_pixmap.scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)))
            self.setting_btn.setIconSize(QSize(24, 24))
        self.setting_btn.clicked.connect(self.open_settings)
        self.buttons_layout.addWidget(self.setting_btn)
        
        self.move_to_bottom_right()

    def move_to_bottom_right(self):
        screen = QApplication.primaryScreen().geometry()
        self.adjustSize()
        x = screen.width() - self.width() - 150
        y = screen.height() - self.height() - 250
        self.move(x, y)

    def load_image(self, key_name):
        path = os.path.join(self.image_dir, f"{key_name}.png")
        if not os.path.exists(path):
            path = os.path.join(self.image_dir, "static.png")
            
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(
                self.base_size * self.current_scale, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.adjustSize()

    @pyqtSlot(str)
    def on_key_pressed(self, key_name):
        self.load_image(key_name)

    @pyqtSlot(str)
    def on_key_released(self, key_name):
        self.load_image(key_name)

    def zoom_in(self):
        old_bottom = self.frameGeometry().bottom()
        self.current_scale *= 1.05
        self.load_image("static")
        self.move(self.x(), old_bottom - self.height())

    def zoom_out(self):
        old_bottom = self.frameGeometry().bottom()
        self.current_scale *= 0.95
        self.load_image("static")
        self.move(self.x(), old_bottom - self.height())

    def set_character_size(self, size):
        """Adjust the character display size.
        `size` is the desired base dimension in pixels (width = height)."""
        self.base_size = QSize(size, size)
        self.load_image("static")

    def open_settings(self):
        form = SettingsForm(self)
        form.exec()


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
