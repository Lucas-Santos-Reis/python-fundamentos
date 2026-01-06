from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def menu_principal():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("📝 Cadastro", callback_data="cadastro"))
    markup.add(InlineKeyboardButton("🔔 Ativar Notificações", callback_data="notificacoes"))
    markup.add(InlineKeyboardButton("🛠️ Serviços", callback_data="servicos"))
    markup.add(InlineKeyboardButton("ℹ️ Sobre", callback_data="sobre"))
    return markup

def menu_servicos():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📦 Bot de Atendimento", callback_data="servico_atendimento"))
    markup.add(InlineKeyboardButton("🤖 Bot Personalizado", callback_data="servico_personalizado"))
    markup.add(InlineKeyboardButton("💰 Solicitar Orçamento", callback_data="solicitar_orcamento"))
    markup.add(InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu"))
    return markup

def botao_contato():
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    botao = KeyboardButton(
        "📱 Compartilhar meu número",
        request_contact=True
    )
    markup.add(botao)
    return markup





    
