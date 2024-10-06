#base image
FROM python:3.11-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONUNBUFFERED=1
WORKDIR webproject
ADD . .
RUN pip install -r requirements.txt
#COPY requirements.txt requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
