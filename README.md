# PythonAutotest

Фреймворк автоматизации тестирования веб-приложений.

## Возможности

- Page Object Model паттерн
- Selenium + Playwright поддержка
- pytest + Allure отчётность
- Автоскриншоты при падении
- API тестирование
- Docker интеграция

## Установка

```bash
pip install -r requirements.txt
playwright install chromium
```

## Использование

```bash
pytest tests/ --alluredir=reports/
```

## Структура

```
PythonAutotest/
├── pages/          # Page Objects
├── tests/          # Тесты
├── utils/          # Утилиты
├── conftest.py     # Фикстуры pytest
└── config.py       # Конфигурация
```

## CI/CD

```yaml
# GitHub Actions
- name: Run tests
  run: pytest tests/ --alluredir=reports/
```

MIT License - AlexGoster
