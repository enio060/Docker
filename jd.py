# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return f"""
    <html>
        <head>
            <title>Informacje</title>
        </head>
        <body>
            <h1>Informacje o użytkowniku</h1>
            <p>Imię: xxxx</p>
            <p>Nazwisko: xxxxx</p>
            <p>Numer indeksu: 123456</p>
            <p>Data i godzina: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
