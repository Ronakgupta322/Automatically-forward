from telegram.ext import Application
import logging

# Yahan apna Bot Token dalein
TOKEN = "8929419914:AAE2KSckOvIoPamxzFWtvG67-SmkIVtoXRA"

# Yahan apne sabhi Groups aur Channels ki Chat IDs dalein (Comma se separate karke)
# Public channel ke liye "@channelusername", private ke liye "-100xxxxxxx"
CHAT_IDS = [
    "-1002737072144", 
    "-1002341372879", 
    "-1002560639857",
    "@EkAurGroup"
]

# Jo message aap bhejna chahte hain
MESSAGE_TEXT = "Hello Everyone! Yeh ek automated 1-minute alert hai."

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def send_auto_msg(context):
    for chat in CHAT_IDS:
        try:
            await context.bot.send_message(chat_id=chat, text=MESSAGE_TEXT)
            print(f"Success: Message sent to {chat}")
        except Exception as e:
            # Agar bot kisi group se remove ho gaya ho ya error aaye toh dusre groups me rukna nahi chahiye
            print(f"Error sending to {chat}: {e}")

def main():
    application = Application.builder().token(TOKEN).build()

    # interval=60 (Har 1 minute me chalega)
    application.job_queue.run_repeating(send_auto_msg, interval=60, first=1)

    print("Bot is running... Message har 60 second me jayega.")
    application.run_polling()

if __name__ == '__main__':
    main()
