FROM python:3.6-slim
COPY . /python-test
WORKDIR /python-test
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest"]
# RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
# CMD tail -f /dev/null