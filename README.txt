# Benedict Browser - Complete Edition

A feature-rich, privacy-focused web browser built with Python and PyQt5. Uses **DuckDuckGo** as the default search engine and runs entirely on your local computer.

![Version](https://img.shields.io/badge/version-2.0-blue) ![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

### 🌐 Core Browsing
- **Multi-tab support** - Open and manage multiple tabs like modern browsers
- **DuckDuckGo integration** - Privacy-focused search as default
- **Smart URL bar** - Type searches or URLs directly
- **Free AI access** - One-click DuckDuckGo AI chat in new tabs
- **Full navigation controls** - Back, forward, reload, home buttons

### 🎨 Customization
- **Dark/Light mode** - Toggle themes via settings
- **Custom homepage** - Set any URL as your homepage
- **Modern UI** - Clean, professional interface
- **Tab management** - Closable, movable tabs with titles

### 🔒 Privacy & Performance
- **Local-first** - All browsing happens on your machine
- **VPN compatible** - Automatically uses system VPN when active
- **Lightweight** - Fast and efficient
- **No tracking** - DuckDuckGo doesn't track your searches

---

## 🚀 Quick Start

### Installation

**Requirements:**
- Python 3.6 or later
- PyQt5 and PyQtWebEngine

**Install dependencies:**

**Windows:**
```bash
pip install PyQt5 PyQtWebEngine
```

**Mac:**
```bash
pip3 install PyQt5 PyQtWebEngine
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3-pip python3-pyqt5 python3-pyqt5.qtwebengine
```

### Run Benedict Browser

```bash
python benedict_browser_complete.py
```

**Mac/Linux:**
```bash
python3 benedict_browser_complete.py
```

---

## 📖 Usage Guide

### Basic Navigation

**Search or Visit Sites:**
- Type in the URL bar and press Enter
- Search queries: `python tutorial` → searches DuckDuckGo
- Direct URLs: `github.com` or `https://github.com` → loads site

**Navigation Buttons:**
- **◄** Back - Go to previous page
- **►** Forward - Go to next page
- **↻** Reload - Refresh current page
- **⌂** Home - Return to homepage (DuckDuckGo by default)

### Tab Management

**Open New Tab:**
- Click the **+** button next to existing tabs
- Or click **AI** button to open DuckDuckGo AI in new tab

**Close Tab:**
- Click the **X** on any tab
- Last tab won't close (goes to homepage instead)

**Switch Tabs:**
- Click on any tab to switch
- Drag tabs to reorder them

**Tab Features:**
- Tabs show page titles automatically
- URL bar updates when switching tabs
- Each tab browses independently

### Settings Menu

**Access Settings:**
Click the **☰** (hamburger menu) button in the toolbar

**Available Settings:**

1. **Theme Selection**
   - Dark Mode (default) - Black/blue color scheme
   - Light Mode - White/blue color scheme
   - Changes apply immediately

2. **Homepage**
   - Set custom homepage URL
   - Default: `https://duckduckgo.com`
   - Enter any valid URL

**Save Settings:**
Click **Save** to apply changes

### DuckDuckGo AI

**Access Free AI:**
- Click the **AI** button in toolbar
- Opens DuckDuckGo AI chat in new tab
- No API keys or accounts needed
- Completely free to use

---

## 🔧 Advanced Features

### VPN Integration

Benedict Browser automatically uses your **system's network connection**:

1. **Connect to your VPN** (ProtonVPN, NordVPN, etc.)
2. **Open Benedict Browser**
3. ✅ All traffic automatically routes through VPN

**Recommended free VPNs:**
- ProtonVPN (unlimited free tier)
- Windscribe (10GB/month free)
- TunnelBear (500MB/month free)

### Keyboard Shortcuts

- `Ctrl + L` (Windows/Linux) or `Cmd + L` (Mac) - Focus URL bar
- `Backspace` - Go back
- `Ctrl + R` or `F5` - Reload page
- `Ctrl + T` - New tab (if implemented)

### Custom Homepage

**To change your homepage:**
1. Click **☰** (settings menu)
2. Enter new URL in **Homepage** field
3. Examples:
   - `https://google.com`
   - `https://github.com`
   - `https://news.ycombinator.com`
4. Click **Save**

---

## 🎨 Themes

### Dark Mode (Default)
- Background: Deep black (#0A0A0A)
- Surfaces: Dark gray (#1E1E1E)
- Accent: Blue (#4A90E2)
- Text: White
- Easy on eyes for long browsing sessions

### Light Mode
- Background: White (#FFFFFF)
- Surfaces: Light gray (#F5F5F5)
- Accent: Blue (#4A90E2)
- Text: Black
- Clean, professional appearance

**Toggle themes anytime via Settings menu**

---

## 💡 Tips & Tricks

### Efficient Browsing
1. **Use tabs** for multiple sites instead of multiple windows
2. **Drag tabs** to organize your workflow
3. **Set homepage** to your most-visited site
4. **Use dark mode** for night browsing

### Privacy Tips
1. **Use DuckDuckGo search** - no tracking
2. **Enable system VPN** for additional privacy
3. **Use DuckDuckGo AI** instead of ChatGPT (no login required)

### Search Shortcuts
DuckDuckGo supports "bangs" for quick searches:
- `!w python` - Search Wikipedia
- `!yt music` - Search YouTube
- `!gh repository` - Search GitHub
- `!so error message` - Search Stack Overflow

---

## 🐛 Troubleshooting

### Common Issues

**"Module not found" Error**
```bash
pip install PyQt5 PyQtWebEngine
```
Or try:
```bash
python -m pip install PyQt5 PyQtWebEngine
```

**Browser window is blank**
- Reinstall PyQtWebEngine: `pip uninstall PyQtWebEngine` then `pip install PyQtWebEngine`
- Update PyQt5: `pip install --upgrade PyQt5`

**Tabs not working**
- Ensure you're running the latest version
- Restart the browser
- Check console for error messages

**Settings don't save**
- Close and reopen browser to apply changes
- Check file permissions in browser directory

**VPN not working**
- Connect to VPN **before** opening browser
- Verify VPN connection is active
- Test with regular browser first

---

## 📊 System Requirements

**Minimum:**
- OS: Windows 7+, macOS 10.12+, Linux (most distributions)
- Python: 3.6 or later
- RAM: 512 MB
- Disk: 200 MB for dependencies

**Recommended:**
- OS: Windows 10+, macOS 11+, Ubuntu 20.04+
- Python: 3.8 or later
- RAM: 2 GB
- Disk: 500 MB

---

## 🎓 For CS Projects & Learning

### Educational Value

Benedict Browser demonstrates:
- ✅ GUI development with PyQt5
- ✅ Web rendering with QtWebEngine
- ✅ Tab management and state handling
- ✅ Settings persistence
- ✅ Theme/styling systems
- ✅ Event-driven programming

### Extending the Browser

**Ideas for enhancements:**
- Bookmark system
- Download manager
- History tracking
- Extensions/plugins
- Custom themes
- Incognito mode
- Password manager
- Ad blocking

**Code is open for modification and learning!**

---

## 🔐 Security & Privacy

### What Benedict Browser Does:
- ✅ Uses privacy-focused DuckDuckGo
- ✅ Runs completely locally
- ✅ No telemetry or tracking
- ✅ No data collection
- ✅ Compatible with VPNs

### What Benedict Browser Doesn't Do:
- ❌ No built-in ad blocking (use system-level blockers)
- ❌ No automatic HTTPS upgrade (type https:// manually)
- ❌ No incognito/private mode (yet)
- ❌ No password management

**For maximum privacy:**
1. Use with a VPN
2. Use DuckDuckGo for searches
3. Clear browser cache regularly (via system)
4. Don't save sensitive passwords

---

## 🆚 Comparison with Other Browsers

| Feature | Benedict | Chrome | Firefox | Edge |
|---------|----------|--------|---------|------|
| Open Source | ✅ | ❌ | ✅ | ❌ |
| Lightweight | ✅ | ❌ | ⚠️ | ❌ |
| Privacy-focused | ✅ | ❌ | ✅ | ❌ |
| Tab Support | ✅ | ✅ | ✅ | ✅ |
| Extensions | ❌ | ✅ | ✅ | ✅ |
| Custom Themes | ✅ | ⚠️ | ✅ | ⚠️ |
| VPN Compatible | ✅ | ✅ | ✅ | ✅ |
| Resource Usage | Low | High | Medium | Medium |

---

## 📜 Version History

### v2.0 (Current) - Complete Edition
- ✅ Multi-tab support
- ✅ Dark/Light mode themes
- ✅ Settings menu
- ✅ Custom homepage
- ✅ Improved UI/UX
- ✅ Tab management features

### v1.0 - Basic Edition
- Basic browsing functionality
- DuckDuckGo integration
- Simple dark theme
- Single-window browsing

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Bookmark system
- History management
- Download manager
- Extension support
- Additional themes
- Performance optimizations

**To contribute:**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - Free to use, modify, and distribute

---

## 🙏 Acknowledgments

Built with:
- **Python** - Programming language
- **PyQt5** - GUI framework
- **QtWebEngine** - Web rendering engine
- **DuckDuckGo** - Privacy-focused search

---

## 📞 Support

**Found a bug?** Open an issue on GitHub
**Have a question?** Check the troubleshooting section above
**Want to contribute?** See contributing guidelines

---

## 🎯 Quick Reference

**Start Browser:**
```bash
python benedict_browser_complete.py
```

**New Tab:** Click `+` button
**Close Tab:** Click `X` on tab
**Settings:** Click `☰` button
**DuckDuckGo AI:** Click `AI` button
**Change Theme:** Settings → Select theme → Save
**Set Homepage:** Settings → Enter URL → Save

---

**Enjoy browsing with Benedict Browser!** 🌐🔒

Built for privacy, designed for simplicity.
