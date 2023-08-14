FROM python:3.8.13-slim-buster
WORKDIR /chatroom

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip --no-cache-dir

COPY ./chatroom ./
RUN pip install -r /chatroom/requirements.txt --no-cache-dir

COPY ./docker-compose.yml ./docker-compose.yml

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

CMD ["gunicorn", "--access-logfile", "./access.log", "--bind", "0.0.0.0:8000", "chatroom.wsgi:application" ]
# , "--log-level=debug"
# -c /some/folder/gunicorn.conf.py
# COPY gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# EXPOSE 8000