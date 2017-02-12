# internet-speed
Python based tool that checks and stores upload and download speeds using speedtest.net script.
Values are written to ThingSpeak.com (default) or local RRD database.
  
## Run
* create conf/private_settings.py according to [conf/private_settings_example.py](conf/private_settings_example.py) file with your own api key
* adapt [conf/settings.py](conf/settings.py) to your environment
* finally run [bin/speed.py](bin/speed.py) file to measure transfer and update thingspeak db

## Note
In [db/](db/) and [www/](www/) you will find files related to RRD database

## Technology stack
* python
* bash
* rest
* rrd


