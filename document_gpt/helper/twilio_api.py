from twilio.rest import Client

from config import config

account_sid = 'ACdf9c98796adf3037c55d53aa31b9ab17'
auth_token = 'e08b1184b1adee895dbcd7a5cc4c8fb4'
client = Client(account_sid, auth_token)

def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.
    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send
    Returns:
        - None
    '''

    _ = client.messages.create(
        from_= 'whatsapp:+14155238886',
        body=message,
        to=to
    )
