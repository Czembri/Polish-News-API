FROM python:3.8.3-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","run.py"]