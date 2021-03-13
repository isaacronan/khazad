FROM python:3
ARG PORT=2941
ENV PORT=${PORT}
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
CMD gunicorn --bind 0.0.0.0:${PORT} wsgi