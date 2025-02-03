# Проект анализа транзакций

Этот проект анализирует транзакции из файла Excel и 
генерирует данные JSON для веб-страниц, отчетов Excel и предоставляет другие услуги.

## Оглавление

- [Установка]
- [Использование]
- [Структура проекта])
- [Функции]
- [Тестирование]
- [Вклад]
- [Лицензия]
## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Kursovaya-.git
    cd Kursovaya-
    ```
2. Install dependencies using Poetry: 
    ```sh
    poetry install
    ```
3. Set up environment variables:

    Create a `.env` file in the root directory of the project and add your API keys:
    ```ini
    API_KEY=your_api_key_here
    ```

## Usage
Run the main script to see the results:

```sh
python src/main.py
   ```

## Структура проекта
kurs/
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── main.py
│   ├── views.py
│   ├── reports.py
│   └── services.py
├── data/
│   ├── operations.xlsx
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   ├── test_views.py
│   ├── test_reports.py
│   └── test_services.py
├── user_settings.json
├── .env
├── .env_template
├── .gitignore
├── .flake8
├── pyproject.toml
├── poetry.lock
└── README.md

### Функции
1. Веб-страницы-Главная: генерирует ответ JSON для главной страницы.
2. Поиск по номеру телефона: находит транзакции, содержащие номера телефонов.
3. Поиск индивидуальных переводов: находит транзакции, связанные с переводами физическим лицам.
4. Отчет о расходах по категориям: генерирует отчет о расходах по категориям.
5. Отчет о расходах в рабочие дни/выходные дни: генерирует отчет о расходах в рабочие дни и выходные.
6. 
### Тестирование
Для запуска тестов используйте следующую команду:
- pytest

### Содействие
1. Форкните репозиторий.
2. Создайте новую ветку:
- git checkout -b feature/your-feature
3. Внесите изменения и зафиксируйте их:
- git commit -m "Add your feature"
4. Запуште ветку:
- git push origin feature/your-feature
5. Создайте запрос

### Лицензия
Этот проект распространяется по лицензии MIT. 
Подробности смотрите в файле ЛИЦЕНЗИИ.
