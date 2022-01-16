# Mara X Monitoring

![Granfana Preview](./preview.png "Granfana Preview")

Kubernetes-based InfluxDB and Grafana Deployment that ingests and graphs metrics pushed from [marax-telegraf-agent](https://github.com/laebshade/marax-telegraf-agent) docker container running on Raspberry Pi Zero 2 W.

All credit to the author of this [post](https://www.reddit.com/r/espresso/comments/hft5zv/data_visualisation_lelit_marax_mod/) for doing so much of the ground work!

## How to run

Apply all files to your Kubernetes cluster:

```shell
cat *.yaml | kubectl apply -f -
```


## What do I need?

- Lelit Mara X PL62 espresso machine ([link](https://marax.lelit.com/index-eng.html))
- Serial to USB cable ([link](https://www.amazon.co.uk/gp/product/B01N4X3BJB/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1))
- https://github.com/bitnami-labs/sealed-secrets and updating the relevant sealed secrets manifests.
- Computer capable of running linux & Docker, like a Raspberry Pi ([link](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/))
- Kubernetes cluster on your LAN to run InfluxDB and Grafana