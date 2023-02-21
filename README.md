# api_final_yatube
<h1 align="center"><img src="https://trudvsem.ru/information/resources/upload/opendata/api/apigif_redesign.gif" height="300" width = "400"/></h1>

## Описание проекта:
Данный проект представляет собой backend часть социальной платформы yatube. В ней реализована api для взаимодействия с frontend частью проекта.
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:KirillBalezin/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```