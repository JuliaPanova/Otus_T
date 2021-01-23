FROM python:3.7.9-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY my_class/pyproject.toml my_class/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY my_class .

EXPOSE 8080

CMD ["python", "main.py"]

