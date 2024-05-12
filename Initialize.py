from os import system
import subprocess

def fix_win32():

    cmd1 = ['python', '-m', 'win32api']
    cmd2 = ['python', 'venv\Scripts\pywin32_postinstall.py', '-install']

    r = subprocess.call(cmd1, shell=True)

    if r:

        r2 = subprocess.call(cmd2, shell=True)

        if not r2:
            print('[*] Initialize.py successful')
        else:
            print('[!] Initialize.py failed')
    
    exit()
            
if __name__ == '__main__':

    fix_win32()
