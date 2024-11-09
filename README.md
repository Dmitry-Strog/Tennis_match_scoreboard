# Проект “Табло теннисного матча”

## Описание
Проект "Табло теннисного матча" представляет собой веб-приложение, которое позволяет отслеживать и управлять текущими и завершенными теннисными матчами. Приложение предоставляет возможность создавать новые матчи, просматривать статистику завершенных матчей, а также отслеживать текущий счет в реальном времени.

## Техническое Задание
[Техническое задание проекта](https://zhukovsd.github.io/python-backend-learning-course/projects/tennis-scoreboard/)

## Установка и запуск проекта

### 1. Клонирование репозитория
Для начала склонируйте репозиторий на свой локальный компьютер:
```bash
git clone https://github.com/Dmitry-Strog/Tennis_match_scoreboard.git
```

### 2. Установка MySQL
Убедитесь, что у вас установлена и запущена база данных MySQL. Если нет, вы можете установить её, следуя инструкциям на официальном сайте MySQL.

### 3. Установка зависимостей
Перейдите в директорию проекта и установите необходимые зависимости:
```bash
cd Tennis_match_scoreboard
pip install -r requirements.txt
```

### 4. Настройка окружения
Переименуйте файл `.env-example` в `.env` и обновите данные в соответствии с вашей конфигурацией MySQL:
```bash
mv .env-example .env
```

### 5. Применение миграций
Примените миграции для создания необходимых таблиц в базе данных:
```bash
alembic upgrade head
```

### 6. Запуск проекта
Запустите проект с помощью следующей команды:
```bash
python3 main.py
```

## Функционал приложения

### 1. Создание нового матча
- Пользователь может создать новый теннисный матч, указав имена игроков.
- После создания матча, приложение начинает отслеживать счет и состояние матча.

### 2. Просмотр законченных матчей
<img width="500" alt="image" src="https://github.com/user-attachments/assets/492dd7cb-9af5-428f-a38e-7e13dc317a33">

- Пользователь может просматривать список завершенных матчей.
- Приложение отображает список матчей с возможностью фильтрации по именам игроков.
### 3. Подсчёт очков в текущем матче
<img width="500" alt="image" src="https://github.com/user-attachments/assets/b3ad92f9-5653-480f-9c6d-bfc9cbdaa64e">

- Приложение автоматически подсчитывает очки и обновляет счет в реальном времени.
- Во время матча, приложение отображает текущий счет и состояние игры.
