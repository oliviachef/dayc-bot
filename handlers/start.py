from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "Hey there, I'm alive.\nI am an AI ChatBot developed by 💛 by @imoliviant"
    )


__handlers__ = [
    [
        CommandHandler(
            "alexa",
            start
        )
    ]
]
