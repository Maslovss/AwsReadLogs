# AwsReadLogs

Python скрипт для чтения лог файлов AWS CloudTrail

## Копирование логов с AWS сервера на локальный компьютер

AWS CloudTrail копирует каждые 5 минут архивированные лог файлы .json.gz в указанный S3 bucket.
Для того, чтобы посмотреть логи сначала копируем их на наш компьютер:

`aws s3 sync s3://<bucket-name> .`
 
Появится папка AWSLogs с множеством файлов
 
##Параметры запуска скрипта
 
`python3 aws_read_logs.py --help`
`usage: aws_read_logs.py [-h] [--user USER] [--region REGION] [--ip IP]
                        [--service SERVICE] [--event EVENT] [--id EVENTID]

Read aws logs from .json.gz files

optional arguments:
  -h, --help         show this help message and exit
  --user USER        Filter by USER contains value
  --region REGION    Filter by region contains value
  --ip IP            Filter by IP contains value
  --service SERVICE  Filter by aws service contains value
  --event EVENT      Filter by event name contains value
  --id EVENTID       Filter by exact eventID and show log json`

Например: `python3 aws_read_logs.py --user admin --event changepassword > table.csv`
Для отображения всех записей запускаем без параметров  python3 aws_read_logs.py


При указывании конкретного eventID скрипт выводит json текст найденного события в логах.
Например: `python3 aws_read_logs.py --id=80de7756-ce24-46b6-a9c1-7e38f92f72d0`

Во всех остальных случаях выводится текст в формате csv с разделителем между полями ;

## Дальнейший анализ полученного csv файла

Для GUI систем просто открыть csv файл любой программой, которая поддерживает такой формат.
Например открыть EXCEL, выбрать все данные, установить фильтр и дальше анализировать данные.

Для просмотра в терминале устанавливаем visidata:
`pip3 install visidata`

`vd --csv-delimiter=";" <наш файл>.csv`

## Анализ данных в visidata

Выбираем столбец для фильтрации и/или поиска данных
Для поиска нажимаем  / и текст для поиска
Для перехода к следующему жмем N

Для фильтрации:
Первый вариант:
на необходимом столбце нажимаем shift-F, дальше стрелками вверх вниз выбираем нужное значения для фильтрации и ENTER

Второй вариант:
нажимаем SHIFT |  вводим выражение для поиска , выделяются строки с совпадениями
нажимаем " для отображения только выделенных строк

Для выхода из просмотра жмем q



