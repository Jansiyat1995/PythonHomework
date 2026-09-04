# PythonHomework

## Запуск тестов

Из корня проекта `PythonHomework` выполните:

```powershell
$env:PYTHONPATH=".\10_lesson"; .\.venv\Scripts\python.exe -m pytest .\10_lesson\tests\test_calculator.py --alluredir=allure-results
```

## Просмотр отчёта

После выполнения тестов выполните:

```powershell
allure serve .\allure-results
```

Отчёт откроется в браузере.
