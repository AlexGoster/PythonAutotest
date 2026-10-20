# Проверка проекта

Проверки выполнялись 10–20 октября 2026. Исходная рабочая копия была чистой.

12 тестов прошли. Настоящий headless Selenium и HTTP API на Windows: login/search/cart/API против локального tests/demo_app.py. Исправлены headless, удалённый Grid и сеть Compose.

Проверен тестовый стенд, не внешний сайт. Playwright присутствует в dependencies, но исполняемые Page Objects используют Selenium. Docker Grid/Firefox не подтверждены.

## Повторный запуск

Команды из папки проекта после создания и активации Python venv. Нужен установленный Chrome/Chromium. Без BASE_URL/API_URL тесты сами поднимают локальную имитацию; внешние сайты не используются.

```bash
python -m venv .venv
# Активируйте .venv согласно ОС.
python -m pip install -r requirements.txt
python -m pytest tests/ --alluredir=reports/allure-results
```

Тесты в отдельном тестовом окружении:

```bash
python -m pytest -o addopts= -q
```

20 октября образ собран и те же 12 тестов прошли в Linux Docker с настоящим Chromium/chromedriver и локальной имитацией приложения. Внешние сайты, PostgreSQL и Redis этому прогону не нужны.

Повторить контейнерный прогон: `docker compose -p autotest-local --profile local run --rm --build tests-local`.
Firefox и удалённый Selenium Grid не проверялись.
