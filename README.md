# PythonAutotest

Фреймворк автоматизации тестирования веб-приложений на Python.

## Описание

Собственный фреймворк для E2E и API-тестирования с поддержкой Page Object паттерна, автоскриншотов и отчётности.

## Технологии

- **Язык:** Python 3.11+
- **Тестирование:** pytest, Selenium, Playwright
- **Отчётность:** Allure
- **Данные:** pytest.fixture, параметризация
- **Деплой:** Docker, GitHub Actions

## Возможности

- Page Object Model паттерн
- Selenium + Playwright поддержка
- pytest + Allure отчётность
- Автоскриншоты при падении тестов
- Параметризация тестов
- API тестирование
- Docker интеграция
- CI/CD (GitHub Actions)

## Установка и запуск

```bash
# Клонирование
git clone https://github.com/AlexGoster/PythonAutotest.git
cd PythonAutotest

# Установка зависимостей
pip install -r requirements.txt

# Установка браузеров
playwright install chromium

# Запуск тестов
pytest tests/ --alluredir=reports/

# Просмотр отчёта
allure serve reports/
```

## Структура проекта

```
PythonAutotest/
├── pages/              # Page Objects
│   ├── login_page.py
│   ├── home_page.py
│   └── base_page.py
├── tests/              # Тесты
│   ├── test_login.py
│   ├── test_search.py
│   └── test_cart.py
├── utils/              # Утилиты
│   ├── driver.py       # WebDriver
│   └── helpers.py      # Вспомогательные функции
├── reports/            # Отчёты Allure
├── conftest.py         # Фикстуры pytest
├── config.py           # Конфигурация
├── pytest.ini          # Настройки pytest
├── Dockerfile
└── docker-compose.yml
```

## Пример теста

```python
# tests/test_login.py
from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open("https://example.com/login")
    page.enter_email("user@example.com")
    page.enter_password("password123")
    page.click_login()
    assert page.is_logged_in() == True
```

## CI/CD

```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: playwright install chromium
      - run: pytest tests/ --alluredir=reports/
```

## Что я изучила

- Проектирование тестовой архитектуры (Page Object)
- Работа с Selenium и Playwright
- Параметризация и фикстуры pytest
- Интеграция с Allure для отчётности
- Настройка CI/CD pipeline

## License

MIT License - AlexGoster


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-23


Last updated: 2026-09-23


Last updated: 2026-09-23


Last updated: 2026-09-21


Last updated: 2026-09-21


Last updated: 2026-09-21
