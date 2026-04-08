import os
from datetime import datetime


def _build_content(user_text: str, agent_text: str) -> str:
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    content = f"""
==================================================
                CHEFIA - INTERAÇÃO
==================================================

DATA/HORA:
{timestamp}

--------------------------------------------------
PERGUNTA DO USUÁRIO
--------------------------------------------------
{user_text}

--------------------------------------------------
RESPOSTA DO AGENTE
--------------------------------------------------
{agent_text}

==================================================
FIM DO REGISTRO
==================================================
"""
    return content.strip()


def save_last_interaction_txt(
    user_text: str,
    agent_text: str,
    file_path: str = "data/output/interacao_chefia.txt"
) -> str:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    content = _build_content(user_text, agent_text)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return os.path.abspath(file_path)


def append_history_txt(
    user_text: str,
    agent_text: str,
    file_path: str = "data/output/historico_chefia.txt"
) -> str:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    content = _build_content(user_text, agent_text)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content + "\n\n")

    return os.path.abspath(file_path)