FROM python:3.8.13-slim-buster
WORKDIR /chatroom
COPY ./chatroom ./
COPY ./chatroom/entrypoint.sh ./entrypoint.sh

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /chatroom/requirements.txt --no-cache-dir
# COPY gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000" , "chatroom.wsgi:application"]