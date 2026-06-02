import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.funcoes import aliquota_ir_por_duracao
for meses in [1,6,7,12,13,24,25,36]:
    print(meses, aliquota_ir_por_duracao(meses))
