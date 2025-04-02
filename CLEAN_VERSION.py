import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests
import tempfile
import openai
import subprocess

# === Fill-in: API Keys ===
TELEGRAM_BOT_TOKEN = "7631176242:AAFqzrasidsIG9-QCHybzvicdtIpSd5YEVo"
openai.api_key = "sk-vyUOp4E5FV50k16n94ZriT3BlbkFJQYHHRXpNXrJ2mNaT8rg"

# === File where transcription will be saved ===
OUTPUT_FILE_PATH = "/Users/tomastovey/Documents/telegram-voice-bot/commands.txt"

# === Function to transcribe voice ===
def transcribe_audio(mp3_path):
    with open(mp3_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

# === Bot handler ===
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as temp_ogg:
        await file.download_to_drive(temp_ogg.name)

    # Convert .ogg to .mp3 using ffmpeg
    mp3_path = temp_ogg.name.replace(".ogg", ".mp3")
    subprocess.run(["ffmpeg", "-i", temp_ogg.name, mp3_path], check=True)

    # Transcribe
    text = transcribe_audio(mp3_path)

    # Save to file
    with open(OUTPUT_FILE_PATH, "w") as f:
        f.write(text)

    # Let user know
    await update.message.reply_text(f"📝 Transcribed:\n{text}")

# === Main ===
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Start bot (NO scheduler included)
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    print("🎤 Bot is listening for voice notes...")
    app.run_polling()

