import psutil
import os
import sys
import subprocess


path_process = input('input path_process: ')
delay = int(input('input delay: '))
process_name = path_process.split('\\')[-1]
print(process_name)

subprocess.Popen(path_process)
process_name = path_process.split('/')[-1]
try:
    for i in psutil.process_iter():
        if i.name() == process_name:
            with open('log_file.txt', 'a') as f:
                while True:
                    f.write(f'cpu: {i.cpu_percent()}\n')
                    print(f'cpu: {i.cpu_percent()}')
                    f.write(f'Resident Set Size: {i.memory_full_info()[0]}\n')
                    print(f'Resident Set Size: {i.memory_full_info()[0]}')
                    f.write(f'Virtual Memory Size: {i.memory_full_info()[1]}\n')
                    print(f'Virtual Memory Size: {i.memory_full_info()[1]}')
                    f.write(f'File Descriptors: {i.num_fds()}\n')
                    print(f'File Descriptors: {i.num_fds()}')
                    time.sleep(delay)
except:
    pass