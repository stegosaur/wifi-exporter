# wifi-exporter
prometheus exporter for wifi signal

usage: `python3 exporter.py --port <port> --polling-interval <time> --interface <interface>`

arguments are optional. default value for port is 3012, default value for polling interval is 7 sec, default interface is wlan0

within docker, the arguments --net="host" need to be added to expose the wireless interface to the container

sample output:
  
```
# HELP wifi_signal_available wifi max signal % available for SSID
# TYPE wifi_signal_available gauge
wifi_signal_available{ap_mac="2A:3F:1B:EB:9E:8A",freq="5.18 GHz",ssid="Eagle"} 69.0
wifi_signal_available{ap_mac="26:5A:4C:96:B8:7A",freq="2.437 GHz",ssid="Puzila Home 2g"} 58.0
wifi_signal_available{ap_mac="F0:9F:C2:DD:5E:76",freq="2.437 GHz",ssid="Puzila Guest"} 59.0
wifi_signal_available{ap_mac="24:5A:4C:86:B8:7A",freq="2.437 GHz",ssid="Puzila Guest"} 59.0
wifi_signal_available{ap_mac="F6:9F:C2:DD:5E:76",freq="2.437 GHz",ssid="Puzila Home 2g"} 58.0
wifi_signal_available{ap_mac="FA:9F:C2:DD:5E:76",freq="2.437 GHz",ssid=""} 62.0
wifi_signal_available{ap_mac="F6:9F:C2:DE:5E:76",freq="5.22 GHz",ssid="Puzila Home"} 39.0
wifi_signal_available{ap_mac="26:5A:4C:A6:B8:7B",freq="5.22 GHz",ssid="Puzila Guest"} 70.0
wifi_signal_available{ap_mac="26:5A:4C:96:B8:7B",freq="5.22 GHz",ssid="Puzila Home"} 70.0
wifi_signal_available{ap_mac="04:A2:22:B1:7B:CF",freq="2.412 GHz",ssid="OliviaWifi"} 33.0
wifi_signal_available{ap_mac="34:98:B5:5E:67:D7",freq="2.422 GHz",ssid="DylanVictoria"} 36.0
wifi_signal_available{ap_mac="7A:45:58:1D:6A:25",freq="2.437 GHz",ssid="Puzila Home 2g"} 46.0
wifi_signal_available{ap_mac="7A:45:58:2D:6A:25",freq="2.437 GHz",ssid=""} 48.0
wifi_signal_available{ap_mac="90:9A:4A:47:6B:A4",freq="2.452 GHz",ssid="TP-Link_6BA5"} 61.0
wifi_signal_available{ap_mac="78:45:58:4D:6A:26",freq="5.2 GHz",ssid="Puzila Home"} 35.0
wifi_signal_available{ap_mac="7A:45:58:1D:6A:26",freq="5.2 GHz",ssid="Puzila Guest"} 35.0
wifi_signal_available{ap_mac="FA:9F:C2:DE:5E:76",freq="5.22 GHz",ssid="Puzila Guest"} 39.0
wifi_signal_available{ap_mac="26:5A:4C:B6:B8:7B",freq="5.22 GHz",ssid=""} 31.0
wifi_signal_available{ap_mac="90:9A:4A:47:6B:A3",freq="5.745 GHz",ssid="TP-Link_6BA5_5G_2"} 44.0
wifi_signal_available{ap_mac="80:2A:A8:52:1E:FC",freq="5.745 GHz",ssid="Puzila Home"} 40.0
wifi_signal_available{ap_mac="86:2A:A8:52:1E:FC",freq="5.745 GHz",ssid="Puzila Guest"} 39.0
wifi_signal_available{ap_mac="04:A2:22:B1:7B:D0",freq="5.805 GHz",ssid="OliviaWifi"} 31.0
wifi_signal_available{ap_mac="6A:A2:22:B1:7B:D1",freq="5.805 GHz",ssid=""} 31.0
wifi_signal_available{ap_mac="8A:2A:A8:51:1E:FC",freq="2.412 GHz",ssid=""} 38.0
wifi_signal_available{ap_mac="78:45:58:4D:6A:25",freq="2.437 GHz",ssid="Puzila Guest"} 47.0
wifi_signal_available{ap_mac="90:9A:4A:47:6B:A2",freq="5.22 GHz",ssid="TP-Link_6BA5_5G_1"} 43.0
wifi_signal_available{ap_mac="24:5A:4C:86:B8:7B",freq="5.22 GHz",ssid=""} 31.0
# HELP wifi_signal_for_net_in_use wifi signal for network currently in use
# TYPE wifi_signal_for_net_in_use gauge
wifi_signal_for_net_in_use{ap_mac="2A:3F:1B:EB:9E:8A",freq="5.18 GHz",ssid="Eagle"} 70.0
```
