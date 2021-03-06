FROM python:3.8

RUN pip install pipenv

WORKDIR /code

COPY catalog /code/

RUN pipenv install --system --deploy

CMD ["flask", "run"]