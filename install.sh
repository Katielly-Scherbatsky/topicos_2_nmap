#!/bin/bash

echo "📦 Instalando dependências..."
sudo apt update
sudo apt install -y python3 python3-pip

echo "🐍 Instalando bibliotecas Python (caso necessário)..."
pip3 install -r requirements.txt 2>/dev/null || echo "Sem dependências extras."

echo "✅ Instalação concluída. Execute com: python3 scanner.py"
