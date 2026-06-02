import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication, QTableWidget, QFileDialog, QTableWidgetItem
from core import funcoes
from types import SimpleNamespace

os.environ['QT_QPA_PLATFORM'] = 'offscreen'

app = QApplication([])

QFileDialog.getSaveFileName = lambda *args, **kwargs: (
    os.path.join(os.getenv('TEMP', '.'), 'dummy_export.csv'),
    'CSV (*.csv)'
)

saved = []
funcoes._save_csv = lambda filename, headers, rows: saved.append((filename, headers, rows))

obj = SimpleNamespace()
obj.window = lambda: None
obj.tabela = QTableWidget()
obj.tabela.setColumnCount(2)
obj.tabela.setHorizontalHeaderLabels(['A', 'B'])
obj.tabela.insertRow(0)
obj.tabela.setItem(0, 0, QTableWidgetItem('x'))
obj.tabela.setItem(0, 1, QTableWidgetItem('y'))

funcoes.exportar_dados(obj)
print('export_test_ok', saved)
