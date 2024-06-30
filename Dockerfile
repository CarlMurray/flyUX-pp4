FROM python:3.9-alpine
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]