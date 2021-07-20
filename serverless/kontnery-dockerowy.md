Skrypt Lambdy (app.py):
```
from datetime import date 
from datetime import datetime 
import json

def handler(event, context):

  year = event["year"]
  month = event["month"]
  day = event["day"]

  birth_date = datetime.strptime(year+"-"+month+"-"+day, "%Y-%m-%d")

  birth_date = date(int(year), int(month), int(day))
  today_date = date.today()
  number_days = today_date - birth_date

  return {
    'statusCode': 200,
    'body': json.dumps('You were born ' + str(number_days.days) + ' days ago!')
  }
```

Skrypt Dockerfile:
```
# Define function directory
ARG FUNCTION_DIR="/app"

FROM python:buster as build-image

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code
COPY app/* ${FUNCTION_DIR}

# Install the runtime interface client
RUN pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric

# Multi-stage build: grab a fresh copy of the base image
FROM python:buster

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]
```