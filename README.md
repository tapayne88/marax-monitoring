# Mara X Monitoring

Store Marax temperature data in DB and expose via grafana. Also plot temperature on inky wHAT display.

Generated mock data from [mockaroo](https://www.mockaroo.com) with the help of this [reddit post](https://www.reddit.com/r/espresso/comments/hft5zv/data_visualisation_lelit_marax_mod/)

## How to run

Run grafana / influx / ingestion via docker-compose with the following

```shell
[sudo] docker-compose up --build
```
