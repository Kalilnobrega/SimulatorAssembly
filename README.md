# Projeto — Simulador Assembly (x86 Modo Real)

Simulador interativo desenvolvido para auxiliar estudantes a entender, visualizar e executar instruções Assembly (arquitetura x86 em modo real). O projeto permite acompanhar registradores, memória e fluxo de execução de forma didática e clara.

---

## 👥 Responsáveis pelo Projeto

* **Vitor Vitoriano** — [GitHub](https://github.com/Vitor-Vitoriano) • [LinkedIn](link-do-linkedin-do-vitor)
* **Paulo Adrian** — [GitHub](link-do-github-do-paulo) • [LinkedIn](link-do-linkedin-do-paulo)
* **Kalil Nóbrega** — [GitHub](link-do-github-do-kalil) • [LinkedIn](link-do-linkedin-do-kalil)

---

## 1. ⚙️ Instruções e Configuração

### 1.1. Ambiente de Desenvolvimento

Utilize **Visual Studio Code** ou um editor de código equivalente.

Certifique-se de que o **Node.js** e o **npm** estejam instalados em sua máquina.

### 1.2. Configuração do Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Vitor-Vitoriano/SimuladorAssembly](https://github.com/Vitor-Vitoriano/SimuladorAssembly)
    cd SimuladorAssembly
    ```

2.  **Instale as dependências do projeto:**
    ```bash
    npm install
    ```
    Isso instalará as seguintes dependências:
    * Vite
    * TailwindCSS
    * PostCSS
    * Autoprefixer

### 1.3. Configuração do TailwindCSS

Caso precise reinstalar ou configurar novamente as dependências do TailwindCSS (descritas no `package.json`), use o comando:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
