📌 README – AutoAssistBot
📖 Descrição

AutoAssistBot é um chatbot para Telegram desenvolvido em Python, voltado ao atendimento automatizado, cadastro de usuários e solicitação de orçamentos. O projeto utiliza a biblioteca pyTelegramBotAPI (telebot) e persistência simples em arquivos .txt, sendo ideal como base para bots comerciais e MVPs.

⚙️ Funcionalidades:
- Menu interativo com botões Inline e Reply

- Cadastro de usuários (nome, telefone, chat_id)

- Solicitação de orçamento por texto

- Suporte a Telegram Mobile e Web

- Persistência de dados em arquivos locais

- Fluxos controlados por estado do usuário

🗂️ Estrutura do Projeto
AutoAssistBot/
│
├── main.py               # Inicialização do bot
├── config.py             # Token da API do Telegram
├── user_menu.py          # Menus e botões
├── user_messages.py      # Handlers e fluxos
├── user_services.py      # Persistência de dados
│
├── data/
│   ├── cadastros.txt
│   └── orcamentos.txt
│
└── README.md

▶️ Como Executar

1. Crie um bot no @BotFather

2. Insira o token em config.py

3. Instale as dependências:
-> pip install pyTelegramBotAPI

4. Execute:
-> python main.py

🧠 Observações Técnicas

ReplyKeyboardMarkup funciona apenas em dispositivos móveis

Telegram Web exige fallback para entrada manual

Controle de estado feito com set() (adequado para MVPs)

Para produção, recomenda-se:

Banco de dados (SQLite/PostgreSQL)

Framework assíncrono

Essas soluções serão implementadas futuramente em um novo arquivo.