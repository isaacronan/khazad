FROM python:3
ARG PORT
ENV PORT=${PORT}
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install scipy
RUN pip install flask
RUN pip install gunicorn
CMD gunicorn --bind 0.0.0.0:${PORT} wsgi
