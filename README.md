# Парсер PEPs Python 🐍

### Данный проект позволяет спарсить список всех PEP и посчитать их количество в каждом статусе.

### Порядок запуска:
1. Активируйте виртуальное окружение и установите зависимости в скачанный репозиторий:

   ```python -m venv venv```

   ```source venv/Scripts/activate (для windows) /// source venv/bin/activate (для mac OS)```

   ```python -m pip install -r requirements.txt```

2. Запускайте парсер:

   ```scrapy crawl pep```

### Результаты:
После запуска у Вас появится директория results, внутри которой будут находиться результаты парсинга в виде двух файлов .csv: в одном - список всех PEP (номер, название, статус), в другом: количество PEP в каждой категории и общее кол-во PEP.

<p align=center>
  <a href="url"><img src="https://github.com/xaer981/xaer981/blob/main/main_cat.gif" align="center" height="40" width="128"></a>
</p>
