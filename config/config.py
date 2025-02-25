import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('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')
TWILIO_SID = os.getenv('ACdf9c98796adf3037c55d53aa31b9ab17')
TWILIO_TOKEN = os.getenv('e08b1184b1adee895dbcd7a5cc4c8fb4')
FROM = os.getenv('whatsapp:+14155238886')

DB_DIR = 'data/db'
INPUT_FILE_PATH = 'data/input/sample.pdf'
OUTPUT_DIR = 'data/output'
