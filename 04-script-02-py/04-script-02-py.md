---
Author: Дмитрий Казанский
---

# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательные задания

1. Есть скрипт:
	```python
    #!/usr/bin/env python3
	a = 1
	b = '2'
	c = a + b
	```
	* Какое значение будет присвоено переменной c: Ошибка `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
	* Как получить для переменной c значение 12 : `c=int(str(a)+b)`
	* Как получить для переменной c значение 3: `c=c=a+int(b)`

2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя 

	```python
    #!/usr/bin/env python3

    import os

	bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
	result_os = os.popen(' && '.join(bash_command)).read()
    #is_change = False
	for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
    #       break

	```
> Закоментил строки `#is_change = False` и `#       break`

3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями:

	```python
    #!/usr/bin/env python3

    import os
	import sys
	cmd = os.getcwd()
	if len(sysy.argv) >= 2:
		cmdArg = sys.argv[1]
	bash_command = ["cd "+cmdArg, "git status"]
	result_os = os.popen(' && '.join(bash_command)).read()
    #is_change = False
	for result in result_os.split('\n'):
		if result.find('fatal') != -1:
			print('В каталоге нет репозиториев GIT')
        elif result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
    #       break
		

	```
	>  Добавил в скрипт функцию получения аргументов из командной строки (бибилиотека `sys`)
	>  
	
4. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.

```
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
 print(hostUrlList[hostUrl] + ' - ' + ipHostUrl)  
  tm.sleep(wait)
  
```

[На главную](../README.md)

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так получилось, что мы очень часто вносим правки в конфигурацию своей системы прямо на сервере. Но так как вся наша команда разработки держит файлы конфигурации в github и пользуется gitflow, то нам приходится каждый раз переносить архив с нашими изменениями с сервера на наш локальный компьютер, формировать новую ветку, коммитить в неё изменения, создавать pull request (PR) и только после выполнения Merge мы наконец можем официально подтвердить, что новая конфигурация применена. Мы хотим максимально автоматизировать всю цепочку действий. Для этого нам нужно написать скрипт, который будет в директории с локальным репозиторием обращаться по API к github, создавать PR для вливания текущей выбранной ветки в master с сообщением, которое мы вписываем в первый параметр при обращении к py-файлу (сообщение не может быть пустым). При желании, можно добавить к указанному функционалу создание новой ветки, commit и push в неё изменений конфигурации. С директорией локального репозитория можно делать всё, что угодно. Также, принимаем во внимание, что Merge Conflict у нас отсутствуют и их точно не будет при push, как в свою ветку, так и при слиянии в master. Важно получить конечный результат с созданным PR, в котором применяются наши изменения. 
