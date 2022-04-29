import subprocess
import os
import sys

class SM:

    def __init__(self, avail):
        self.m = avail
    
    def __call__(self):
        print("~super simple session manager~")
        for i, (k, v) in enumerate(self.m):
            print(i, k)
        choice = input("choice> ").strip()
        script = self.m[int(choice)][1].split(' ')
        subprocess.run(script)

if __name__ == '__main__':
    avail = [ 
        ['qtile', f'startx /home/{os.getlogin()}/.config/qtile/xinitrc'],
        ['tty',   ''],
    ]
    sm = SM(avail)
    sm()
