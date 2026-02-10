"""
Benedict Browser - Portable Edition
Auto-installs dependencies and runs without CMD access
Just double-click or run in any IDE (jGRASP, IDLE, PyCharm, etc.)
"""

import sys
import subprocess
import importlib.util

def check_and_install(package_name, import_name=None):
    """Check if package is installed, if not install it"""
    if import_name is None:
        import_name = package_name
    
    if importlib.util.find_spec(import_name) is None:
        print(f"Installing {package_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✓ {package_name} installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {package_name}")
            print(f"Please install manually: pip install {package_name}")
            return False
    return True

# Auto-install dependencies
print("Benedict Browser - Checking dependencies...")
print("-" * 50)

required_packages = [
    ("PyQt5", "PyQt5"),
    ("PyQtWebEngine", "PyQt5.QtWebEngineWidgets")
]

all_installed = True
for package, import_name in required_packages:
    if not check_and_install(package, import_name):
        all_installed = False

if not all_installed:
    print("\n⚠️ Some dependencies failed to install.")
    print("Browser may not work correctly.")
    input("Press Enter to try running anyway...")

print("-" * 50)
print("Starting Benedict Browser...")
print()

# Now import and run the browser
from PyQt5.QtCore import QUrl, Qt, QSize, QSettings
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                             QLineEdit, QAction, QVBoxLayout, QWidget,
                             QTabWidget, QPushButton, QHBoxLayout, QMenu,
                             QDialog, QLabel, QRadioButton, QButtonGroup, QMessageBox)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont, QIcon

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Settings')
        self.setModal(True)
        self.setMinimumWidth(400)
        self.parent_browser = parent
        
        layout = QVBoxLayout()
        
        # Theme section
        theme_label = QLabel('Theme:')
        theme_label.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(theme_label)
        
        self.theme_group = QButtonGroup()
        self.dark_radio = QRadioButton('Dark Mode')
        self.light_radio = QRadioButton('Light Mode')
        
        self.theme_group.addButton(self.dark_radio, 0)
        self.theme_group.addButton(self.light_radio, 1)
        
        # Set current theme
        if parent and hasattr(parent, 'is_dark_mode'):
            if parent.is_dark_mode:
                self.dark_radio.setChecked(True)
            else:
                self.light_radio.setChecked(True)
        else:
            self.dark_radio.setChecked(True)
        
        layout.addWidget(self.dark_radio)
        layout.addWidget(self.light_radio)
        
        layout.addSpacing(20)
        
        # Homepage section
        homepage_label = QLabel('Homepage:')
        homepage_label.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(homepage_label)
        
        self.homepage_input = QLineEdit()
        self.homepage_input.setText(parent.home_url if parent else 'https://duckduckgo.com')
        layout.addWidget(self.homepage_input)
        
        layout.addSpacing(20)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton('Save')
        save_btn.clicked.connect(self.save_settings)
        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_settings(self):
        # Save theme
        if self.dark_radio.isChecked():
            self.parent_browser.set_dark_mode()
        else:
            self.parent_browser.set_light_mode()
        
        # Save homepage
        new_home = self.homepage_input.text().strip()
        if new_home:
            self.parent_browser.home_url = new_home
        
        self.accept()


class BrowserTab(QWidget):
    def __init__(self, parent=None, url=None):
        super().__init__(parent)
        self.parent_browser = parent
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Browser view
        self.browser = QWebEngineView()
        self.browser.setZoomFactor(0.9)
        layout.addWidget(self.browser)
        
        # Load URL
        if url:
            self.browser.setUrl(QUrl(url))
        else:
            self.browser.setUrl(QUrl('https://duckduckgo.com'))
        
        # Connect signals
        self.browser.urlChanged.connect(self.update_url)
        self.browser.titleChanged.connect(self.update_title)
        
        self.setLayout(layout)
    
    def update_url(self, url):
        if self.parent_browser:
            self.parent_browser.update_url_bar(url)
    
    def update_title(self, title):
        if self.parent_browser:
            self.parent_browser.update_tab_title(self, title)


class BenedictBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Benedict Browser - Portable Edition')
        self.setGeometry(100, 100, 1400, 900)
        
        self.home_url = 'https://duckduckgo.com'
        self.is_dark_mode = True
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        main_widget.setLayout(layout)
        
        # Create toolbar
        toolbar = self.create_toolbar()
        self.addToolBar(toolbar)
        
        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        
        # Add new tab button
        self.tabs.setCornerWidget(self.create_new_tab_button(), Qt.TopRightCorner)
        
        layout.addWidget(self.tabs)
        
        # Add first tab
        self.add_new_tab()
        
        # Apply dark mode
        self.set_dark_mode()
    
    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(20, 20))
        toolbar.setMinimumHeight(45)
        
        # Back button
        self.back_btn = QAction('Back', self)
        self.back_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.back_btn.setToolTip('Back')
        self.back_btn.triggered.connect(self.navigate_back)
        toolbar.addAction(self.back_btn)
        
        # Forward button
        self.forward_btn = QAction('Fwd', self)
        self.forward_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.forward_btn.setToolTip('Forward')
        self.forward_btn.triggered.connect(self.navigate_forward)
        toolbar.addAction(self.forward_btn)
        
        # Reload button
        self.reload_btn = QAction('Reload', self)
        self.reload_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.reload_btn.setToolTip('Reload')
        self.reload_btn.triggered.connect(self.reload_page)
        toolbar.addAction(self.reload_btn)
        
        # Home button
        self.home_btn = QAction('Home', self)
        self.home_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.home_btn.setToolTip('Home')
        self.home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(self.home_btn)
        
        toolbar.addSeparator()
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search DuckDuckGo or enter URL...")
        self.url_bar.setFont(QFont("Arial", 12))
        self.url_bar.setMinimumHeight(32)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        toolbar.addSeparator()
        
        # DuckDuckGo AI button
        ddg_ai_btn = QAction('AI', self)
        ddg_ai_btn.setFont(QFont("Arial", 12, QFont.Bold))
        ddg_ai_btn.setToolTip('DuckDuckGo AI Chat')
        ddg_ai_btn.triggered.connect(self.open_duckduckgo_ai)
        toolbar.addAction(ddg_ai_btn)
        
        # Settings button (menu)
        self.settings_btn = QAction('Settings', self)
        self.settings_btn.setFont(QFont("Arial", 11, QFont.Bold))
        self.settings_btn.setToolTip('Settings')
        self.settings_btn.triggered.connect(self.show_settings_menu)
        toolbar.addAction(self.settings_btn)
        
        self.toolbar = toolbar
        return toolbar
    
    def create_new_tab_button(self):
        new_tab_btn = QPushButton('+')
        new_tab_btn.setFont(QFont("Arial", 16, QFont.Bold))
        new_tab_btn.setFixedSize(30, 30)
        new_tab_btn.setToolTip('New Tab')
        new_tab_btn.clicked.connect(self.add_new_tab)
        return new_tab_btn
    
    def add_new_tab(self, url=None):
        """Add a new tab"""
        tab = BrowserTab(self, url)
        
        # Add tab with title
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)
        
        # Focus URL bar
        self.url_bar.setFocus()
    
    def close_tab(self, index):
        """Close a tab"""
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            # Don't close last tab, just go home
            self.navigate_home()
    
    def tab_changed(self, index):
        """Update URL bar when switching tabs"""
        if index >= 0:
            current_tab = self.tabs.widget(index)
            if current_tab and hasattr(current_tab, 'browser'):
                url = current_tab.browser.url().toString()
                self.url_bar.setText(url)
    
    def update_tab_title(self, tab, title):
        """Update tab title when page title changes"""
        index = self.tabs.indexOf(tab)
        if index >= 0:
            # Limit title length
            if len(title) > 20:
                title = title[:20] + "..."
            self.tabs.setTabText(index, title)
    
    def current_browser(self):
        """Get current tab's browser"""
        current_tab = self.tabs.currentWidget()
        if current_tab and hasattr(current_tab, 'browser'):
            return current_tab.browser
        return None
    
    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        
        if not url:
            return
        
        browser = self.current_browser()
        if not browser:
            return
        
        # Check if it's already a full URL
        if url.startswith('http://') or url.startswith('https://'):
            final_url = url
        # Check if it contains a space or no dot - it's a search
        elif ' ' in url or '.' not in url:
            # It's a search query
            final_url = f'https://duckduckgo.com/?q={url.replace(" ", "+")}'
        else:
            # It's probably a domain
            final_url = 'https://' + url
        
        browser.setUrl(QUrl(final_url))
    
    def navigate_back(self):
        browser = self.current_browser()
        if browser:
            browser.back()
    
    def navigate_forward(self):
        browser = self.current_browser()
        if browser:
            browser.forward()
    
    def reload_page(self):
        browser = self.current_browser()
        if browser:
            browser.reload()
    
    def navigate_home(self):
        browser = self.current_browser()
        if browser:
            browser.setUrl(QUrl(self.home_url))
    
    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())
    
    def open_duckduckgo_ai(self):
        """Open DuckDuckGo AI in new tab"""
        self.add_new_tab('https://duckduckgo.com/chat')
    
    def show_settings_menu(self):
        """Show settings dialog"""
        dialog = SettingsDialog(self)
        dialog.exec_()
    
    def set_dark_mode(self):
        """Apply dark mode theme"""
        self.is_dark_mode = True
        
        dark_style = """
            QMainWindow {
                background-color: #0A0A0A;
            }
            QWidget {
                background-color: #1E1E1E;
                color: #FFFFFF;
                font-size: 13px;
            }
            QToolBar {
                background-color: #1E1E1E;
                border: none;
                padding: 5px;
                spacing: 3px;
            }
            QToolButton {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #3D3D3D;
                border-radius: 5px;
                padding: 6px 10px;
                min-width: 35px;
                min-height: 35px;
            }
            QToolButton:hover {
                background-color: #3D3D3D;
                border: 1px solid #4A90E2;
            }
            QToolButton:pressed {
                background-color: #4A90E2;
            }
            QLineEdit {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 2px solid #3D3D3D;
                border-radius: 6px;
                padding: 8px 12px;
                selection-background-color: #4A90E2;
            }
            QLineEdit:focus {
                border: 2px solid #4A90E2;
                background-color: #353535;
            }
            QTabWidget::pane {
                border: 1px solid #3D3D3D;
                background-color: #1E1E1E;
            }
            QTabBar::tab {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #3D3D3D;
                padding: 8px 15px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #4A90E2;
                border-bottom: 2px solid #4A90E2;
            }
            QTabBar::tab:hover {
                background-color: #3D3D3D;
            }
            QPushButton {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #3D3D3D;
                border-radius: 4px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #3D3D3D;
                border: 1px solid #4A90E2;
            }
            QPushButton:pressed {
                background-color: #4A90E2;
            }
            QDialog {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            QLabel {
                color: #FFFFFF;
                background-color: transparent;
            }
            QRadioButton {
                color: #FFFFFF;
                background-color: transparent;
            }
        """
        
        self.setStyleSheet(dark_style)
    
    def set_light_mode(self):
        """Apply light mode theme"""
        self.is_dark_mode = False
        
        light_style = """
            QMainWindow {
                background-color: #FFFFFF;
            }
            QWidget {
                background-color: #F5F5F5;
                color: #000000;
                font-size: 13px;
            }
            QToolBar {
                background-color: #FFFFFF;
                border-bottom: 1px solid #E0E0E0;
                padding: 5px;
                spacing: 3px;
            }
            QToolButton {
                background-color: #FFFFFF;
                color: #000000;
                border: 1px solid #D0D0D0;
                border-radius: 5px;
                padding: 6px 10px;
                min-width: 35px;
                min-height: 35px;
            }
            QToolButton:hover {
                background-color: #E8F4FF;
                border: 1px solid #4A90E2;
            }
            QToolButton:pressed {
                background-color: #4A90E2;
                color: #FFFFFF;
            }
            QLineEdit {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #D0D0D0;
                border-radius: 6px;
                padding: 8px 12px;
                selection-background-color: #4A90E2;
            }
            QLineEdit:focus {
                border: 2px solid #4A90E2;
                background-color: #F8FBFF;
            }
            QTabWidget::pane {
                border: 1px solid #D0D0D0;
                background-color: #FFFFFF;
            }
            QTabBar::tab {
                background-color: #E8E8E8;
                color: #000000;
                border: 1px solid #D0D0D0;
                padding: 8px 15px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #4A90E2;
                color: #FFFFFF;
                border-bottom: 2px solid #4A90E2;
            }
            QTabBar::tab:hover {
                background-color: #D0D0D0;
            }
            QPushButton {
                background-color: #FFFFFF;
                color: #000000;
                border: 1px solid #D0D0D0;
                border-radius: 4px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #E8F4FF;
                border: 1px solid #4A90E2;
            }
            QPushButton:pressed {
                background-color: #4A90E2;
                color: #FFFFFF;
            }
            QDialog {
                background-color: #F5F5F5;
                color: #000000;
            }
            QLabel {
                color: #000000;
                background-color: transparent;
            }
            QRadioButton {
                color: #000000;
                background-color: transparent;
            }
        """
        
        self.setStyleSheet(light_style)


if __name__ == '__main__':
    # Enable high DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    browser = BenedictBrowser()
    browser.show()
    sys.exit(app.exec_())
