import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import requests
import uuid
from datetime import datetime

# ============================================================
# PROJETO: DioBot - Versão Governada
#
# Objetivo:
# Demonstrar o uso consciente de IA em ambiente corporativo,
# adicionando:
# - Filtros de compliance
# - Classificação de risco
# - Rastreabilidade e auditoria com Langfuse
#
# Essa versão representa o que seria aceitável em produção.
# ============================================================

# 1. Carrega variáveis de ambiente
load_dotenv()

# --- GEMINI ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# --- LANGFUSE ---
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_BASE_URL = "https://cloud.langfuse.com"

# Função responsável por enviar logs de auditoria para o Langfuse
def enviar_para_langfuse(input_usuario, resposta_ia, risco, motivo):
    """
    Envia para o Langfuse:
    - O prompt do usuário
    - A resposta da IA
    - O nível de risco
    - O motivo da decisão
    """
    if not LANGFUSE_PUBLIC_KEY or not LANGFUSE_SECRET_KEY:
        return

    trace_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat() + "Z"

    payload = {
        "batch": [
            {
                "id": str(uuid.uuid4()),
                "type": "trace-create",
                "timestamp": now,
                "body": {
                    "id": trace_id,
                    "name": "chat_diobot",
                    "environment": "production",
                    "input": {"mensagem": input_usuario},
                    "output": {"resposta": resposta_ia},
                    "metadata": {"risco": risco, "motivo": motivo}
                }
            }
        ]
    }

    requests.post(
        f"{LANGFUSE_BASE_URL}/api/public/ingestion",
        auth=(LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY),
        json=payload,
        timeout=5
    )

# ---------------- INTERFACE ----------------

st.set_page_config(
    page_title="DioBot V2 - Governado",
    page_icon="✅",
    layout="wide"
)

st.sidebar.title("🔐 Auditoria")

if LANGFUSE_PUBLIC_KEY:
    st.sidebar.success("Langfuse conectado")

st.title("DioBot V2 - Uso Consciente de IA")

# Inicializo histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Digite sua dúvida")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Regras simples de compliance
    termos_proibidos = ["lavar dinheiro", "sonegar", "matar", "tráfico"]

    if any(t in prompt.lower() for t in termos_proibidos):
        resposta = "🚫 Solicitação bloqueada por política de compliance."
        risco = "ALTO"
        motivo = "Conteúdo potencialmente ilegal ou perigoso."

        enviar_para_langfuse(prompt, resposta, risco, motivo)

        st.chat_message("assistant").markdown(resposta)
        st.session_state.messages.append(
            {"role": "assistant", "content": resposta}
        )
        st.stop()

    # Chamada normal do modelo
    chat = model.start_chat()
    response = chat.send_message(prompt)
    resposta = response.text

    enviar_para_langfuse(
        prompt,
        resposta,
        risco="BAIXO",
        motivo="Interação permitida"
    )

    st.chat_message("assistant").markdown(resposta)
    st.session_state.messages.append(
        {"role": "assistant", "content": resposta}
    )