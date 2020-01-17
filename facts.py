#!/usr/bin/env python3

from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule
from sportsreference.nfl.roster import Roster

def list_team_names(my_year):

    # if you give an unknown year or team it will go to the except block which prints out no data for that year
    # then return to the main page in this code
    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    # walk through each team and print out just the long name and the abbreviated name
    for team in allTeams:
        print("%-22s %-3s" % (team.name, team.abbreviation))

def display_teams(my_year):
    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    # Let's sort the list of teams by wins in ascending order
    # The build-in python sorted function takes two parameters
    #    - the list "allTeams" which was return from call to Teams above
    #    - the key, which is a small function (lambda) which just returns what we are sorting on "team.wins"
    sortedTeams = sorted(allTeams, key=lambda team: team.wins)

    # walk through each team and print out more information
    for team in sortedTeams:
        print("%-20s %-11s Won: %2d Lost: %2d pts+: %-3d pts-: %-3d ptdiff: %-4d" %
        (team.name,
         team.abbreviation,
         team.wins,
         team.losses,
         team.points_for,
         team.points_against,
         team.points_difference))

def display_results(my_year):

    # stores the abbreviated names in a dictionary which converts abbr names to full name
    abbrevName2Name = {}

    allTeams = Teams(year=my_year)

    # walk through all the teams, saving a dictionary of abbrev name to actual team name
    for team in allTeams:
        abbrevName2Name[team.abbreviation] = team.name

    # Loop forever
    while 1:
        name = input("Team Name (l/list/q/quit/stop): ")

        # this time we convert to UPPER, because we need abbreviated name in UpperCase
        name = name.upper()

        if (name== "") or (name== "Q") or (name== "QUIT") or (name== "STOP"):
            break

        if (name== "L") or (name=="LIST"):
            list_team_names(my_year)
            # "continue" goes back up to run the while loop again
            continue

        try:
            allgames = Schedule(name, year=my_year)
        except:
            print("This is an unknown team or an unavaliable year")
            # "continue" goes back up to run the while loop again
            continue

        teamName = abbrevName2Name[name]
        won = 0
        lost = 0
        tie = 0

        # Walk through all the the games, keeping track of
        #    - number of wins
        #    - number of losses
        #    - number of ties
        # And print out each games result to the user
        
        for game in allgames:
            # if points_allowed is equal "None", then there are no more valid games in this list
            if game.points_allowed is None:
                break

            oppAbbr = game.opponent_abbr.upper()
            oppName = abbrevName2Name[oppAbbr]

            if game.result is None:
                result = "Not Played"
            else:
                result = game.result

            if game.points_scored > game.points_allowed:
                won = won + 1
            elif game.points_scored < game.points_allowed:
                lost = lost + 1
            elif game.points_scored == game.points_allowed:
                tie = tie + 1

            print("%s %4s vs %24s %2d to %2d (%s)"%
                (teamName,
                result,
                oppName,
                game.points_scored,
                game.points_allowed,
                game.type))

        print("Record: Wins: %d Loss: %d Ties: %d" % (won,lost,tie))


def display_players(my_year):

    while 1:
        name = input("Team Name (l/list/q/quit/stop): ")
        name = name.upper()

        if (name == "") or (name == "Q") or (name == "QUIT") or (name == "STOP"):
            break

        if (name == "L") or (name == "LIST"):
            list_team_names(my_year)
            continue

        print("Getting Roster for %s, year %s" % (name, my_year))

        # only get roster is not same as last one

        try:
            roster = Roster(name, year=my_year)
            lastAbbrevName = name
        except:
            print("Unknown Team Name Abbreviations, use list to display Team and Abbreviations")
            continue

        for player in roster.players:
            print("Name: %-30s Weight: %-4s Height: %-3s" % (player.name, player.weight, player.height))



# Main function for the facts CLI
#     - Basically run another while loop for this module commands

def run_facts():
    year=""

    # Loop forever, because 1 is true
    while 1:

        # Get input from user, assign what they type to the variable "cmd"
        cmd = input ("(l/list) (t/team) (p/player) (r/results) (y/year) (q/quit/stop): ")

        # convert all input to lower, to help minimize what we need to test for
        cmd = cmd.lower()

        # complese if ... elfi to determine what the user entered up above
        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            # user wants to quit, break, then return from function to main cli
            break
        elif (cmd=="l") or (cmd=="list"):
             list_team_names(year)
        elif (cmd=="t") or (cmd=="team"): 
            display_teams(year)
        elif (cmd=="r") or (cmd=="results"):
             display_results(year)
        elif (cmd=="y") or (cmd=="year"):
            year = input("year : ")
        elif (cmd=="p") or (cmd=="player"):
             display_players(year)

# Python entrypoint if we just want to run facts.py alone
if __name__ == '__main__':
     run_facts()
