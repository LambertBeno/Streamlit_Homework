# Streamlit_Homework

### Описание проекта

Этот проект представляет собой Streamlit-приложение для:
1. **Исследования данных** по чаевым в вымышленном ресторане.
2. **Визуализации котировок акций** на основе данных с Yahoo Finance.

Приложение позволяет загружать пользовательские данные, генерировать недостающие данные, строить различные графики для анализа данных, а также отображать котировки акций для выбранного тикера.

### Функциональность:
- Загрузка пользовательских данных в форматах: CSV, XLSX, TXT.
- Автоматическая генерация недостающих данных (например, даты).
- Построение различных графиков для анализа данных по чаевым.
- **Визуализация котировок акций**:
  - Ввод тикера акций (например, AAPL для Apple, GOOGL для Google).
  - Выбор временного диапазона для отображения котировок.
  - Отображение графиков цены закрытия и объёма торгов по выбранному тикеру.
  - Возможность выбора интервала данных (день, неделя, месяц и т.д.).
- Возможность скачивания графиков в формате PNG.

### Запуск приложения

1. После установки всех зависимостей, запустите приложение Streamlit:
    ```bash
    streamlit run main.py
    ```

2. Откройте браузер и перейдите по адресу:
    ```
    http://localhost:8501
    ```

### Структура проекта

- `data_processing/` — директория с модулями для обработки данных (например, словари).
- `modules/` — директория с основными функциями для обработки данных.
- `scripts/` — скрипты для генерации данных и построения графиков.
- `pages/` — страницы приложения Streamlit (разделение на разные функциональные страницы).
- `venv/` — виртуальное окружение.
- `main.py` — основной файл для запуска приложения.
- `requirements.txt` — файл со всеми зависимостями проекта.
- `README.md` — этот файл.

### Визуализация котировок акций

Приложение предоставляет возможность ввода тикера акций, на основании которого происходит получение данных с Yahoo Finance. Пользователь может выбрать временной диапазон и интервал (день, неделя, месяц) для отображения графиков цены закрытия и объёма торгов. Это даёт возможность исследовать исторические данные по акциям за выбранный период.

### Зависимости

Список основных библиотек, необходимых для работы проекта:
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `yfinance`
- и другие (см. полный список в `requirements.txt`)

### Использование

1. Загрузите файл данных в поддерживаемом формате (CSV, XLSX, TXT).
2. Исследуйте данные, используя графики, доступные через интерфейс.
3. Введите тикер для просмотра котировок акций.
4. Постройте графики, выбрав различные параметры визуализации.
5. Скачивайте построенные графики с помощью боковой панели.

### Примечания

- Проект автоматически генерирует недостающие данные, такие как даты, если они отсутствуют в загружаемом файле.
- Обратите внимание на структуру загружаемых данных — проект предполагает наличие определённых столбцов (например, сумма счета, чаевые и т.д.).
