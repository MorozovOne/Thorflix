from dotenv import load_dotenv
import os

load_dotenv()


def get_settings():
    return {
        "db_host": os.environ.get('DB_HOST'),
        "db_name": os.environ.get('DB_NAME'),
        "db_user": os.environ.get('DB_USER'),
        "db_pass": os.environ.get('DB_PASS'),
        "smtp_user": os.environ.get('SMTP_USER'),
        "smtp_pass": os.environ.get('SMTP_PASS'),
        "smtp_host": os.environ.get('SMTP_HOST'),
        "smtp_port": os.environ.get('SMTP_PORT'),
        "redis_host": os.environ.get('REDIS_HOST'),
        "secret_key": os.environ.get('SECRET_KEY'),
    }