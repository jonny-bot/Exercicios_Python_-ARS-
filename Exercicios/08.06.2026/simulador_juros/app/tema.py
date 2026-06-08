from PyQt5.QtGui import QPalette, QColor

def aplicar_tema(widget, dark_mode=False):
    palette = QPalette()
    if dark_mode:
        # Paleta escura
        palette.setColor(QPalette.Window, QColor("#1F2937"))
        palette.setColor(QPalette.WindowText, QColor("#F9FAFB"))
        palette.setColor(QPalette.Base, QColor("#374151"))   # fundo de campos/tabelas
        palette.setColor(QPalette.Text, QColor("#F9FAFB"))   # texto de campos/tabelas
        palette.setColor(QPalette.Button, QColor("#2563EB"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        widget.setPalette(palette)

        # Estilos adicionais
        widget.setStyleSheet("""
            QWidget { background-color: #1F2937; color: #F9FAFB; }
            QLabel { color: #F9FAFB; }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #374151;
                color: #F9FAFB;
                border: 2px solid #9CA3AF;
                border-radius: 6px;
                padding: 6px;
            }
            QTableWidget {
                background-color: #374151;
                color: #F9FAFB;
                gridline-color: #9CA3AF;
                alternate-background-color: #2D3748;
            }
            QHeaderView::section {
                background-color: #111827;
                color: #F9FAFB;
                padding: 6px;
                border: 1px solid #374151;
            }
            QPushButton {
                background-color: #2563EB;
                color: #fff;
                border-radius: 6px;
                padding: 8px 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1E40AF; }
        """)
    else:
        # Paleta clara
        palette.setColor(QPalette.Window, QColor("#F3F4F6"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        palette.setColor(QPalette.Base, QColor("#FFFFFF"))
        palette.setColor(QPalette.Text, QColor("#111827"))
        palette.setColor(QPalette.Button, QColor("#2563EB"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        widget.setPalette(palette)

        # Estilos adicionais
        widget.setStyleSheet("""
            QWidget { background-color: #F3F4F6; color: #111827; }
            QLabel { color: #111827; }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #fff;
                color: #111827;
                border: 2px solid #9CA3AF;
                border-radius: 6px;
                padding: 6px;
            }
            QTableWidget {
                background-color: #fff;
                color: #111827;
                gridline-color: #9CA3AF;
                alternate-background-color: #F9FAFB;
            }
            QHeaderView::section {
                background-color: #F3F4F6;
                color: #111827;
                padding: 6px;
                border: 1px solid #E5E7EB;
            }
            QPushButton {
                background-color: #2563EB;
                color: #fff;
                border-radius: 6px;
                padding: 8px 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1E40AF; }
        """)
