import sys
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                             QLineEdit, QAction, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont

class BenedictBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Benedict Browser')
        self.setGeometry(100, 100, 1400, 900)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        main_widget.setLayout(layout)
        
        # Create toolbar with larger elements
        toolbar = self.create_toolbar()
        self.addToolBar(toolbar)
        
        # Browser view
        self.browser = QWebEngineView()
        self.browser.setZoomFactor(0.9)  # Slightly reduce page zoom (90%)
        layout.addWidget(self.browser)
        
        # Set DuckDuckGo as homepage
        self.home_url = 'https://duckduckgo.com'
        self.browser.setUrl(QUrl(self.home_url))
        
        # Update URL bar when page changes
        self.browser.urlChanged.connect(self.update_url_bar)
        
    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(18, 18))  # Smaller icons
        toolbar.setStyleSheet("""
            QToolBar {
                background-color: #1E1E1E;
                border: none;
                padding: 5px;
                spacing: 5px;
            }
            QToolButton {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #3D3D3D;
                border-radius: 4px;
                padding: 6px 8px;
                font-size: 14px;
                font-weight: bold;
                min-width: 30px;
                min-height: 30px;
            }
            QToolButton:hover {
                background-color: #3D3D3D;
                border: 1px solid #4A90E2;
            }
            QToolButton:pressed {
                background-color: #4A90E2;
            }
        """)
        
        # Back button
        back_btn = QAction('←', self)
        back_btn.setFont(QFont("Arial", 14, QFont.Bold))
        back_btn.triggered.connect(self.navigate_back)
        toolbar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction('→', self)
        forward_btn.setFont(QFont("Arial", 14, QFont.Bold))
        forward_btn.triggered.connect(self.navigate_forward)
        toolbar.addAction(forward_btn)
        
        # Reload button
        reload_btn = QAction('⟳', self)
        reload_btn.setFont(QFont("Arial", 14, QFont.Bold))
        reload_btn.triggered.connect(self.reload_page)
        toolbar.addAction(reload_btn)
        
        # Home button
        home_btn = QAction('⌂', self)
        home_btn.setFont(QFont("Arial", 14, QFont.Bold))
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search DuckDuckGo or enter URL...")
        self.url_bar.setFont(QFont("Arial", 12))
        self.url_bar.setMinimumHeight(32)
        self.url_bar.setStyleSheet("""
            QLineEdit {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 2px solid #3D3D3D;
                border-radius: 5px;
                padding: 6px 10px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #4A90E2;
                background-color: #353535;
            }
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        # DuckDuckGo AI button
        ddg_ai_btn = QAction('🦆 AI', self)
        ddg_ai_btn.setFont(QFont("Arial", 12, QFont.Bold))
        ddg_ai_btn.triggered.connect(self.open_duckduckgo_ai)
        toolbar.addAction(ddg_ai_btn)
        
        return toolbar
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        
        # If it's not a URL, treat it as a DuckDuckGo search
        if not url.startswith('http://') and not url.startswith('https://'):
            if '.' not in url or ' ' in url:
                # It's a search query
                url = f'https://duckduckgo.com/?q={url.replace(" ", "+")}'
            else:
                # It's probably a domain
                url = 'https://' + url
        
        self.browser.setUrl(QUrl(url))
    
    def navigate_back(self):
        self.browser.back()
    
    def navigate_forward(self):
        self.browser.forward()
    
    def reload_page(self):
        self.browser.reload()
    
    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))
    
    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())
    
    def open_duckduckgo_ai(self):
        """Open DuckDuckGo AI Chat (FREE!)"""
        self.browser.setUrl(QUrl('https://duckduckgo.com/chat'))


if __name__ == '__main__':
    # Enable high DPI scaling BEFORE creating QApplication
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    # Set application-wide dark theme with larger, more visible elements
    app.setStyleSheet("""
        QMainWindow {
            background-color: #0A0A0A;
        }
        QWidget {
            font-size: 14px;
        }
    """)
    
    browser = BenedictBrowser()
    browser.show()
    sys.exit(app.exec_())
