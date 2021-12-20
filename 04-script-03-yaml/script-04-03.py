#!/usr/bin/env python3
import socket as sct
import time as tm
import os
import json
import yaml
# Functions services
def sForm(dictData): # restructure data structure
  return [{k:v} for k,v in dictData.items()]
def filesUpdate (hosts): # update service info in files
  with open('serviceList.json', 'w') as srvF:
    json.dump(sForm(hosts), srvF, indent=2)
  with open('serviceList.yaml', 'w') as srvY:
    yaml.dump(sForm(hosts), srvY, default_flow_style=False)
# set variables
i = 0
times = 2
wait = 5
err = 0
hostUrlList = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
filesUpdate(hostUrlList)
print('Список веб-сервисов для проверки: ',hostUrlList)
print(30*'=')
while i < times:
  i += 1
  print('== Номер проверки:', i, 50*'=')
  for hostUrl in hostUrlList:
    ipHostUrl = sct.gethostbyname(hostUrl)
    if ipHostUrl != hostUrlList[hostUrl]:
      print(' [ERROR] ' + str(hostUrl) +' IP mistmatch: '+hostUrlList[hostUrl]+' '+ipHostUrl)
      hostUrlList[hostUrl]=ipHostUrl
      err +=1
    elif ipHostUrl == hostUrlList[hostUrl]:
      print('Ok:' + hostUrl + ' - ' + hostUrlList[hostUrl] )
  if err != 0:
    filesUpdate(hostUrlList)
    print (err + 'IP mistmatch. Service ip list updated')
    err=0
  tm.sleep(wait)
