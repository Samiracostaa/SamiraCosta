# 🌐 GitHub Pages - Guia Visual Completo

## 📋 Pré-requisitos
- ✅ Conta no GitHub
- ✅ Git instalado no computador

---

## 🚀 Passo 1: Criar Repositório

### 1.1 Acesse o GitHub
- Vá para: **https://github.com**
- Faça login na sua conta

### 1.2 Criar Novo Repositório
- Clique no botão **"New"** (verde)
- Ou clique no **"+"** → **"New repository"**

### 1.3 Configurar Repositório
```
Repository name: portfolio-samira
Description: Meu portfólio pessoal - Desenvolvedora Fullstack
Visibility: Public ✅
Add a README file: ❌ (NÃO marque)
Add .gitignore: ❌ (NÃO marque)
Choose a license: ❌ (NÃO marque)
```

### 1.4 Criar
- Clique em **"Create repository"**

---

## 📁 Passo 2: Preparar Arquivos Localmente

### 2.1 Executar Script Automático
```bash
# No terminal, no diretório do seu portfólio
.\deploy-github.bat
```

### 2.2 Ou Comandos Manuais
```bash
git init
git add .
git commit -m "Primeiro commit - Portfólio"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/portfolio-samira.git
git push -u origin main
```

---

## ⚙️ Passo 3: Configurar GitHub Pages

### 3.1 Acessar Settings
- No seu repositório → **"Settings"** (aba)

### 3.2 Configurar Pages
- Role para baixo → **"Pages"** (menu lateral)
- **Source:** Deploy from a branch
- **Branch:** main
- **Folder:** / (root)
- Clique em **"Save"**

### 3.3 Aguardar Deploy
- Aguarde alguns minutos
- Status: "Your site is published at..."

---

## 🔗 Passo 4: URL Final

### Sua URL será:
```
https://SEU_USUARIO.github.io/portfolio-samira
```

### Exemplo:
```
https://samiracostaa.github.io/portfolio-samira
```

---

## 📱 Passo 5: Compartilhar

### LinkedIn
- Adicione a URL no seu perfil
- Seção: "Featured" ou "About"

### Email
- Inclua na assinatura do email
- Exemplo: "Veja meu portfólio: [URL]"

### WhatsApp
- Compartilhe diretamente
- "Olá! Aqui está meu portfólio: [URL]"

### CV
- Seção: "Projetos" ou "Links"

---

## 🎯 Próximos Passos

### Custom Domain (Opcional)
- Compre um domínio (ex: samira.dev)
- Configure no GitHub Pages
- URL: https://samira.dev

### SEO
- Adicione meta tags no HTML
- Otimize para Google

### Analytics
- Google Analytics
- GitHub Analytics

---

## ❓ Problemas Comuns

### Erro: "Repository not found"
- Verifique se o repositório é público
- Confirme o nome do usuário

### Erro: "Page not found"
- Aguarde alguns minutos
- Verifique se o GitHub Pages está ativo

### Erro: "Git not found"
- Instale o Git: https://git-scm.com/
- Reinicie o terminal

---

## 🎉 Sucesso!

Após seguir todos os passos, seu portfólio estará disponível em:
**https://SEU_USUARIO.github.io/portfolio-samira**

Agora você pode compartilhar essa URL com qualquer pessoa no mundo! 🌍 