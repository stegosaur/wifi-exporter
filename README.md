# wifi-exporter
prometheus exporter for wifi signal

usage: `python3 exporter.py --port <port> --polling-interval <time>`
  
arguments are optional. default value for port is 3012, default value for polling interval is 7 sec

sample output:
  
```
# HELP max_wifi_signal_available wifi max signal % available for SSID
# TYPE max_wifi_signal_available gauge
max_wifi_signal_available{ssid="Eagle"} 69.0
max_wifi_signal_available{ssid="WMST-Lab 2.4"} 97.0
max_wifi_signal_available{ssid="HEATKTE-LAB"} 79.0
max_wifi_signal_available{ssid="WMST-Lab 5"} 84.0
max_wifi_signal_available{ssid=""} 82.0
max_wifi_signal_available{ssid="55_WEST"} 79.0
max_wifi_signal_available{ssid="Hopper-Lab"} 72.0
max_wifi_signal_available{ssid="Walmartwifi"} 70.0
max_wifi_signal_available{ssid="Walmartwifi_2.4"} 72.0
max_wifi_signal_available{ssid="Zebra-SE"} 62.0
max_wifi_signal_available{ssid="ZScan"} 59.0
max_wifi_signal_available{ssid="ZWireless"} 64.0
max_wifi_signal_available{ssid="ZCorp"} 64.0
max_wifi_signal_available{ssid="ZGuest"} 64.0
max_wifi_signal_available{ssid="AITTest"} 64.0
max_wifi_signal_available{ssid="Bosch 9E-9F-10"} 54.0
max_wifi_signal_available{ssid="Bosch 9E-A2-0C"} 49.0
max_wifi_signal_available{ssid="APTESTWPA"} 70.0
# HELP wifi_signal_for_net_in_use wifi signal for network currently in use
# TYPE wifi_signal_for_net_in_use gauge
wifi_signal_for_net_in_use{ssid="Eagle"} 66.0
```
