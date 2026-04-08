# 🍳 ChefIA Voz

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![Whisper](https://img.shields.io/badge/Whisper-Transcrição-orange)
![gTTS](https://img.shields.io/badge/gTTS-Texto%20para%20Voz-yellow)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-brightgreen)

Assistente de culinária por voz desenvolvido em Python, capaz de gravar a fala do usuário, transcrever o áudio, interpretar os ingredientes informados e gerar sugestões de receitas de forma estruturada, retornando a resposta em texto, em arquivo `.txt` e também em áudio.

---

## 📌 Sobre o projeto

O **ChefIA Voz** é um agente especializado em culinária caseira, criado com o objetivo de ajudar o usuário a descobrir receitas a partir dos ingredientes que possui em casa.

A proposta do projeto é unir **processamento de áudio**, **inteligência artificial generativa** e **organização modular de software** para construir uma solução prática, acessível e interativa.

O usuário fala no microfone quais ingredientes possui ou qual receita deseja, e o sistema:

1. grava a fala;  
2. transcreve o áudio em texto;  
3. envia a transcrição para um agente culinário especializado;  
4. recebe uma resposta organizada com a receita;  
5. salva a interação em arquivo `.txt`;  
6. converte a resposta em áudio para reprodução.  

---

## 🎯 Objetivo

O objetivo deste trabalho é demonstrar a aplicação prática de inteligência artificial em um problema cotidiano: **sugerir receitas de forma automática e por voz**, com base nos ingredientes disponíveis.

Além disso, o projeto também busca:

- aplicar conceitos de IA generativa;
- utilizar reconhecimento de fala e síntese de voz;
- estruturar um sistema em módulos reutilizáveis;
- desenvolver uma aplicação apresentável e executável via GitHub.

---

## ✅ Funcionalidades

- 🎙️ Gravação de áudio pelo microfone  
- 📝 Transcrição automática da fala com Whisper  
- 🤖 Interpretação do pedido com OpenAI  
- 🍲 Resposta especializada em culinária caseira  
- 📋 Geração de receita estruturada  
- 🔊 Conversão da resposta em áudio com gTTS  
- 📄 Exportação da última interação em arquivo `.txt`  
- 🗂️ Histórico acumulado das interações  

---

## 💡 Exemplo de uso

O usuário pode falar frases como:

- "Tenho ovo, queijo e tomate. O que posso fazer?"
- "Me dá uma receita com frango e batata"
- "Tenho arroz, cebola e cenoura. O que dá para preparar?"
- "Quero uma receita simples para o jantar"

A resposta do agente é organizada em:

1. **Nome da receita**  
2. **Ingredientes**  
3. **Modo de preparo**  
4. **Tempo estimado**  
5. **Dicas extras**  

---

## 🛠️ Tecnologias utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias e bibliotecas:

- **Python**
- **OpenAI API** — geração de respostas do agente
- **Whisper** — transcrição de áudio para texto
- **gTTS** — conversão de texto em fala
- **sounddevice** — gravação do áudio pelo microfone
- **scipy** — salvamento do arquivo de áudio `.wav`
- **python-dotenv** — leitura de variáveis de ambiente
- **VS Code** — ambiente de desenvolvimento

---

## 🧱 Estrutura do projeto

```bash
ass_voz_mult_idiom/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── audio/
│   │   ├── __init__.py
│   │   ├── recorder.py
│   │   ├── transcriber.py
│   │   └── tts.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── culinary_agent.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils/
│       ├── __init__.py
│       └── exporter.py
├── data/
│   ├── input/
│   └── output/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py

---
    
└── README.md

