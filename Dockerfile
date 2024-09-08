# syntax=docker/dockerfile:1.0.0-experimental
FROM python:3.10-slim as base_image

# for additional file parsers

# tesseract-ocr \
# tesseract-ocr-jpn \
# libsm6 \
# libxext6 \
# ffmpeg \

RUN apt-get update -qqy && \
    apt-get install -y --no-install-recommends \
      ssh \
      git \
      gcc \
      g++ \
      poppler-utils \
      libpoppler-dev \
      unzip \
      curl \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app

FROM base_image as dev

COPY . /app
RUN pip install --no-cache-dir -e "libs/kotaemon[all]" -e "libs/ktem"
RUN pip install --no-cache-dir langchain-google-genai
RUN pip install --no-cache-dir graphrag future

CMD ["python", "app.py"]
