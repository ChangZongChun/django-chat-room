# Chun's Chat Room

Chun's Chat Room is a website that allows everyone who register an account to discuss any topic in rooms with other users.

## HTTP server - Nginx

1. 編輯 nginx.conf (/etc/nginx/nginx.conf)，  
修改 server 執行時讀取的資料夾

```bash
# include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-available/*;
```

2. 編輯 default.conf (/etc/nginx/sites-available/default.conf)，  

```bash
upstream uwsgi {
    server <wsgi server ip>; # use TCP
    # server unix:/chatroom/app.sock; # for a file socket
}
```
