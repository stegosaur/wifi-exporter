import time
import argparse
import iwlib
from iwlib import iwlist
import prometheus_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", action="store", dest="port", type=int, default=3012)
parser.add_argument("--polling-interval", action="store", dest="polling_interval", type=int, default=7)
parser.add_argument("--interface", action="store", dest="iface", type=str, default="wlan0")

args = parser.parse_args()

if __name__ == "__main__":
  prometheus_client.start_http_server(args.port)
  print(time.ctime() + " :: starting wifi-exporter, listening on port " + str(args.port) )
  avail = prometheus_client.Gauge("wifi_signal_available", "wifi signal % available for SSID" , ['ssid','freq','ap_mac'])
  in_use = prometheus_client.Gauge("wifi_signal_for_net_in_use", "wifi signal for network currently in use", ['ssid','freq','ap_mac'])
  while True:
    current_net=iwlib.iwconfig.get_iwconfig(args.iface)
    in_use.labels(ssid=str(current_net['ESSID'],'utf-8'),
                  freq=str(current_net['Frequency'],'utf-8'),
                  ap_mac=str(current_net['Access Point'],'utf-8')).set(current_net['stats']['quality'])
    try:
      nets=iwlist.scan(args.iface)
      for net in nets: avail.labels(ssid=str(net['ESSID'],'utf-8'),
                                    freq=str(net['Frequency'],'utf-8'),
                                    ap_mac=str(net['Access Point'],'utf-8')).set(net['stats']['quality'])
    except: print(time.ctime() + " :: wifi scan failure")
    time.sleep(args.polling_interval)# sample element from iwlist.scan(args.iface)
    in_use.clear()

#  {
#    'Mode': b'Master',
#    'ESSID': b'Eagle',
#    'Frequency': b'5.18 GHz',
#    'Key': b'off',
#    'Access Point': b'2A:AA:AA:AA:AA:AA',
#    'BitRate': b'54 Mb/s',
#    'stats': {
#      'quality': 70,
#      'level': 220,
#      'noise': 0,
#      'updated': 75
#    }
