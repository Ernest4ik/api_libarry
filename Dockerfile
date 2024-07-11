FROM python:latest
WORKDIR /app
COPY ./api_library /app/api_library
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn", "api_library.main:app", "--host", "0.0.0.0", "--port", "80"]
