@echo off
REM Criação da estrutura de diretórios para o projeto "projeto_vendas"

mkdir projeto_vendas
cd projeto_vendas

mkdir data
echo. > data\vendas.csv

mkdir src
echo. > src\analise_vendas.py

mkdir notebooks
echo. > notebooks\exploracao.ipynb

echo # Projeto Vendas > README.md

echo Estrutura criada com sucesso!
pause
