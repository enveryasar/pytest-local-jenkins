FROM python:3.9-alpine
RUN mkdir /pytest-container
COPY . /pytest-container
WORKDIR /pytest-container
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
# ENTRYPOINT pytest -s -v tests/test_sample.py
