---
Author: Дмитрий Казанский
---

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

  >  `"ip : 71.78.22.43` - ошибки синтаксиса: добавить закрывающую кавычку (`"`) для ключа `ip`; положить в кавычки значение этого ключа `"71.78.22.43"`
  >

2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле

```
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

```
> При старте скрипт записывает начальные значения IP сервисов в файлы `serviceList.json`, `serviceList.yaml`;
> Если в процессе работы скрипта IP меняются, то значения в файлах обновляются.
> 
## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

---

[На главную](../README.md)
