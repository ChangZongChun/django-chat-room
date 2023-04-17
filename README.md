# Chun's Chat Room

[Chun's Chat Room](http://18.183.74.175) is a website that allows everyone who register an account to discuss any topic in rooms with other users.

## Installation
Clone the repository  
```bash
git clone https://github.com/ChangZongChun/django-chat-room.git
```
Move into the directory  
```bash
cd chatroom
```
Edit nginx configuration:  
1. 編輯 nginx.conf (/etc/nginx/nginx.conf)，修改 server 執行時讀取的資料夾

```bash
# include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-available/*;
```

2. 編輯 default.conf (/etc/nginx/sites-available/default.conf)  

```bash
upstream uwsgi {
    server <wsgi server ip>; # use TCP
    # server unix:/chatroom/app.sock; # for a file socket
}
```
Docker-compose
```bash
docker-compose up
```  

Get in (Django+Gunicorn) container
```bash
docker exec -it <Container ID> bash
```

Collect static files into /chatroom/staticfiles/
```bash
python manage.py makemigrations musics
python manage.py migrate
python manage.py collectstatic
```
(https://github.com/ChangZongChun/django-chat-room/blob/53b19cc96ee7bd646a28729676e44c261eef0359/app_basic_structure_small.jpg)
