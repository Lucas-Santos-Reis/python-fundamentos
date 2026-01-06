from user_menu import menu_principal, botao_contato, menu_servicos

from user_services import salvar_cadastro, salvar_orcamento
from telebot import types
from telebot.types import ReplyKeyboardRemove

# ===============================
# CONTROLE DE ESTADO (MEMÓRIA)
# ===============================
usuarios_aguardando_orcamento = set()
usuarios_aguardando_telefone = set()


def registrar_handlers(bot):

    # ===============================
    # START / MENU
    # ===============================
    @bot.message_handler(commands=['start', 'menu'])
    def start_menu(message: types.Message):
        bot.send_message(
            message.chat.id,'''
    👋 Olá! Bem-vindo ao AutoAssist Bot.
    Faça seu cadastro para começar a usar nossos serviços
    ou escolha uma opção no menu abaixo.''',
            reply_markup=menu_principal()
        )

    # ===============================
    # CALLBACKS INLINE
    # ===============================
    @bot.callback_query_handler(func=lambda call: True)
    def tratar_callbacks(call: types.CallbackQuery):

        try:
            bot.answer_callback_query(call.id)
        except:
            return

        chat_id = call.message.chat.id

        # ---------- CADASTRO ----------
        if call.data == "cadastro":

            # REMOVE O INLINE KEYBOARD (OBRIGATÓRIO)
            bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=call.message.message_id,
                reply_markup=None
            )

            # MARCA ESTADO DE CADASTRO
            usuarios_aguardando_telefone.add(chat_id)

            bot.send_message(
                chat_id,
                "📱 Se estiver no celular, use o botão abaixo.\n"
                "💻 Se estiver no Telegram Web, digite seu telefone com DDD."
            )

            bot.send_message(
                chat_id,
                "Compartilhe seu telefone:",
                reply_markup=botao_contato()
            )

        # ---------- NOTIFICAÇÕES ----------
        elif call.data == "notificacoes":
            bot.send_message(chat_id, "⚠️ Notificações ainda não disponíveis. Em breve!")
        elif call.data == "sobre":
            bot.send_message(chat_id, '''
    AutoAssist Bot v1.0
    Desenvolvido para facilitar o atendimento automático.
    📩 Entre em contato para mais informações:
    Telegram: @lucasreis364
    Linkedin: linkedin.com/in/lucassantosreis''')
        # ---------- SERVIÇOS ----------
        elif call.data == "servicos":
            bot.send_message(
                chat_id,
                "🛠️ *Nossos Serviços*",
                reply_markup=menu_servicos(),
                parse_mode="Markdown"
            )

        elif call.data == "servico_atendimento":
            bot.send_message(chat_id, '''
    📦 Bot automatizado para atendimento ao cliente, com respostas rápidas, coleta de informações, registro de pedidos e integração com canais de comunicação, reduzindo tempo de resposta e aumentando a eficiência do suporte.''')

        elif call.data == "servico_personalizado":
            bot.send_message(chat_id, '''
    🤖 Desenvolvimento de bots personalizados para atender às necessidades específicas do seu negócio, seja para atendimento ao cliente, automação de processos internos ou integração com outras plataformas, proporcionando soluções sob medida para otimizar suas operações, solicite seu orçamento conosco!''')

        # ---------- ORÇAMENTO ----------
        elif call.data == "solicitar_orcamento":
            usuarios_aguardando_orcamento.add(chat_id)

            bot.send_message(
                chat_id,
                "💰 Descreva brevemente o seu negócio e o que você precisa (texto):"
            )

        # ---------- VOLTAR ----------
        elif call.data == "voltar_menu":
            bot.send_message(
                chat_id,
                "⬅️ Menu principal:",
                reply_markup=menu_principal()
            )

    # ===============================
    # RECEBE CONTATO (CADASTRO MOBILE)
    # ===============================
    @bot.message_handler(content_types=['contact'])
    def receber_contato(message: types.Message):
        chat_id = message.chat.id

        # IGNORA CONTATOS FORA DO FLUXO
        if chat_id not in usuarios_aguardando_telefone:
            return

        usuarios_aguardando_telefone.remove(chat_id)

        salvar_cadastro(
            chat_id,
            message.from_user.id,
            message.from_user.first_name,
            message.contact.phone_number
        )

        bot.send_message(
            chat_id,
            "✅ Cadastro realizado com sucesso!",
            reply_markup=ReplyKeyboardRemove()
        )

        bot.send_message(
            chat_id,
            "Menu principal:",
            reply_markup=menu_principal()
        )

    # ===============================
    # TELEFONE DIGITADO (TELEGRAM WEB)
    # ===============================
    @bot.message_handler(
        func=lambda m: m.text and m.text.replace(" ", "").replace("+", "").isdigit()
    )
    def receber_telefone_digitado(message: types.Message):
        chat_id = message.chat.id

        if chat_id not in usuarios_aguardando_telefone:
            return

        usuarios_aguardando_telefone.remove(chat_id)

        salvar_cadastro(
            chat_id,
            message.from_user.id,
            message.from_user.first_name,
            message.text
        )

        bot.send_message(
            chat_id,
            "✅ Cadastro realizado com sucesso!",
            reply_markup=menu_principal()
        )

    # ===============================
    # TEXTO LIVRE (ORÇAMENTO)
    # ===============================
    @bot.message_handler(func=lambda m: True, content_types=['text'])
    def tratar_texto(message: types.Message):
        chat_id = message.chat.id

        # SOMENTE PROCESSA SE FOR ORÇAMENTO
        if chat_id not in usuarios_aguardando_orcamento:
            return

        usuarios_aguardando_orcamento.remove(chat_id)

        salvar_orcamento(chat_id, message.text)

        bot.send_message(
            chat_id,
            "✅ Orçamento solicitado com sucesso!",
            reply_markup=menu_principal()
        )
