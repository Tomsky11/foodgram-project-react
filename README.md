![example workflow](https://github.com/Tomsky11/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Foodgram - «Продуктовый помощник».

При помощи данного сервиса пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.  

## Сайт доступен по адресу

<http://84.201.166.5>

## Авторизационные данные администратора
email: to@mail.ru  
password: spravka_1 

# Запуск проекта локально
Склонируйте проект:  

```https://github.com/Tomsky11/foodgram-project-react```

В директории foodgram-project-react/backend/ cоздайте и заполните файл .env по шаблону:  

```
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=<имя базы данных postgres>  
DB_USER=<пользователь бд>  
DB_PASSWORD=<пароль>  
DB_HOST=db  
DB_PORT=5432
```

Перейдите в папку infra и выполните:  

```docker-compose up -d```

### Настройка
Запустите миграции:  

```sudo docker-compose exec -T backend python manage.py migrate --noinput```

Соберите статику:  

```sudo docker-compose exec -T backend python manage.py collectstatic --noinput```

Загрузите начальные данные со списком ингредиентов:

```sudo docker-compose exec -T backend python manage.py loaddata dump.json```


### Задействованные технологии
* Python 3.8.5
* Django Rest Framework 3.11.0
* Docker
* Nginx
* Postgres
* React
