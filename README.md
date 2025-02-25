# 📄 DocumentGPT

O **DocumentGPT** é uma aplicação em Python que utiliza inteligência artificial para análise automatizada de documentos PDF. O projeto usa a biblioteca **LangChain** para leitura, indexação e pesquisa de documentos, com suporte para interações em linguagem natural e envio de mensagens via WhatsApp usando a **Twilio API**.

## 🚀 Funcionalidades

- 📚 Extração automática de texto de documentos PDF.
- 🔍 Indexação de conteúdo para buscas por similaridade.
- 💬 Interação com modelo de linguagem da OpenAI (GPT) para consultas inteligentes.
- 🔔 Envio de notificações via WhatsApp usando a Twilio API.
- 📊 Geração de relatórios automatizados com base no conteúdo extraído.

---

## 🛠️ Tecnologias Usadas

- **Python 3.10+**
- [LangChain](https://langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Twilio API](https://www.twilio.com/)
- [ChromaDB](https://www.trychroma.com/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior (evitar versões superiores à 3.11 por questões de compatibilidade)
- Conta no [Twilio](https://www.twilio.com/)
- Chave de API da OpenAI
- Ambiente virtual configurado (recomendado)

---

## 💻 Como rodar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/DocumentGPT.git
cd DocumentGPT
```

### 2️⃣ Crie e ative o ambiente virtual
Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto e adicione suas credenciais:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

### 5️⃣ Adicione seus arquivos PDF
Coloque os arquivos PDF que deseja processar na pasta:
```bash
data/input/
```

### 6️⃣ Rode o projeto
```bash
python run.py
```

### 📂 Estrutura do Projeto
```graphql
DocumentGPT/
│
├── config/                        # Configurações gerais
├── data/                          # Dados do projeto
│   ├── db/                        # Banco de dados vetorial (ChromaDB)
│   ├── input/                     # PDFs a serem processados
│   │   ├── _Sample_.pdf           # Exemplo de documento PDF
│   │   └── sample.pdf             # Outro exemplo
│   ├── output/                    # Textos extraídos dos PDFs
│
├── document_gpt/                  # Código principal
│   ├── helper/                    # Funções auxiliares
│   │   ├── conversation.py        # Sistema de interação com IA
│   │   ├── create_index.py        # Indexação de documentos
│   │   └── twilio_api.py          # Envio de mensagens via Twilio
│   └── src/                       # Código principal da aplicação
│       ├── main.py                # Ponto de entrada
│       └── __init__.py            # Inicializador do módulo
│
├── venv/                          # Ambiente virtual (não versionado)
│
├── .gitignore                     # Arquivos e pastas ignorados pelo Git
├── .env                           # Variáveis de ambiente (não versionado)
├── call_create_index.py           # Script para indexação manual
├── run.py                         # Executa a aplicação principal
├── requirements.txt               # Lista de dependências
├── runtime.txt                    # Versão do Python
└── README.md                      # Documentação do projeto
```

### 🤖 Como usar a IA para interagir com os documentos
Após executar o comando:
```bash
python run.py
```

Digite suas perguntas diretamente no terminal. Por exemplo:
```bash
Você: Quais são os tópicos abordados no sample.pdf?
IA: O documento aborda os seguintes tópicos...
```

Para encerrar a interação, digite:
```bash
sair
```

### 🔔 Envio de mensagens pelo WhatsApp com Twilio
No código, você pode enviar mensagens usando a função send_message:
```bash
from document_gpt.helper.twilio_api import send_message

# Exemplo de envio de mensagem
send_message("whatsapp:+5599999999999", "Olá! Esta é uma mensagem enviada automaticamente pelo DocumentGPT.")
```

### 🧪 Testes
Para rodar testes básicos:
```bash
python -m unittest discover
```

### 🔧 Configurações Específicas
 Banco de dados vetorial: O ChromaDB salva os embeddings no diretório data/db/.
 Logs: Habilite o modo verbose no conversation.py para mais informações durante a execução.

### 🤝 Contribuições
1. Faça um fork do projeto.
2. Crie uma branch: git checkout -b feature/nova-funcionalidade
3. Faça o commit: git commit -m 'Adicionando nova funcionalidade'
4. Faça o push: git push origin feature/nova-funcionalidade
5. Abra um Pull Request.

### 📬 Contato
WFI Tech - William
📧 Email: william.sousa@wfitech.com.br
🌐 Site: wfitech.com.br