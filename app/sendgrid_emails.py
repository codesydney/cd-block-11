from app.config import Config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(user_email):
    message = Mail(
        from_email = Config.SENDER_EMAIL,
        to_emails= user_email,
        subject='Account created',
        plain_text_content='Hello, Your citizen dev account has been successfully created'
    )
    sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
    response = sg.send(message)
