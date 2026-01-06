from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

ARQ_ORCAMENTOS = "data/orcamentos.txt"
ARQ_CADASTROS = "data/cadastros.txt"

def salvar_cadastro(chat_id, user_id, nome, telefone):
    with open(ARQ_CADASTROS, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now()} | chat_id={chat_id} | user_id={user_id} | nome={nome} | telefone={telefone}\n"
        )

def salvar_orcamento(chat_id, texto):
    with open(ARQ_ORCAMENTOS, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now()} | chat_id={chat_id} | orçamento={texto}\n"
        )
