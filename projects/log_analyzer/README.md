# log_analyzer

Учебная утилита для анализа логов станка или производственного процесса.

## Что делает

- читает файл `sample_log.txt`;
- считает общее количество строк;
- считает события `CNC`;
- считает события `Spindle`;
- считает события `Program running`;
- сохраняет отчёт в `report.txt`.

## Запуск

```powershell
python projects\log_analyzer\log_analyzer.py
```

## Пример вывода

```text
CNC событий: 3
Spindle событий: 2
Program running событий: 3
Всего строк: 8
```

## Что использовано

- `pathlib.Path` для работы с путями;
- `open(..., encoding="utf-8")` для чтения и записи файлов;
- `try/except FileNotFoundError` для обработки отсутствующего файла;
- счётчики и условия `if`.