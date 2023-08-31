import os
import openai
from user_ids import user_ids
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_api_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em markting bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ],
        stream=True
    )
    return completion.choices[0].messages.content.strip('\"')

users = []
for user_id in user_ids:
    user = {"id": user_id, "name": f"Nome do Usuário {user_id}", "news": []}
    news = generate_api_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
    users.append(user)