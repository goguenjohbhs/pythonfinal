#!/usr/bin/env python3

def main ():

    while 1:
        cmd = input ("(f/facts) (t/trivia) (q/quit/stop): ")
        cmd = cmd.lower()

        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            break


if __name__ == '__main__':
    print("Welcome to Sports App")
    main()
