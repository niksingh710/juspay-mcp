FROM python:3.13.2-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup --home /home/appuser appuser

# Create working directory and set permissions
WORKDIR /app
COPY . /app
RUN chown -R appuser:appgroup /app

# Set environment variables for Python and user home
ENV PYTHONUNBUFFERED=1 \
    HOME=/home/appuser

RUN pip install --upgrade pip setuptools wheel

# Switch to non-root user
USER appuser

RUN pip install --no-cache-dir --no-build-isolation . --root-user-action=ignore

ENTRYPOINT ["python", "stdio.py"]
