import os


def format_date(date):
    return date.strftime("%Y-%m-%d")

def generate_id():
    return os.urandom(16).hex()
