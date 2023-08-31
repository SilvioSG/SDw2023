# Chatbot de Geração de Mensagens sobre Investimentos

Este projeto demonstra o uso da API do OpenAI para gerar mensagens sobre a importância dos investimentos em um contexto de marketing bancário. O chatbot utiliza o modelo GPT-3.5 Turbo da OpenAI para criar mensagens personalizadas para diferentes usuários.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado os seguintes requisitos:

- Python (versão X.X)
  - Biblioteca `openai`
  - Biblioteca `dotenv`

## Instalação

1. Clone este repositório em sua máquina local.

   2. Instale as dependências necessárias usando o seguinte comando:

```bash
pip install openai python-dotenv
```

## Configuração

Crie uma conta no OpenAI e obtenha sua chave de API.
Renomeie o arquivo .env.example para .env e insira sua chave de API do OpenAI no campo OPENAI_API_KEY.
Como Usar

Abra um terminal e navegue até o diretório do projeto.
Execute o script principal usando o seguinte comando:
bash
Copy code
python main.py
O script irá gerar mensagens personalizadas sobre a importância dos investimentos para diferentes usuários, utilizando o modelo GPT-3.5 Turbo da OpenAI.

## Personalização

Você pode ajustar o comportamento do chatbot alterando as mensagens, o modelo de linguagem ou outras configurações na função generate_api_news no arquivo main.py.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.


