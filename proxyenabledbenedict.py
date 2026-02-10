"""
Benedict Browser - Simple Bypass Edition
For CS Project: Manual proxy setup to bypass restrictions
"""

import sys
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                             QLineEdit, QAction, QVBoxLayout, QWidget,
                             QMessageBox, QLabel, QComboBox, QInputDialog)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont
from PyQt5.QtNetwork import QNetworkProxy

class BenedictBrowserSimple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Benedict Browser - Bypass Edition')
        self.setGeometry(100, 100, 1400, 900)
        
        self.proxy_enabled = False
        
        # Free proxy list (pre-loaded)
        self.free_proxies = [
            {'ip': '51.159.115.233', 'port': 3128},
            {'ip': '103.152.112.162', 'port': 80},
            {'ip': '20.206.106.192', 'port': 80},
            {'ip': '47.88.62.42', 'port': 80},
            {'ip': '8.219.97.248', 'port': 80},
        ]
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        main_widget.setLayout(layout)
        
        # Create toolbar
        toolbar = self.create_toolbar()
        self.addToolBar(toolbar)
        
        # Browser view
        self.browser = QWebEngineView()
        self.browser.setZoomFactor(0.9)
        layout.addWidget(self.browser)
        
        # Set DuckDuckGo as homepage
        self.home_url = 'https://duckduckgo.com'
        self.browser.setUrl(QUrl(self.home_url))
        
        # Update URL bar when page changes
        self.browser.urlChanged.connect(self.update_url_bar)
    
    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(18, 18))
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
            QComboBox {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #3D3D3D;
                border-radius: 4px;
                padding: 5px;
                min-width: 150px;
                font-size: 12px;
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
        
        # Bypass toggle button
        bypass_btn = QAction('Enable Bypass', self)
        bypass_btn.setFont(QFont("Arial", 12, QFont.Bold))
        bypass_btn.triggered.connect(self.toggle_bypass)
        toolbar.addAction(bypass_btn)
        self.bypass_btn = bypass_btn
        
        # Status label
        self.status_label = QLabel("Direct")
        self.status_label.setStyleSheet("color: #4CAF50; padding: 5px; font-size: 11px;")
        toolbar.addWidget(self.status_label)
        
        return toolbar
    
    def toggle_bypass(self):
        """Toggle bypass mode on/off"""
        if not self.proxy_enabled:
            # Enable bypass
            try:
                # Use first proxy from list
                proxy = self.free_proxies[0]
                self.enable_proxy(proxy['ip'], proxy['port'])
                
                self.bypass_btn.setText('Disable Bypass')
                self.status_label.setText(f"Proxy: {proxy['ip']}")
                self.status_label.setStyleSheet("color: #FF9800; padding: 5px; font-size: 11px;")
                
                QMessageBox.information(
                    self,
                    'Bypass Enabled',
                    f'Now routing through proxy:\n{proxy["ip"]}:{proxy["port"]}\n\nNetwork restrictions bypassed!'
                )
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to enable bypass:\n{str(e)}')
        else:
            # Disable bypass
            self.disable_proxy()
            self.bypass_btn.setText('Enable Bypass')
            self.status_label.setText("Direct")
            self.status_label.setStyleSheet("color: #4CAF50; padding: 5px; font-size: 11px;")
    
    def enable_proxy(self, host, port):
        """Enable proxy connection"""
        proxy = QNetworkProxy()
        proxy.setType(QNetworkProxy.HttpProxy)
        proxy.setHostName(host)
        proxy.setPort(port)
        
        QNetworkProxy.setApplicationProxy(proxy)
        self.proxy_enabled = True
        print(f"[BYPASS ENABLED] {host}:{port}")
    
    def disable_proxy(self):
        """Disable proxy"""
        QNetworkProxy.setApplicationProxy(QNetworkProxy.NoProxy)
        self.proxy_enabled = False
        print("[DIRECT CONNECTION] Bypass disabled")
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        
        if not url.startswith('http://') and not url.startswith('https://'):
            if '.' not in url or ' ' in url:
                url = f'https://duckduckgo.com/?q={url.replace(" ", "+")}'
            else:
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
    # Enable high DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    # Dark theme
    app.setStyleSheet("""
        QMainWindow {
            background-color: #0A0A0A;
        }
        QWidget {
            font-size: 14px;
        }
    """)
    
    browser = BenedictBrowserSimple()
    browser.show()
    sys.exit(app.exec_())
