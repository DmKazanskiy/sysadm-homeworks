#!/usr/bin/env python3
import os
#bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
bash_command = ["cd ~/GIT/sysadm-homeworks", "echo 'Проверка изменений репозитория:'","pwd"]
print(os.popen(' && '.join(bash_command)).read())
bash_command = ["cd ~/GIT/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False
for result in result_os.split('\n'):
    if (result.find('изменено') != -1 or result.find('modified') != -1):
        prepare_result = result.replace('\tизменено:   ', '').replace('\tmodified:   ', '')
        print('',prepare_result)
#       break