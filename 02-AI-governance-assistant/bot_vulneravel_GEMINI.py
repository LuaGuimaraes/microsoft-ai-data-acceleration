import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ============================================================
# PROJETO: DioBot - Versão Vulnerável (Sem Governança)
#
# Objetivo:
# Esta versão foi criada propositalmente SEM filtros de segurança
# e SEM rastreabilidade para demonstrar os riscos do uso de IA
# em um ambiente corporativo sem governança.
#
# Aqui, a IA responde praticamente qualquer coisa.
# Isso é poderoso, mas extremamente perigoso para empresas.
# ============================================================

# 1. Carrega as variáveis de ambiente a partir do arquivo .env
# As chaves NAO ESTAO e NUNCA ficam no código por segurança.
load_dotenv()

# 2. Configura a chave da API do Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# 3. Configura o modelo Gemini SEM filtros de segurança
# Atenção: isso é proposital e faz parte do experimento.
# Em produção, isso NUNCA deve ser feito.
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    safety_settings=safety_settings,
    system_instruction="Você é um assistente financeiro."
)

# ---------------- INTERFACE ----------------

st.set_page_config(
    page_title="DioBot V1 - Sem Governança",
    page_icon="⚠️"
)

st.title("DioBot V1 - Sem Governança")
st.warning(
    "Este assistente não possui filtros nem rastreabilidade. "
    "Ele é propositalmente vulnerável.",
    icon="⚠️"
)

# Inicializa o histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens antigas no chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
prompt = st.chat_input("O que você precisa?")

if prompt:
    # Mostra a mensagem do usuário na tela
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Converte o histórico para o formato esperado pelo Gemini
    history = []
    for msg in st.session_state.messages[:-1]:
        role = "user" if msg["role"] == "user" else "model"
        history.append({"role": role, "parts": [msg["content"]]})

    # Chama o modelo SEM qualquer controle de segurança
    try:
        chat = model.start_chat(history=history)
        response = chat.send_message(prompt)
        resposta = response.text
    except Exception as e:
        resposta = f"Erro ao chamar a API: {e}"

    # Mostra a resposta da IA
    st.chat_message("assistant").markdown(resposta)
    st.session_state.messages.append(
        {"role": "assistant", "content": resposta}
    )