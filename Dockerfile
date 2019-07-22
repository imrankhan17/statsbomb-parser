FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt && \
        pip install codecov pycodestyle pylint pytest pytest-cov httmock twine

CMD ["python"]
