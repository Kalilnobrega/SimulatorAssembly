🖥️ Projeto — Simulador Assembly (x86 Modo Real)
Simulador interativo desenvolvido para auxiliar estudantes a entender, visualizar e executar instruções Assembly (arquitetura x86 em modo real).
 O projeto permite acompanhar registradores, memória e fluxo de execução de forma didática e clara.

👥 Responsáveis pelo Projeto
Vitor Vitoriano —  GitHub • LinkedIn


Paulo Adrian —  GitHub • LinkedIn


Kalil Nóbrega —  GitHub • LinkedIn









📘 Instruções do Projeto
1️⃣ Ambiente de Desenvolvimento
Utilize Visual Studio Code ou um editor de código equivalente.


Certifique-se de que o Node.js e o npm estejam instalados na sua máquina.

⚙️ 2️⃣ Configuração do Projeto
🔹 Clone o repositório
git clone https://github.com/Vitor-Vitoriano/SimulatorAssembly
cd SimulatorAssembly


🔹 Instale as dependências do projeto
npm install

Isso instalará:
Vite


TailwindCSS


PostCSS


Autoprefixer


Demais dependências descritas no package.json
🎨 3️⃣ Configuração do TailwindCSS
Caso precise reinstalar ou configurar novamente, use:
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

✔️ Atualize o arquivo tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


✔️ Inclua o Tailwind no seu CSS principal (ex.: src/style.css)
@tailwind base;
@tailwind components;
@tailwind utilities;


🚀 4️⃣ Executando o projeto
Use o comando abaixo para iniciar o ambiente de desenvolvimento:
npm run dev

Abra a URL gerada no terminal para acessar o simulador no navegador.
🔧 Funcionalidades do Simulador
Execução passo a passo de instruções Assembly


Visualização de registradores


Exibição da memória


Interface estilizada com TailwindCSS


Entrada e edição interativa de código Assembly


Painel de execução e depuração
