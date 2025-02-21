FROM python:3.9

ADD main.py . 

RUN pip install requests flask

CMD ["python", "./main.py"]