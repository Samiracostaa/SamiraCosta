# 🚀 Servidor Web Local - Python

Este é um servidor HTTP simples desenvolvido em Python para servir seu portfólio localmente.

## 📋 Pré-requisitos

- **Python 3.6 ou superior** instalado no seu sistema
- Verifique se o Python está instalado executando: `python --version`

## 🛠️ Como usar

### Método 1: Script Automático (Recomendado)

1. **Execute o script batch:**
   ```bash
   start-server.bat
   ```

2. **O script irá:**
   - Compilar automaticamente o servidor
   - Iniciar o servidor na porta 8080
   - Mostrar a URL de acesso

### Método 2: Comandos Manuais

1. **Execute o servidor diretamente:**
   ```bash
   python server.py
   ```

2. **Ou usando o módulo HTTP do Python:**
   ```bash
   python -m http.server 8080
   ```

## 🌐 Acesso

Após iniciar o servidor, acesse:
- **URL principal:** http://localhost:8080
- **Porta:** 8080 (configurável no código)

## 📁 Estrutura de Arquivos

O servidor serve todos os arquivos do diretório atual:
- `index.html` - Página principal do portfólio
- `styles.css` - Estilos CSS
- `script.js` - JavaScript
- `README.md` - Documentação

## ⚙️ Configurações

### Alterar a Porta

Para mudar a porta do servidor, edite a linha 13 no arquivo `server.py`:

```python
PORT = 8080  # Mude para a porta desejada
```

### Alterar o Diretório Raiz

Para servir arquivos de outro diretório, edite a linha 14:

```python
DIRECTORY = "."  # Mude para o caminho desejado
```

## 🔧 Funcionalidades

- ✅ Servir arquivos estáticos (HTML, CSS, JS, imagens)
- ✅ Suporte a múltiplos tipos MIME
- ✅ Logs detalhados das requisições
- ✅ Páginas de erro personalizadas
- ✅ Suporte a múltiplas conexões simultâneas
- ✅ Segurança básica (não permite acesso fora do diretório raiz)

## 📊 Logs do Servidor

O servidor mostra logs em tempo real:
- 📥 Requisições recebidas
- ✅ Arquivos servidos com sucesso
- ❌ Erros encontrados

## ⏹️ Parar o Servidor

Para parar o servidor:
- Pressione **Ctrl+C** no terminal
- Ou feche a janela do terminal

## 🐛 Solução de Problemas

### Erro: "python não é reconhecido"
- **Solução:** Instale o Python e configure a variável PATH

### Erro: "Porta já em uso"
- **Solução:** Mude a porta no código ou pare outros serviços na porta 8080

### Erro: "Arquivo não encontrado"
- **Solução:** Verifique se o arquivo `index.html` existe no diretório

### Erro: "Permission denied"
- **Solução:** Execute o comando como administrador ou mude a porta

## 📝 Exemplo de Uso

```bash
# 1. Navegue até o diretório do projeto
cd /caminho/para/seu/portfolio

# 2. Execute o servidor
start-server.bat

# 3. Abra o navegador e acesse
# http://localhost:8080
```

## 🎯 Próximos Passos

- [ ] Adicionar suporte a HTTPS
- [ ] Implementar cache de arquivos
- [ ] Adicionar compressão gzip
- [ ] Criar interface web para gerenciamento
- [ ] Adicionar suporte a variáveis de ambiente

---

**Desenvolvido com ❤️ para servir seu portfólio localmente!** 