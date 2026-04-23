from pynput import keyboard
from PyQt6.QtCore import QObject, pyqtSignal

class KeyboardListener(QObject):
    key_pressed = pyqtSignal(str)
    key_released = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.active_keys = [] 

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def _get_key_name(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                char = key.char.lower()
                if char.isalnum():
                    return char
                elif char == ' ':
                    return 'space'
                else:
                    return 'function'
            else:
                special_key = str(key).replace('Key.', '')
                mapping = {
                    'space': 'space',
                    'enter': 'enter',
                    'shift': 'function',
                    'shift_r': 'function',
                    'ctrl': 'function',
                    'ctrl_r': 'function',
                    'alt': 'function',
                    'alt_r': 'function',
                    'cmd': 'function',
                    'cmd_r': 'function',
                    'tab': 'function',
                    'caps_lock': 'function',
                    'backspace': 'function',
                    'delete': 'function',
                    'esc': 'function',
                }
                return mapping.get(special_key, 'function')
        except:
            return 'function'

    def on_press(self, key):
        key_name = self._get_key_name(key)
        if key_name not in self.active_keys:
            self.active_keys.append(key_name)
        self.key_pressed.emit(key_name)

    def on_release(self, key):
        key_name = self._get_key_name(key)
        if key_name in self.active_keys:
            self.active_keys.remove(key_name)
        
        if self.active_keys:
            self.key_pressed.emit(self.active_keys[-1])
        else:
            self.key_released.emit('static')
