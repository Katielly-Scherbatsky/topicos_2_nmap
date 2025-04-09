import socket
import threading
import time
import csv
import os
import argparse

# Função para verificar portas TCP
def scan_tcp(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append((port, "Aberta"))
        else:
            results.append((port, "Fechada"))
    except socket.error:
        results.append((port, "Filtrada"))
    finally:
        sock.close()

# Função para verificar portas UDP
def scan_udp(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b'', (ip, port))
        sock.recvfrom(1024)
        results.append((port, "Aberta"))
    except socket.timeout:
        results.append((port, "Filtrada"))
    except socket.error:
        results.append((port, "Fechada"))
    finally:
        sock.close()

# Varredura com threads
def scan_ports(ip, start_port, end_port, protocol):
    results = []
    threads = []

    for port in range(start_port, end_port + 1):
        if protocol == 'tcp':
            thread = threading.Thread(target=scan_tcp, args=(ip, port, results))
        elif protocol == 'udp':
            thread = threading.Thread(target=scan_udp, args=(ip, port, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted(results)

# Exporta para arquivo
def export_results(results, filename):
    ext = os.path.splitext(filename)[1].lower()

    with open(filename, 'w', newline='') as file:
        if ext == '.csv':
            writer = csv.writer(file)
            writer.writerow(['Porta', 'Status'])
            writer.writerows(results)
        elif ext == '.txt':
            for port, status in results:
                file.write(f'Porta {port}: {status}\n')
        else:
            print("Formato não suportado. Use .csv ou .txt")
            return

    print(f"✔️ Resultados exportados para: {filename}")

# Ponto principal
def main():
    parser = argparse.ArgumentParser(description="Scanner de portas TCP/UDP")
    parser.add_argument("ip", help="Endereço IP a ser escaneado")
    parser.add_argument("-p", "--protocolo", choices=["tcp", "udp"], required=True, help="Protocolo a ser usado")
    parser.add_argument("-s", "--start", type=int, default=1, help="Porta inicial (padrão: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Porta final (padrão: 1024)")
    parser.add_argument("-x", "--export", help="Nome do arquivo para exportar os resultados (.csv ou .txt)")

    args = parser.parse_args()

    print(f"🔎 Iniciando escaneamento {args.protocolo.upper()} em {args.ip} de {args.start} a {args.end}...")

    start_time = time.time()
    results = scan_ports(args.ip, args.start, args.end, args.protocolo)
    duration = time.time() - start_time

    print(f"\n✅ Varredura concluída em {duration:.2f} segundos.")
    for port, status in results:
        print(f"Porta {port}: {status}")

    if args.export:
        export_results(results, args.export)

if __name__ == "__main__":
    main()
