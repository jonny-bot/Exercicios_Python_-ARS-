import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication
from app.telas.ui_juros_simples import JurosSimples

app = QApplication(sys.argv)
w = JurosSimples()
w.capital.setText('1000')
w.taxa.setText('1.05')
w.tempo.setText('240')
w.tipo_tempo.setCurrentText('Meses')
w.tipo_taxa.setCurrentText('Mensal')
try:
    w.calcular()
    print('OK', w.total_juros.text(), w.total_final.text(), w.tabela.rowCount())
except Exception as e:
    import traceback
    traceback.print_exc()
