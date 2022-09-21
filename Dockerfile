FROM python:3.8

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD . /app/
WORKDIR /app

ENTRYPOINT ["python", "-m", "pytest", "-v", "--junit-xml", "tests/*"]