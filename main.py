from typing import Final
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, \
    CallbackQueryHandler
import os

from database import client
from services.transaction_service import TransactionService

load_dotenv()

BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')
CUSTOMER_COMMAND: Final = 'customer'
SUPPLIER_COMMAND: Final = 'supplier'

transaction_service = TransactionService()


def start_transaction():
    try:
        new_transaction = transaction_service.store("First Last", "first transaction", "chatter", "BTC")

        print(new_transaction)
    except Exception as e:
        print(e)


def all_transactions():
    try:
        transactions = transaction_service.all()

        print(transactions)
    except Exception as e:
        print(e)


def update_transaction():
    try:
        update = {
            "customer_id": "nothing here",
            "customer_address": "098765567890jeue",
            "status": "COMPLETED"
        }

        transaction = transaction_service.update("66e85a3bc49697d32c2c2dcf", update)

        print(transaction)
    except Exception as e:
        print(e)


# Commands
async def start_command(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Start New Transaction", callback_data='new_transaction')],
        [InlineKeyboardButton("Help", callback_data='help')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Escrow Service Bot! Choose an option:", reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'new_transaction':
        await query.edit_message_text(text="Please enter transaction details in the format '/customer \
        <wallet_address>'.")

    elif query.data == 'help':
        await query.edit_message_text(text="To start a new transaction, click 'Start New Transaction'. For assistance, \
        contact support@fairscrow.com.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Right then. I am a help bot. I am here to help you. I can help you with the '
                                    'following commands:\n')


async def record_customer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text: str = update.message.text
    user = update.message.from_user.id

    print(f'User ({user}) sent: "{message_text}"')

    if update.message.chat.type != 'group':
        await update.message.reply_text('This command only works in groups.')
        return

    message_text = message_text.replace(f'/{CUSTOMER_COMMAND}', '').strip()

    if BOT_USERNAME in message_text:
        message_text = message_text.replace(BOT_USERNAME, '').strip()

    print(f'User ({user}) sent: "{message_text}"')
    print(f'User ({user}) sent: "{message_text.strip("/")}"')

    if len(message_text) == 0:
        await update.message.reply_text('Incorrect message format. Expecting your wallet address.')
        return

    # base_coin = verify_wallet_address(message_text)
    #
    # if base_coin == 'Unknown':
    #     await update.message.reply_text('Unknown wallet address. Please check and try again.')
    #     return
    #
    # await update.message.chat.send_message(f'User ({user}) provided a "{base_coin}" address.')
    #
    # updated_transaction = transaction_service.add_customer_details(user, message_text, base_coin)
    #
    # print(updated_transaction)
    #
    # if not updated_transaction['status']:
    #     await update.message.reply_text(updated_transaction['message'])
    #     return

    await update.message.reply_text('An escrow account will be generated below. Please verify the escrow \
    account before making payment.')


async def record_supplier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text: str = update.message.text
    user = update.message.from_user.id
    group_id = update.message.chat.id

    print(update)

    print(f'User ({user}) sent: "{message_text}"')

    if update.message.chat.type != 'group':
        await update.message.reply_text('This command only works in groups.')
        return

    message_text = message_text.replace(f'/{SUPPLIER_COMMAND}', '').strip()

    if BOT_USERNAME in message_text:
        message_text = message_text.replace(BOT_USERNAME, '').strip()

    print(f'User ({user}) sent: "{message_text}"')
    print(f'User ({user}) sent: "{message_text.strip("/")}"')

    if len(message_text) == 0:
        await update.message.reply_text('Incorrect message format. Expecting your wallet address.')
        return

    # base_coin = verify_wallet_address(message_text)
    #
    # if base_coin == 'Unknown':
    #     await update.message.reply_text('Unknown wallet address. Please check and try again.')
    #     return
    #
    # await update.message.chat.send_message(f'User ({user}) provided a "{base_coin}" address.')
    #
    # last_transaction = transaction_service.get_last_transaction()
    #
    # print(last_transaction)
    #
    # if last_transaction is None or last_transaction.customer_id is not None:
    #     transaction_service.add_new_transaction(group_id, user, message_text, base_coin)

    # updated_transaction = transaction_service.add_customer_details(user, message_text)
    #
    # print(updated_transaction)
    #
    # if not updated_transaction['status']:
    #     await update.message.reply_text(updated_transaction['message'])
    #     return

    await update.message.reply_text('The customer can proceed to provide a wallet address.')


# Responses
async def handle_response(text: str) -> str:
    processed_text = text.lower()

    if 'hello' in processed_text:
        return 'Hello there!'

    if 'how are you' in processed_text:
        return 'I am good! How about you?'

    if 'i love python' in processed_text:
        return 'Remember to subscribe.'

    return 'I do not understand what you wrote.'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    message_text: str = update.message.text

    print(f'User ({update.message.chat.id}) in ({message_type}) sent: "{message_text}"')

    if message_type == 'group':
        if BOT_USERNAME in message_text:
            new_text: str = message_text.replace(BOT_USERNAME, '').strip()
            response: str = await handle_response(new_text)
        else:
            return

    else:
        response: str = await handle_response(message_text)

    print('Bot:', response)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Main
def main():
    print('Starting bot...')
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('customer', record_customer))
    app.add_handler(CommandHandler('supplier', record_supplier))
    app.add_handler(CallbackQueryHandler(button))

    # Responses
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling
    print('Bot started. Polling...')
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
