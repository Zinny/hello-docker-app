FROM python:3.10-slim

# Install Flask
RUN pip install flask

COPY app.py /app.py

CMD  ["python3", "/app.py"]

EXPOSE 8080
