```python
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# 替换成您的Telegram Bot Token
BOT_TOKEN = '7688982261:AAF7-gckvMdnvwgiGCh7LZrl4jB2rJ3STpY'

def start(update: Update, context: CallbackContext) -> None:
    """发送欢迎消息并添加置顶按钮"""
    # 发送欢迎消息
    context.bot.send_message(chat_id=update.effective_chat.id, text="欢迎使用tradingtop AI!")
    
    # 创建置顶按钮
    keyboard = [[InlineKeyboardButton("访问 tradingtop.com", url="https://tradingtop.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # 发送消息并置顶
    message = context.bot.send_message(chat_id=update.effective_chat.id, text="点击这里访问 tradingtop.com", reply_markup=reply_markup)
    context.bot.pin_chat_message(chat_id=update.effective_chat.id, message_id=message.message_id)

def main() -> None:
    """启动机器人"""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # 添加命令处理程序
    dispatcher.add_handler(CommandHandler("start", start))

    # 开始轮询
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

