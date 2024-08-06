FROM python:3.10

RUN pip install uv

WORKDIR /app

RUN uv venv 
ENV PATH="/app/.venv/bin:$PATH"

COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt

COPY myproject /app/myproject
COPY user /app/user
COPY link /app/link
COPY manage.py /app/manage.py
COPY Procfile /app/Procfile
COPY decorators.py /app/decorators.py
COPY .env /app/.env

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

