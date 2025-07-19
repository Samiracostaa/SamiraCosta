#!/usr/bin/env python3
"""
Servidor Web Local - Python
Serve arquivos estáticos do diretório atual
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Configurações do servidor
PORT = 8080
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado para o servidor HTTP"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        """Log personalizado com emojis"""
        client_ip = self.client_address[0]
        method = self.command
        path = self.path
        status = args[1] if len(args) > 1 else "200"
        
        # Emojis baseados no status
        if status.startswith("2"):
            emoji = "✅"
        elif status.startswith("4"):
            emoji = "❌"
        else:
            emoji = "⚠️"
        
        print(f"{emoji} {method} {path} - {client_ip} ({status})")
    
    def end_headers(self):
        """Adiciona headers CORS"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    """Função principal"""
    # Verifica se o diretório existe
    if not os.path.exists(DIRECTORY):
        print(f"❌ Erro: Diretório '{DIRECTORY}' não encontrado!")
        sys.exit(1)
    
    # Muda para o diretório especificado
    os.chdir(DIRECTORY)
    
    # Obtém o caminho absoluto
    abs_path = os.path.abspath(DIRECTORY)
    
    print("=" * 50)
    print("    🚀 Servidor Web Local - Python")
    print("=" * 50)
    print()
    print(f"📁 Servindo arquivos do diretório: {abs_path}")
    print(f"🌐 URL: http://localhost:{PORT}")
    print(f"⏹️  Para parar o servidor, pressione Ctrl+C")
    print()
    
    try:
        # Cria o servidor
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 Servidor iniciado na porta {PORT}")
            print("📡 Aguardando conexões...")
            print()
            
            # Inicia o servidor
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n⏹️  Servidor parado pelo usuário")
    except OSError as e:
        if e.errno == 48:  # Porta já em uso
            print(f"❌ Erro: Porta {PORT} já está em uso!")
            print("💡 Tente usar uma porta diferente ou pare outros serviços")
        else:
            print(f"❌ Erro ao iniciar o servidor: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main() 