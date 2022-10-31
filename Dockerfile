FROM python:3
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [“python”, "app.py"]