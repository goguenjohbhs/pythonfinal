#!/usr/bin/env python3


def run_facts():
    year=""

    while 1:
        cmd = input ("(l/list) (t/team) (r/results) (y/year) (q/quit/stop): ")
        cmd = cmd.lower()

        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            break
        elif (cmd=="l") or (cmd=="list"):
            print("not yet done")
        elif (cmd=="t") or (cmd=="team"):
            print("not yet done")
        elif (cmd=="r") or (cmd=="results"):
            print("not yet done")
        elif (cmd=="y") or (cmd=="year"):
            print("not yet done")

if __name__ == '__main__':
     run_facts()
