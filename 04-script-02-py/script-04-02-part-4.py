#!/usr/bin/env python3
import socket as sct
import time as tm
# set variables
i = 0
times = 5
wait = 5
hostUrlList = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
print('Список веб-сервисов для проверки: ',hostUrlList)
while i < times:
  i += 1
  print('== Номер проверки:', i, 50*'=')
  for hostUrl in hostUrlList:
    ipHostUrl = sct.gethostbyname(hostUrl)
    if ipHostUrl != hostUrlList[hostUrl]:
      print(' [ERROR] ' + str(hostUrl) +' IP mistmatch: '+hostUrlList[hostUrl]+' '+ipHostUrl)
      hostUrlList[hostUrl]=ipHostUrl
    elif ipHostUrl == hostUrlList[hostUrl]:
      print(hostUrl + ' - ' + hostUrlList[hostUrl])
  tm.sleep(wait)
