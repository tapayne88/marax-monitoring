# Mara X Monitoring

![Granfana Preview](./preview.png "Granfana Preview")

Take serial connection from Mara X containing temperature data a persist in a database and expose via grafana.

Docker will persist DB storage using volumes so restarts won't cause data loss.

Tested on a Raspberry Pi.

## How to run

Run grafana / influxDB / ingestion via docker-compose with the following

```shell
[sudo] docker-compose up --build
```

This can now be backgrounded.
