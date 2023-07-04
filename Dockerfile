# Pull official latest Python Docker image (Pulished with version 3.11.0)
FROM --platform=linux/amd64 python:3.10

# Set up Python behaviour
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Switch on virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y apt-transport-https \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip

COPY src/requirements.txt ./

RUN pip3 install -r requirements.txt

# Copy all files
WORKDIR /opt

COPY . .

WORKDIR /opt/src

# Start up the app server
CMD python main.py