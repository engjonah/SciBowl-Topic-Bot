#Keep bot up 24/7
#Use https://uptimerobot.com/ to ping website every 15 mins to keep replit from shutting down
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Page for discord bot"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()