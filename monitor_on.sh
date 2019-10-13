#!/bin/bash

interface=$1

echo "taking down ${interface}"
ifconfig ${interface} down

#echo "cleaning (airmon-ng check kill)"
#airmon-ng check kill

echo "changing to monitor mode"
iwconfig ${interface} mode monitor

echo "bringing wlano up"
ifconfig ${interface} up

echo "done"


