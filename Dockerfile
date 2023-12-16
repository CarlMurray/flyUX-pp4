FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN chmod +x /app/entrypoint.sh
#RUN python manage.py makemigrations
#RUN python manage.py loaddata /app/fixtures/airports.json /app/fixtures/aircraft.json 
# /app/fixtures/flights.json 
EXPOSE 8500
#ENV AWS_ACCESS_KEY_ID=
#ENV AWS_SECRET_ACCESS_KEY=
#ENV AWS_STORAGE_BUCKET_NAME=
ENV DATABASE_URL=postgresql://postgres:postgres@db.local:5432/flyuxdb?sslmode=disable
ENV DEBUG=FALSE
ENV DISABLE_COLLECTSTATIC=0
ENV HOST=db.local
ENV NAME=flyuxdb
ENV PASSWORD=postgres
ENV PORT=5432
ENV SECRET_KEY=django-insecure-hl+argx+#jcd+lk@$wr63a6rsxypha&6asnx$h6t6i24ek_jlk
ENV USER=postgres
ENV USE_S3=FALSE
ENTRYPOINT ["/app/entrypoint.sh"]

