FROM python:3.9

RUN apt-get update

RUN pip install pipenv

WORKDIR /code


RUN pip3 install -r requirements.txt

CMD ["flask", "run"]