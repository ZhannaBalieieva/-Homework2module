import telegram
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes




app = ApplicationBuilder().token('5850848888:AGGYIfZZ0J-9aq89T7HHtUVwXPP0GD8lAKA').build()


app.add_handler("hello")

app.run_polling()