# Автоматизация тестирования магазина МебельМарт
тестовый фреймворк для автоматизации UI-тестирования интернет-магазина мебели (Playwright + pytest + Page Object Model)

# Быстрый старт
## Клонировать репозиторий
git clone https://github.com/AGaniushkina/MebelMartTests.git
cd MebelMartTests

## Установить зависимости
pip install -r requirements.txt
playwright install

## Запустить тесты (параллельно 2 потока)
pytest -n 2 -v -s --alluredir=allure-results

## Открыть Allure отчет
После прогона тестов результаты сохраняются в папку `allure-results`.
allure serve allure-results/

# Тестируемый функционал
Фильтрация по характеристикам
Характеристики товара в карточке
Добавление товара в избранное
Поиск товара по названию
Корзина: добавление, проверка цены/количества
