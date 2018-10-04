#Football menu system
from commonFunctions import is_number
from football import *
import pprint

__author__ = "David Bristoll"
__copyright__ = "Copyright 2018, David Bristoll"
__maintainer__ = "David Bristoll"
__email__ = "david.bristoll@gmail.com"
__status__ = "Development"

predictions = []

# temporary, placeholder functions:
def download_fixtures(x):
    print("\nThe download fixtures feature is not yet available.\n")


def display_fixtures(x):
    print("\nThe display fixtures feature is not yet available.\n")


def analyse_fixtures(x):
    print("\nThe analyse fixtures feature is not yet available.\n")


def display_analysis(x):
    print("\nThe display analysis feature is not yet available.\n")


def single_game_analysis(x):
    print("\nThe single game analysis feature is not yet available.\n")


def leave(x):
    print("\nExit to previous menu.\n")


def choose_leagues(league_data):
    league_data = select_league(league_data)


def display_selected_leagues(league_data):
    pprint.pprint(league_data)


def display_predictions(predictions):
    """
    Takes in the current list of predictions generated via game analysis options.
    Displays the predictions on screen.
    """

    if not predictions:
        print("\nNo predictions to display. Run manual game analysis and select games to predict first.")

        print("\nPress enter to return to previous menu.")
        input()
        return
    else:
        print("\nPredictions")
        print("===========\n")
        for game in predictions:
            print(game[0], game[1], game[2], game[3])
        print("\nPress enter to return to previous menu.\n")
        input()
        return

def reports(league_data, predictions):
    print("\nReports Menu")
    print("============")
    
    report_options = [["(1) Export JSON data", "1"],
                      ["(2) Display currently loaded league data", "2"],
                      ["(3) Display predictions", "3"],
                      ["(M) Return to previous menu", "m"]
                      ]
    
    exit_menu = False
    available_options = []
    selection = ""
    
    # Gather a list of available_option numbers for input recognition

    for option in report_options:
        available_options.append(option[1])
    
    while not exit_menu:
        
        selected_leagues = []
        
        for option in report_options:
            print(option[0])
            
        while selection not in available_options:
            selection = input()
            selection = selection.lower()
        
        # Menu selection conditionals
        if selection.lower() == "m":
                exit_menu = True
                return league_data
        if selection == report_options[0][1]:
            export_json_file(league_data)
        if selection == report_options[1][1]:
            display_selected_leagues(league_data)
        if selection == report_options[2][1]:
            display_predictions(predictions)
        selection = ""


def football_menu(league_data):
    football_options = [["(1) Select a league", "1", choose_leagues],  # The selectLeague function from football.py
                        ["(2) Download upcoming fixtures*", "2", download_fixtures],
                        ["(3) Display upcoming fixtures*", "3", display_fixtures],
                        ["(4) Run analytics on upcoming fixtures*", "4", analyse_fixtures],
                        ["(5) Display analytics in upcoming fixtures*", "5", display_analysis],
                        ["(6) Single game analysis from fixture list*", "6", single_game_analysis],
                        ["(7) Manual single game analysis", "7", manual_game_analysis],
                        ["(8) Reports", "8", reports],
                        ["(9) Import data from JSON file", "9"],
                        ["(10) Clear currently loaded league data", "10"],
                        ["(11) Clear currently stored prediction data", "11"],
                        ["(M) Previous menu", "m", leave]
                        ]
    selected_leagues = []
    exit_menu = False
    available_options = []
    selection = ""

    # Gather a list of availableOption numbers for input recognition
    for option in football_options:
        available_options.append(option[1])
    
    while not exit_menu:
        if league_data == {}:
            football_options[0][0] = "(1) Select a league"
        else:
            football_options[0][0] = "(1) Select another league"
        
        selected_leagues = []

        #  If there are leagues selected in LeagueData, add them to the selectedLeagues
        #  list and display the list.
        if league_data != {}:
            for league in league_data:
                selected_leagues.append(league)
            print("\n Selected league(s):\n")
            for league in selected_leagues:

                print(league)
            print()
        else:
            print("\nNo league currently selected. Please start by selecting a league.\n")

        # Display the available options 
        for option in football_options:
            print(option[0])
            
        # Display any additional information
        print("\nItems marked with a * are not available in this version.")

        # Keep asking for a selection while the selection provided is not in the availableOptions list.
        while selection not in available_options:
            selection = input()
            selection = selection.lower()

        # If the selection is in the list, run it's function passing
        #the leagueData dictionary by default.
        for option in football_options:
            if selection.lower() == "m":
                exit_menu = True
                break
            if selection == "7":
                exit_manual_analysis_menu = False
                while not exit_manual_analysis_menu:
                    another_game = ""
                    new_prediction = []
                    new_prediction = manual_game_analysis(league_data)
                    if not new_prediction:
                        selection = ""
                        break
                    if new_prediction != "" and new_prediction != []:
                        if new_prediction not in predictions:
                            predictions.append(new_prediction)
                            selection = ""
                        else:
                            print("\nThis prediction is already in the predictions list.")
                        while another_game.lower() != "y" and another_game.lower() != "n":
                            print("\nAnalyse another game? (Y/N)")
                            another_game = input()
                            if another_game.lower() == "n":
                                exit_manual_analysis_menu = True
                                break
                            if another_game.lower() == "y":
                                break           
                continue     
            if selection == "8":
                reports(league_data, predictions)
                selection = ""
                continue
            if selection == "9":
                league_data = import_json_file()
                selection = ""
                continue
            if selection == "10":
                league_data = {}
                selection = ""
                continue    
            if selection == "11":
                predictions.clear()
                selection = ""
                continue
            
            # General action for other menu items
            if selection == option[1]:
                option[2](league_data)
                selection = ""
