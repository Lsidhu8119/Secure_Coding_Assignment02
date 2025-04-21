import os
import subprocess
import pymysql
from urllib.request import urlopen

# Securely load database config from environment variables
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "changeme"),
}


def get_user_input():
    user_input = input("Enter your name: ")
    return user_input


def send_email(to, subject, body):
    # Secure subprocess call to prevent shell injection (fixes Bandit warning)
    subprocess.run(["mail", "-s", subject, to], input=body.encode(), check=True)


def get_data():
    url = "http://insecure-api.com/get-data"
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input)
