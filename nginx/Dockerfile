FROM nginx:1.19.0-alpine
# FROM nginx:latest

# RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./default.conf /etc/nginx/sites-avaliable/default.conf

RUN mkdir -p /etc/nginx/sites-enabled/ \
    && ln -s /etc/nginx/sites-avaliable/default.conf /etc/nginx/sites-enabled/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]