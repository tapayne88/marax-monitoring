FROM python:3

WORKDIR /usr/src/app

COPY pi-plotter/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY crontab /etc/cron.d/pi-plotter
RUN chmod 0644 /etc/cron.d/pi-plotter
RUN touch /var/log/cron.log

RUN apt update
RUN apt -y install cron

CMD cron && tail -f /var/log/cron.log
