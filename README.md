# PythonAutotest

Selenium Page Objects и pytest API-тесты с Allure. Без BASE_URL/API_URL тесты
поднимают локальный `tests/demo_app.py`, имитацию проверяемого приложения.
Успешный прогон подтверждает работу тестового проекта, а не внешнего сайта.

[Проверенный запуск и ограничения](VERIFICATION.md).

```bash
python -m venv .venv
# Активируйте .venv и установите Chrome/Chromium.
python -m pip install -r requirements.txt
python -m pytest tests/ --alluredir=reports/allure-results
```

Настройки: BROWSER=chrome|firefox, HEADLESS=true|false, SELENIUM_GRID_URL.
Для своего тестового приложения задайте обе переменные BASE_URL/API_URL,
TEST_USER/TEST_PASS и соответствующие Page Objects. API-тесты создания/удаления
пользователей меняют данные выбранного API: используйте отдельный тестовый стенд.

```bash
docker compose -p autotest-local --profile local run --rm --build tests-local
```

Образ содержит Chromium и chromedriver. Вариант Selenium Grid:

```bash
docker compose -p autotest-grid run --rm --build tests
docker compose -p autotest-grid down
```

Playwright присутствует в dependencies, но исполняемые тесты используют Selenium.
Видео и Playwright Page Objects не реализованы. Allure CLI устанавливается отдельно:
`allure serve reports/allure-results`.
