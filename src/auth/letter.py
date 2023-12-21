import smtplib
from email.message import EmailMessage



def send_letter_to_email(token: str, username: str, email_str: str):
    email = EmailMessage()
    email['Subject'] = 'Ваш код для подтверждения'
    email['From'] = SMTP_USER
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
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)