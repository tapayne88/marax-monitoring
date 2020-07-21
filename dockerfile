FROM python:3

WORKDIR /usr/src/app

COPY pi-plotter .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./plot_temperature.py" ]
