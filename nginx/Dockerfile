FROM nginx:1.19.0-alpine
COPY ./default.conf /etc/nginx/sites-avaliable/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]