# FROM python:3.6-slim
# COPY . /python-test
# WORKDIR /python-test
# RUN pip install --no-cache-dir -r requirements.txt
# # CMD ["pytest", "-v", "--junitxml=reports/result.xml"]
# # RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
# # COPY /python-test/reports .
# # CMD tail -f /dev/null


FROM python:3.9-alpine
RUN mkdir /pytest-container
COPY . /pytest-container
WORKDIR /pytest-container
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
# ENTRYPOINT pytest -s -v tests/test_sample.py
