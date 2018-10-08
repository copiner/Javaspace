
#only works on Unix/Linux/Mac
import subprocess

print('$ francis www.python.org')
r = subprocess.call(['francis','www.python.org'])
print('Exit code:', r)

#communciate()
