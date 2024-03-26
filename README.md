# Unofficial vpngate telegram bot

Get access to first `vpngate.net` 60 servers sorted by score. \
This code comes with absolutely no warranty. \
For connection guide visit [vpngate](https://vpngate.net) . \
Loging and password for connection are `vpn`. 

For deploying a service you can either do:
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install .
export TELEGRAM_TOKEN=<YOUR BOT TOKEN>
open-gate
```

or you can install an app and put a systemd service file into `/etc/systed/system/`
And then 
```shell
systemctl enable opengate-bot.service
systemctl start opengate-bot.service
```
Don't forget to change path to `open-gate` in the service file and add env variable with a token.
