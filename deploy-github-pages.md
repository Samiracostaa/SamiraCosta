# 🚀 Deploy no GitHub Pages

## Passo a Passo Completo

### 1. Criar Repositório no GitHub

1. **Acesse:** https://github.com
2. **Clique em:** "New repository" (botão verde)
3. **Configure:**
   - **Repository name:** `portfolio-samira` (ou o nome que preferir)
   - **Description:** "Meu portfólio pessoal - Desenvolvedora Fullstack"
   - **Visibility:** Public
   - **NÃO marque** "Add a README file"
4. **Clique em:** "Create repository"

### 2. Subir os Arquivos

```bash
# No terminal, no diretório do seu portfólio
git init
git add .
git commit -m "Primeiro commit - Portfólio"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/portfolio-samira.git
git push -u origin main
```

### 3. Configurar GitHub Pages

1. **No repositório:** Settings → Pages
2. **Source:** Deploy from a branch
3. **Branch:** main
4. **Folder:** / (root)
5. **Save**

### 4. URL Final
- **Sua URL será:** `https://SEU_USUARIO.github.io/portfolio-samira`
- **Exemplo:** `https://samiracostaa.github.io/portfolio-samira`

---

## ⚡ Deploy Automático

Crie um arquivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./
```

---

## 🔗 Links para Compartilhar

- **LinkedIn:** Adicione a URL no seu perfil
- **Email:** Inclua no seu email de assinatura
- **CV:** Adicione na seção de projetos
- **WhatsApp:** Compartilhe diretamente

---

## ✨ Vantagens do GitHub Pages

- ✅ **Gratuito**
- ✅ **HTTPS automático**
- ✅ **Custom domain** (opcional)
- ✅ **Integração com GitHub**
- ✅ **Deploy automático**
- ✅ **Profissional e confiável** 