# Google Cloud Platform DNS updater

This package updates a DNS zone hosted on Google Cloud DNS to the IP addresses of the local
machine as visible from the internet using https://ifconfig.co/.

This script can be run in a cron job to periodically update DNS records of a GCP project on
connections without a static IP assigned. Supports IPv4 and IPv6.

## Installation
```shell script
pip install -U git+https://github.com/jasonrig/gcloud-dyndns.git
```

## Usage
```
$ update-gcloud-dns -h
usage: update-gcloud-dns [-h] [--ttl TTL] [--project_id PROJECT_ID]
                         [--force_update]
                         zone_name dns_name

positional arguments:
  zone_name             the name of the GCP zone to manage
  dns_name              the DNS name to update

optional arguments:
  -h, --help            show this help message and exit
  --ttl TTL             TTL of the update record
  --project_id PROJECT_ID
                        name of the GCP project
  --force_update        force the DNS update even if the record hasn't changed
```

### Example:
```shell script
update-gcloud-dns --project_id some-gcp-project-195432 mydnszone test.mydnszone.com
```