#!/bin/bash
#########################
#   InfluxDB_recovery   #
#                       #
#            2019.8.6   #
#########################

sudo influx -execute 'create database librenms'
sudo influxd restore -portable -db librenms -newdb librenms_bk /home/ntus/environ_backup  #資料倒入臨時資料庫
sudo influx -database librenms_bk -execute 'SELECT * INTO librenms..:MEASUREMENT FROM /.*/ GROUP BY *' #臨時資料庫的資料複製至資料庫
sudo influx -execute 'drop database librenms_bk'

