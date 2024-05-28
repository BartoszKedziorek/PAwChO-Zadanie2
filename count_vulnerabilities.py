import subprocess, sys


result = subprocess.check_output('docker scout quickview zadanie2test:latest',
                                  shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT)


#print(result)
result = result.decode('utf-8')
start_index = result.find('Target')
end_index = result.find('What\'s Next?')
print(result[start_index:end_index])
# for line in result.splitlines():
#     print(line)