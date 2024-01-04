import smtplib
from email.message import EmailMessage

from core.config import get_settings

smtp_user = get_settings().get('smtp_user')
smtp_pass = get_settings().get('smtp_pass')
smtp_host = get_settings().get('smtp_host')
smtp_port = get_settings().get('smtp_port')


def send_letter_to_email(token: str, username: str, email_str: str):
    email = EmailMessage()
    email['Subject'] = 'Ваш код для подтверждения'
    email['From'] = smtp_user
    email['To'] = email_str

    email.set_content(
        '<div>'
        f'<div style="color: #121212; padding: 32px 32px;">'
        f'</h3 style="font-family: Roboto;">Привет {username}, мы прислали тебе токен!</h3>'
        f'<p style="color: black; font-family: Roboto;">{token}</p>'
        f'</div>'
        '</div>',
        subtype='html'
    )
    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(email)