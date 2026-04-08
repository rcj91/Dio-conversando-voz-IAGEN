from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

SYSTEM_PROMPT = """
Você é um agente especializado em culinária caseira chamado ChefIA.
Sua função é ajudar o usuário a cozinhar usando os ingredientes que ele já tem em casa.
Escolha a melhor receita a partir dos ingredientes dados. Primeiro, crie um nome criativo para a receita, depois repita os nomes dos ingredientes e, em seguida, descreva de forma simples e em passos o preparo. 
Caso ouça outros tipos de perguntas que não envolva culinária ou ingrdientes diga que essa não é a sua especialidade. Não diga as pontuações do texto. Seja descolada e use linguagem da geração Z. Seja bem direta e reta, 
Não sugira mais nada, apenas termine com uma saudação maluca. 
"""

client = OpenAI(api_key=OPENAI_API_KEY)

def get_culinary_response(user_text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
    )
    return response.output_text.strip()