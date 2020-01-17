#!/usr/bin/env python3
import facts
import trivia

# Main:
#    - High level CLI to control whether we quit / call facts / call triva

def main ():

    # Loop forever, because 1 is true
    while 1:

        # Get input from user, assign what they type to the variable "cmd"
        cmd = input ("(f/facts) (t/trivia) (q/quit/stop): ")

        # convert all input to lower, to help minimize what we need to test for
        cmd = cmd.lower()

        # complese if ... elfi to determine what the user entered up above
        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            # user choose to quit, so we break out of while loop, leaving the app
            break
        elif (cmd=="f") or (cmd=="facts"):
            # user choose facts, so call the entrypoint to the facts package
            facts.run_facts()
        elif (cmd=="t") or (cmd=="trivia"):
            # user choose trivia, so call the entrypoint to the triviapackage
            trivia.run_trivia()

# Python entrypoint starts at the following code

if __name__ == '__main__':
    print("Welcome to Sports App")

    # Call the main Command Line Interface (CLI) for our app
    main()
