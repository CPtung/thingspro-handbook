while true;do

val=`cat /proc/loadavg | cut -f1 -d" "`
echo $val
curl -i -XPOST 'http://localhost:8086/write?db=statsdemo' --data-binary 'cpu,host=serverA value='$val







sleep 5
done
