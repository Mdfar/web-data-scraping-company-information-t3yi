FROM python:3.10-slim

WORKDIR /app COPY . . RUN pip install -r requirements.txt RUN playwright install chromium RUN playwright install-deps

CMD ["python", "main.py"]