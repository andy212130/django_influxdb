#!/bin/bash
#######################
#   InfluxDB_backup   #
#		      #
#          2019.8.6   #
#######################

sudo influxd backup -portable ./environ_backup 
sudo influxd backup -portable -database librenms ./environ_backup

sudo scp -r environ_backup ntus@10.20.30.47:/home/ntus/
