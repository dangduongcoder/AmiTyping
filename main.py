import sys
from PyQt6.QtWidgets import QApplication
from app_window import CharacterWindow
from keyboard_listener import KeyboardListener

def main():
    app = QApplication(sys.argv)
    
    window = CharacterWindow()
    window.show()
    
    listener = KeyboardListener()
    listener.key_pressed.connect(window.on_key_pressed)
    listener.key_released.connect(window.on_key_released)
    listener.start()
    
    try:
        sys.exit(app.exec())
    finally:
        listener.stop()

if __name__ == "__main__":
    main()
