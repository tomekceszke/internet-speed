#!/bin/sh

#mv speed.rrd speed.rrd.old &&

rrdtool create speed.rrd \
	--start N \
	--step 3600 \
DS:download:GAUGE:7200:0:U \
DS:upload:GAUGE:7200:0:U \
RRA:AVERAGE:0.5:1:8760

chmod 777 speed.rrd
