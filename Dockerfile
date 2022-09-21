FROM python:3.6-slim
COPY . /python-test
WORKDIR /python-test
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-v", "--junitxml=reports/result.xml"]
# RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
# COPY /python-test/reports .
# CMD tail -f /dev/null