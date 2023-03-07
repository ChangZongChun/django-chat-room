FROM python:3.8.13-slim-buster
WORKDIR /chatroom
COPY ./chatroom ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /chatroom/requirements.txt --no-cache-dir

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "chatroom.wsgi:application", "--bind", "0.0.0.0:8000"]