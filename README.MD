# internet-speed
Python based tool that checks and stores upload and download speeds using speedtest.net script.
Values are written to ThingSpeak.com (default) or local RRD database.
  
## Run
First create conf/private_settings.py according to [conf/private_settings_examle.py](conf/private_settings_examle.py) file with your own api key.
Then adapt [conf/settings.py](conf/settings.py) to your environment.
Finally run [bin/speed.py](bin/speed.py) file to measure transfer and update thingspeak db.

## Note
In [db/](db/) and [www/](www/) you will find files related to RRD database
