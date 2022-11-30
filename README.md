#### Two example Dockerfile

## Dockerfile

```bash
FROM python:3.9-alpine
RUN mkdir /pytest-container
COPY . /pytest-container
WORKDIR /pytest-container
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
```

### Build image:

```bash
docker build -t pytest-image .
```

### Create a container:
```bash
docker run -ti --name pytest-container pytest-image /bin/sh
```
### Run test inside container CLI:
```bash
pytest -s -v test_sample.py
```


# OR

## Dockerfile

```bash
FROM python:3.9-alpine
RUN mkdir /pytest-container
COPY . /pytest-container
WORKDIR /pytest-container
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT pytest -s -v test_sample.py
```

### Build image:

```bash
docker build -t pytest-image .
```

### Create a container:
```bash
docker run -ti --name pytest-container pytest-image
```

#### Run it with docker-compose.yml

##### Run
```bash
docker-compose up
```

##### Down

```bash
docker-compose down --rmi all
```
