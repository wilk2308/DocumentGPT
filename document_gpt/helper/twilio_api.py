from twilio.rest import Client
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Recuperar credenciais do arquivo .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Inicializar o cliente Twilio
client = Client(account_sid, auth_token)

def send_message(to: str, message: str) -> None:
    '''
    Envia uma mensagem para um número no WhatsApp via Twilio.

    Parâmetros:
        - to (str): Número do destinatário no formato 'whatsapp:+55XXXXXXXXX'
        - message (str): Texto da mensagem a ser enviada

    Retorno:
        - None
    '''

    try:
        response = client.messages.create(
            from_=from_whatsapp_number,
            body=message,
            to=to
        )
        print(f"Mensagem enviada com sucesso! SID: {response.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
