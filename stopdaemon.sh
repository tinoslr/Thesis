#!/bin/bash

# Überprüfe, ob der Benutzer Root-Rechte hat
if [ "$(id -u)" != "0" ]; then
    echo "Das Skript muss mit Root-Rechten ausgeführt werden. Bitte mit sudo versuchen."
    exit 1
fi

# Suche nach allen Prozessen, die mit 'iperf' verbunden sind, und beende sie
pids=$(pgrep -f "iperf")

if [ -z "$pids" ]; then
    echo "Es wurden keine laufenden iperf-Daemons gefunden."
else
    echo "Beende die folgenden iperf-Daemons: $pids"
    kill -9 $pids
    echo "iperf-Daemons erfolgreich beendet."
fi
