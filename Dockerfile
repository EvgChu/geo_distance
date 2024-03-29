FROM python:3.9
COPY . .

RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5000

CMD ["run.sh"]