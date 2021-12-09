FROM ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]