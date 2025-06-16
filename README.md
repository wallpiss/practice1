# 🚀 Flask-приложение в Docker с автодеплоем через GitHub Actions

Простое Flask-приложение, автоматически собираемое и развёртываемое на сервер через GitHub Actions.

## 🧠 Описание проекта

Это базовое веб-приложение на Flask, которое выводит приветственное сообщение.  
Оно развёртывается в Docker-контейнере на удалённом сервере каждый раз, когда происходит `push` в ветку `main`.

---

## 📁 Структура проекта

```

├── app.py                # Код приложения Flask
├── requirements.txt      # Зависимости Python
├── Dockerfile            # Инструкция сборки Docker-образа
├── .github/workflows/
│   └── docker-build.yml  # CI/CD pipeline на GitHub Actions
└── README.md             # Документация проекта

````

---

## 🐍 Код приложения (Flask)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет! Это мой первый сайт!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
````

---

## 🐳 Dockerfile

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## 🛠️ GitHub Actions (CI/CD)

Файл `.github/workflows/docker-build.yml`:

* Проверяет и копирует код на сервер при каждом `push` в ветку `main`.
* Собирает Docker-образ на сервере.
* Перезапускает контейнер с обновлённой версией приложения.

Пример:

```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:
```

Секреты:

* `SERVER_IP` — IP-адрес сервера
* `SSH_PRIVATE_KEY` — приватный ключ SSH для доступа

---

## 🧪 Как запустить локально

1. Установите Docker
2. Выполните в терминале:

```bash
docker build -t my-app .
docker run -d -p 5000:5000 --name flask-container my-app
```

3. Перейдите в браузере по адресу [http://localhost:5000](http://localhost:5000)

---

## ⚙️ Как устроен процесс деплоя

1. Push в `main` → GitHub Actions запускается
2. Код копируется на сервер через SSH
3. На сервере:

   * Сборка нового Docker-образа
   * Остановка и удаление старого контейнера (если был)
   * Запуск нового контейнера
4. Приложение доступно по адресу `http://<SERVER_IP>:5000`

---

## 📋 Зависимости

```
flask==3.1.1
werkzeug==3.1.3
requests==2.26.0
```

---

## 📌 Пример вывода

```
Привет! Это мой первый сайт!
```

---

## ✅ Статус
- [x] Dockerfile работает
- [x] GitHub Actions запускается при push
- [x] Проект собирается и запускается в контейнере
- [x] README содержит инструкции 

