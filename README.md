# Container Security Reference Solution Demo.
> ONUG Security Group reference solution demo for Onug Digital Live.


Componnets: 

Supervisor Binary
Open Policy Agent
Lambda Backend

## Installation

OS X & Linux:

 
```sh
sudo supervisor start  --network-args "portmap=8000:80/tcp" /home/ubuntu/nginx.sif --instancename web1
```



## Development setup

Install [OPA](https://www.openpolicyagent.org/)  and [Singularity](https://singularity.lbl.gov/) 

Copy the supervisor to /usr/bin/share and ensure it exists on the path variable.
```sh
chmod +x supervisor
cp supervisor /urs/bin/share
```

## Issues

If you face any issues during installation, please create a Github issue on the [Github Issues](https://github.com/onug/Security/issues)
