# Build Instructions for AmiTyping

## Overview
AmiTyping is a cross‑platform desktop application built with **Python**, **PyQt6**, and **pynput**. Below are the steps to package the app into a standalone executable for **macOS**, **Windows**, and **Linux** using **PyInstaller**.

## Prerequisites
1. Python 3.8+ installed.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Install **PyInstaller** globally (or in a virtual environment):
   ```bash
   pip install pyinstaller
   ```

## Common PyInstaller Options
- `--onefile` – bundle everything into a single executable.
- `--windowed` – hide the console window (GUI app).
- `--icon <path>` – set the application icon (use `images/static.png`).
- `--add-data "images:images"` – include the `images` folder.

## macOS Build
```bash
pyinstaller \
  --onefile \
  --windowed \
  --icon images/static.png \
  --add-data "images:images" \
  main.py
```
The resulting executable will be located in `dist/main`.

## Windows Build
```bash
pyinstaller \
  --onefile \
  --windowed \
  --icon images/static.png \
  --add-data "images;images" \
  main.py
```
**Note:** Use a semicolon (`;`) to separate source and destination for `--add-data` on Windows.

## Linux Build
```bash
pyinstaller \
  --onefile \
  --windowed \
  --icon images/static.png \
  --add-data "images:images" \
  main.py
```

## Post‑Build Steps
1. Verify the executable runs without errors on the target OS.
2. Distribute the `dist/` folder contents (the executable and any required dynamic libraries if needed).
3. Optionally create an installer (e.g., using `NSIS` for Windows or `pkgbuild` for macOS).

## Troubleshooting
- **Missing images:** Ensure the `images` folder is correctly packaged (`--add-data`).
- **Icon not showing on Windows taskbar:** The window flag `Qt.Window` (set in `app_window.py`) together with `setWindowIcon` ensures the taskbar icon appears.
- **Accessibility permissions on macOS/Linux:** Grant the necessary permissions for global keyboard listening as described in the README.
