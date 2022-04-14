import subprocess
import os
import sys

class SM:

    def __init__(self, avail):
        self.m = avail
        self.idxs, self.names = self.avail_table()
        
    def avail_table(self):
        idx, name = [], []
        for i, k in enumerate(self.m.keys()):
            idx.append(i)
            name.append(k)
        return idx, name

    def show_table(self):
        print("Session Manager:")
        print("========")
        for t in range(len(self.idxs)):
            i = self.idxs[t]
            n = self.names[t]
            print(f"{i}: {n}")
        print("========")

    def prompt_response(self):
        kbd = input("startx> ").strip()
        if kbd == "q":
            sys.exit(0)
        return kbd

    def get_response_session(self, kbd):
        kbd = int(kbd)
        name = self.names[kbd]
        xfname = os.path.join(self.m[name], "xinitrc")
        xfname = os.path.expanduser(xfname)
        return xfname

    def run_response_session(self, xfname):
        cmd = f"startx {xfname}"
        subprocess.run(["startx", xfname])

    def sm(self):
        self.show_table()
        kbd = self.prompt_response()
        xfname = self.get_response_session(kbd)
        self.run_response_session(xfname)

if __name__ == '__main__':
    avail = {
        'qtile': '~/.config/qtile',
    }
    sm = SM(avail)
    sm.sm()

