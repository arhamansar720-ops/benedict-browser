import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                             QLineEdit, QAction, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Browser')
        self.setGeometry(100, 100, 1200, 800)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Create toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Back button
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.navigate_back)
        toolbar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.navigate_forward)
        toolbar.addAction(forward_btn)
        
        # Reload button
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.reload_page)
        toolbar.addAction(reload_btn)
        
        # Home button
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        # Browser view
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)
        
        # Set Google as homepage
        self.home_url = 'https://www.google.com'
        self.browser.setUrl(QUrl(self.home_url))
        
        # Update URL bar when page changes
        self.browser.urlChanged.connect(self.update_url_bar)
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        
        # If it's not a URL, treat it as a Google search
        if not url.startswith('http://') and not url.startswith('https://'):
            if '.' not in url or ' ' in url:
                # It's a search query
                url = f'https://www.google.com/search?q={url.replace(" ", "+")}'
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())
