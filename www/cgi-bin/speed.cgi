#!/usr/bin/rrdcgi 
<HTML>
 <HEAD>
    <TITLE>Internet Quality</TITLE>
    <meta name="author" content="Tomasz Ceszke">
 </HEAD>
 <BODY>
 
<!-- ---------------- 24h ----------------- -->
<span>
 <RRD::GRAPH internet-speed/www/speed/chart_speed_24.png  --imginfo '<IMG SRC=/speed/%s WIDTH=%lu HEIGHT=%lu >' -s -24h  -w 1300 -h 200 --lazy --title="Speed: last 24h" -v Mb/s
        DEF:download=internet-speed/db/speed.rrd:download:AVERAGE
        DEF:upload=internet-speed/db/speed.rrd:upload:AVERAGE
        LINE2:download#00a000:download
        LINE2:upload#2E2EFE:upload
 >
</span>

<!-- ---------------- 1 month ------------- -->
<br><br>
<span>
<RRD::GRAPH internet-speed/www/speed/chart_speed.png  --imginfo '<IMG SRC=/speed/%s WIDTH=%lu HEIGHT=%lu >' -w 1300 -h 200 -s -1m  --title="Speed: last month" -v Mb/s
        DEF:download=internet-speed/db/speed.rrd:download:AVERAGE
        DEF:upload=internet-speed/db/speed.rrd:upload:AVERAGE
        AREA:download#00a000:download
        AREA:upload#2E2EFE:upload
 >
</span>

</BODY>
</HTML>
