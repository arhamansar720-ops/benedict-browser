# Benedict Browser, 

A simple, open-source web browser application that uses DuckDuckGo as the default search engine and runs locally on your computer using Python. Your VPN connection will automatically be used since the browser runs through your system's network connection.

## Features
- Basic web browsing functionality
- Back, forward, reload, and home buttons
- URL bar with DuckDuckGo search integration
- Automatically uses your system's VPN connection
- DuckDuckGo as default homepage and search engine

## Installation Instructions

### Python Version (Recommended - Easier Setup)

#### Windows:
1. Install Python (if not already installed):
   - Download from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. Open Command Prompt and install PyQt5:
   ```
   pip install PyQt5 PyQtWebEngine
   ```

3. Run the browser:
   ```
   python simple_browser.py
   ```

#### Mac:
1. Install Python (if not already installed):
   ```
   brew install python
   ```

2. Install PyQt5:
   ```
   pip3 install PyQt5 PyQtWebEngine
   ```

3. Run the browser:
   ```
   python3 simple_browser.py
   ```

#### Linux (Ubuntu/Debian):
1. Install dependencies:
   ```
   sudo apt update
   sudo apt install python3-pip python3-pyqt5 python3-pyqt5.qtwebengine
   ```

2. Run the browser:
   ```
   python3 simple_browser.py
   ```

---

### Java Version (Alternative)

#### Requirements:
- Java Development Kit (JDK) 11 or later
- JavaFX SDK

#### Windows/Mac/Linux:
1. Install JDK:
   - Download from https://adoptium.net/

2. Download JavaFX:
   - Get from https://openjfx.io/
   - Extract to a known location (e.g., C:\javafx-sdk)

3. Compile:
   ```
   javac --module-path /path/to/javafx-sdk/lib --add-modules javafx.controls,javafx.web SimpleBrowser.java
   ```

4. Run:
   ```
   java --module-path /path/to/javafx-sdk/lib --add-modules javafx.controls,javafx.web SimpleBrowser
   ```

---

## Usage

1. **Navigate to websites**: Type a URL in the address bar and press Enter
2. **DuckDuckGo Search**: Type any search query (without a URL) and press Enter
3. **Navigation**: Use the arrow buttons to go back/forward
4. **Reload**: Click the refresh button to reload the current page
5. **Home**: Click the home button to return to DuckDuckGo

## VPN Usage

The browser will automatically use whatever network connection your computer is using. If you have a VPN active on your system, all browser traffic will go through it automatically - no additional configuration needed!

## Notes

- The Python version is recommended for easier setup
- All traffic goes through your system's network connection (including VPN if active)
- DuckDuckGo is set as the default homepage and search engine
- The browser is lightweight and runs entirely on your local machine
