FROM python:3.13.2-slim

WORKDIR /app

RUN pip install --upgrade pip \
 && pip install setuptools wheel

COPY . /app

RUN pip install --no-cache-dir --no-build-isolation . --root-user-action=ignore

ENV JUSPAY_MCP_TYPE="DASHBOARD"
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "stdio.py"]
