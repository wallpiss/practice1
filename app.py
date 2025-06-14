from flask import Flask  # Импортируем Flask

app = Flask(__name__)  # Создаём приложение

@app.route("/")  # Говорим: "При запросе главной страницы делай следующее"
def hello():
    a = 1 + 2
    return "Привет! Это мой первый сайт!"  # Выводим текст

if __name__ == "__main__":
    app.run()  # Запускаем сервер