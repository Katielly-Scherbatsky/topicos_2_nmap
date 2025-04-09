# 🔍 Scanner de Portas TCP/UDP

Ferramenta em Python para escaneamento de portas TCP ou UDP em um endereço IP. Permite exportação dos resultados e suporta multithreading para maior desempenho.

---

## 🚀 Instalação

Clone o repositório e execute o script de instalação:

```bash
git clone https://github.com/seuusuario/scanner-portas.git
cd scanner-portas
bash install.sh
```

## 🧪 Uso

Execute o scanner com o seguinte comando:

```bash
python3 scanner.py <IP> -p <PROTOCOLO> -s <PORTA_INICIAL> -e <PORTA_FINAL> -x <ARQUIVO_SAÍDA>
```

### Parâmetros

- `-p` : Protocolo a ser usado (tcp ou udp)
- `-s` : Porta inicial para o escaneamento
- `-e` : Porta final para o escaneamento
- `-x` : Exporta os resultados para um arquivo (.csv ou .txt)

### 📌 Exemplos de uso

```bash
python3 scanner.py 127.0.0.1 -p tcp -s 1 -e 1024 -x resultados.csv
```

```bash
python3 scanner.py 192.168.0.100 -p udp -s 20 -e 100 -x relatorio.txt
```

## 📄 Exportação

Os resultados podem ser exportados para .csv ou .txt. O conteúdo incluirá as colunas:

- Porta
- Status (Aberta, Fechada, Filtrada)

## ⚙️ Script install.sh (para Linux)

Script para instalação das dependências:

```bash
#!/bin/bash

echo "Instalando dependências..."
sudo apt update
sudo apt install -y python3 python3-pip

echo "Verificando requisitos Python..."
pip3 install -r requirements.txt 2>/dev/null || echo "Sem dependências extras."

echo "✅ Pronto. Execute com: python3 scanner.py"
```

## 🖥️ Compatibilidade

- ✅ Linux (recomendado)
- ⚠️ Suporte opcional para Windows e macOS

## 📌 Requisitos

- Python 3.x

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.

## 📝 Licença

Este projeto está licenciado sob a MIT License.

## 📌 Observações

- O escaneamento UDP pode ser mais demorado e impreciso devido à natureza do protocolo.
- É necessário permissão de administrador/root para escanear certas portas.

Feito com 💻 por Katielly Bordin Santos
