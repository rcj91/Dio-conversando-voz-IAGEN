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


## 📂 Descrição dos módulos
app/main.py

Arquivo principal responsável por coordenar o fluxo completo da aplicação.

app/audio/recorder.py

Responsável pela gravação do áudio do usuário por meio do microfone.

app/audio/transcriber.py

Responsável pela transcrição do áudio utilizando o modelo Whisper.

app/audio/tts.py

Responsável por converter a resposta do agente em áudio utilizando gTTS.

app/agents/culinary_agent.py

Contém a lógica do agente especializado em culinária e a chamada à API da OpenAI.

app/config/settings.py

Responsável por carregar variáveis de ambiente, como chave da API, idioma e modelo.

app/utils/exporter.py

Responsável por salvar a última interação em um arquivo .txt e também manter um histórico acumulado das interações.

## ⚙️ Como o projeto funciona

O funcionamento do sistema ocorre em etapas bem definidas.

1. Gravação da fala

O sistema ativa o microfone e grava o áudio do usuário por alguns segundos, salvando o conteúdo em um arquivo .wav.

2. Transcrição

O áudio é processado pelo modelo Whisper, que converte a fala em texto.

3. Interpretação da solicitação

O texto transcrito é enviado para um agente culinário implementado com a OpenAI API.

4. Geração da resposta

O agente analisa o pedido e gera uma resposta estruturada com base no prompt interno configurado para culinária.

5. Exportação para texto

A interação é salva em dois arquivos:

um arquivo contendo apenas a última interação;
um arquivo com o histórico completo das interações.
6. Conversão para voz

A resposta do agente é convertida em áudio .mp3, permitindo que o usuário também escute a receita sugerida.

## 🧠 Prompt do agente

O sistema utiliza um prompt interno para especializar o comportamento do modelo em culinária caseira.

Esse prompt orienta o agente a:

responder em português do Brasil;
atuar como especialista em culinária;
sugerir receitas com base nos ingredientes disponíveis;
organizar a resposta em formato estruturado;
priorizar receitas simples, práticas e realistas;
oferecer dicas e possíveis substituições de ingredientes.

Essa abordagem permite transformar um modelo geral de linguagem em um agente especializado em um domínio específico.

## 🚀 Como instalar
1. Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd ass_voz_mult_idiom
2. Instalar as dependências
python -m pip install -r requirements.txt
🔐 Configuração do ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

OPENAI_API_KEY=sua_chave_aqui
WHISPER_MODEL=base
LANGUAGE=pt
Explicação das variáveis
OPENAI_API_KEY: chave de autenticação da API da OpenAI
WHISPER_MODEL: modelo Whisper utilizado na transcrição
LANGUAGE: idioma padrão utilizado no projeto
Arquivo .env.example
OPENAI_API_KEY=coloque_sua_chave_aqui
WHISPER_MODEL=base
LANGUAGE=pt
## 🔒 Importante sobre segurança

O arquivo .env contém informações sensíveis e não deve ser enviado ao GitHub.

Por isso, o .gitignore deve conter:

.env
__pycache__/
.ipynb_checkpoints/
*.pyc
data/input/
data/output/
▶️ Como executar

Na raiz do projeto, execute:

python run.py

Ao rodar, o sistema irá:

verificar as dependências;
gravar o áudio do usuário;
transcrever a fala;
gerar a resposta do agente;
salvar os arquivos de texto;
gerar o áudio da resposta.
👤 Guia do usuário
Passo a passo de uso
Execute o comando python run.py
Aguarde o sistema iniciar a gravação
Fale claramente os ingredientes que possui ou a receita desejada
Aguarde a transcrição e o processamento da resposta
Leia a resposta exibida no terminal
Consulte os arquivos .txt gerados
Ouça a resposta em áudio produzida pelo sistema
Exemplos de perguntas
"Tenho ovo, tomate e queijo"
"O que posso fazer com frango e batata?"
"Quero uma receita rápida para o jantar"
"Tenho arroz, cebola e cenoura"
## 📁 Arquivos gerados pelo sistema

Após a execução, o sistema gera arquivos na pasta data/output/:

interacao_chefia.txt → armazena apenas a última interação
historico_chefia.txt → armazena todas as interações acumuladas
response_audio.mp3 → armazena o áudio da resposta do agente
## 🧪 Exemplo de saída esperada
Entrada do usuário

"Tenho ovo, tomate e queijo. O que posso fazer?"

Saída do agente

Nome da receita: Omelete de tomate com queijo

Ingredientes:

2 ovos
1 tomate picado
queijo a gosto
sal
pimenta

Modo de preparo:

Bata os ovos com sal e pimenta.
Misture o tomate picado.
Despeje em uma frigideira aquecida.
Adicione o queijo.
Dobre a omelete e sirva.

Tempo estimado: 10 minutos

Dicas extras:

Pode adicionar orégano.
Sirva com pão ou salada.
## 📦 Dependências do projeto

Arquivo requirements.txt:

openai
openai-whisper
gTTS
sounddevice
scipy
python-dotenv
ipython
jupyter
## 🧩 Principais desafios enfrentados

Durante o desenvolvimento do projeto, alguns desafios técnicos foram encontrados:

adaptação do código originalmente usado em ambiente notebook para execução local;
instalação e configuração correta das bibliotecas de áudio;
organização modular do sistema em pastas e arquivos;
tratamento da autenticação com .env;
integração entre gravação, transcrição, IA generativa e síntese de voz;
geração de saídas organizadas em texto para facilitar acompanhamento da resposta.

Esses desafios ajudaram a transformar um protótipo inicial em um projeto mais estruturado e adequado para entrega acadêmica.

## 🔮 Melhorias futuras

Como possíveis evoluções do projeto, podem ser implementadas:

interface gráfica com Streamlit ou Gradio;
suporte a receitas por categoria;
restrições alimentares, como receitas vegetarianas ou sem lactose;
geração de múltiplas opções de receita por interação;
interação contínua em formato de conversa;
armazenamento do histórico em banco de dados;
personalização por perfil de usuário.
## 📚 Aprendizados obtidos

Este projeto permitiu aplicar conhecimentos em:

processamento de áudio;
transcrição automática de fala;
uso de modelos generativos;
engenharia de prompts;
modularização e organização de código;
boas práticas de segurança com variáveis de ambiente;
desenvolvimento de aplicações práticas com IA.

Além do aspecto técnico, o projeto também demonstra como a inteligência artificial pode ser utilizada para resolver problemas simples do cotidiano de forma acessível e interativa.

🏁 Conclusão

O ChefIA Voz é uma aplicação que integra diferentes tecnologias para oferecer uma experiência de assistência culinária por voz.

O projeto demonstra, na prática, como recursos de inteligência artificial podem ser usados para construir soluções úteis, interativas e bem estruturadas. Além de atender ao objetivo do trabalho, o sistema também possui potencial para evoluir para uma aplicação mais completa no futuro.

👨‍💻 Autor

Projeto desenvolvido por Rodrigo Cardozo de Jesus como trabalho acadêmico para estudo, com foco em inteligência artificial generativa, processamento de áudio e construção de agentes especializados.

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
