# Benedict Browser

A simple, open-source web browser application that uses **DuckDuckGo** as the default search engine and runs locally on your computer using Python.

Your system's VPN connection is automatically used in the basic version since the browser runs through your computer's network stack.

## Features (Common to Both Versions)
- Basic web browsing functionality
- Back, forward, reload, and home buttons
- URL bar with DuckDuckGo search integration (type a query → searches DuckDuckGo; type a full URL → loads directly)
- DuckDuckGo set as default homepage and search engine
- Lightweight and runs entirely locally

## Two Versions Available

### 1. Basic Version (`simple_browser.py`)
- Uses your **system's default network connection**
- Automatically routes traffic through any active **system VPN** — no extra setup needed
- Ideal for everyday use or when you already have a VPN running system-wide

### 2. Proxy Version (`simple_browser_proxy.py`) — **New!**
- Built-in support for a **custom HTTP/SOCKS proxy**
- Designed to **bypass network restrictions** (e.g., school/work firewalls, regional blocks)
- You configure the proxy once in the code (or via a simple prompt/UI if extended later)
- All browser traffic goes through the specified proxy server instead of your direct connection
- Great for restricted networks where a system VPN isn't allowed or practical

## Installation Instructions (Same for Both Versions)

### Python Version (Recommended - Easier Setup)

#### Windows:
1. Install Python (if not already installed):
   - Download from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. Open Command Prompt and install dependencies:
pip install PyQt5 PyQtWebEngine
text3. Run the desired version:
- Basic: `python simple_browser.py`
- Proxy: `python simple_browser_proxy.py`

#### Mac:
1. Install Python (if not already installed):
brew install python
text2. Install dependencies:
pip3 install PyQt5 PyQtWebEngine
text3. Run:
- Basic: `python3 simple_browser.py`
- Proxy: `python3 simple_browser_proxy.py`

#### Linux (Ubuntu/Debian):
1. Install dependencies:
sudo apt update
sudo apt install python3-pip python3-pyqt5 python3-pyqt5.qtwebengine
text2. Run:
- Basic: `python3 simple_browser.py`
- Proxy: `python3 simple_browser_proxy.py`

---

### Java Version (Alternative – Basic only for now)
(No proxy version yet — contributions welcome!)

#### Requirements:
- Java Development Kit (JDK) 11 or later
- JavaFX SDK

#### Windows/Mac/Linux:
1. Install JDK: https://adoptium.net/
2. Download JavaFX: https://openjfx.io/ → extract to a known location (e.g., C:\javafx-sdk)
3. Compile:
javac --module-path /path/to/javafx-sdk/lib --add-modules javafx.controls,javafx.web SimpleBrowser.java
text4. Run:
java --module-path /path/to/javafx-sdk/lib --add-modules javafx.controls,javafx.web SimpleBrowser
text## Usage (Same for Both Versions)

1. **Navigate to websites**: Type a URL in the address bar and press Enter
2. **DuckDuckGo Search**: Type any search query (without a URL) and press Enter
3. **Navigation**: Use the arrow buttons to go back/forward
4. **Reload**: Click the refresh button
5. **Home**: Click the home button to return to DuckDuckGo

## Proxy Configuration (Proxy Version Only)

In `simple_browser_proxy.py`, you'll see a section near the top to set your proxy. Example:

```python
from PyQt5.QtNetwork import QNetworkProxy

# Configure your proxy here
proxy = QNetworkProxy()
proxy.setType(QNetworkProxy.HttpProxy)          # or QNetworkProxy.Socks5Proxy
proxy.setHostName("your.proxy.host")            # e.g., "proxy.example.com" or "127.0.0.1"
proxy.setPort(8080)                             # your proxy port
# If authentication is required:
# proxy.setUser("username")
# proxy.setPassword("password")

QNetworkProxy.setApplicationProxy(proxy)

Replace with your actual proxy details (free/public proxies, your own server, etc.)
Supports HTTP, HTTPS, and SOCKS5 proxies
Test with a working proxy before relying on it for bypassing restrictions
Warning: Only use trusted proxies — untrusted ones can intercept or log your traffic

VPN Usage

Basic version: Automatically uses your system's network → any active VPN works out of the box
Proxy version: Ignores system VPN/proxy settings and forces traffic through the configured proxy only

Notes

The Python version is recommended for easiest setup and maintenance
Proxy version added recently to help bypass network restrictions
All code is local — no telemetry or external dependencies beyond PyQt5
Feel free to fork and improve (e.g., add a GUI field for proxy settings, authentication support, proxy lists, etc.)
