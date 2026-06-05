import csv
import os

#I consistenly had an issue where I could not locate the csv file and I went to
#w3 schools but it was a computer file/folder thing.
#this code lets the program keep going with an exception instead of just immediately breaking.

#Code that did not work because there was a file location error:
#import csv


#def read_teams():
    #teams = []

    #with open("team.csv", "r", newline="") as file:
        #reader = csv.DictReader(file)

        #for row in reader:
            #teams.append(row)

    #return teams


#def read_players():
    #players = []

    #with open("player.csv", "r", newline="") as file:
        #reader = csv.DictReader(file)
#It was kind of unspecific i suppose

#Original code from me over
#___________________This is AI Generated Code from CHATGPT_____________
# Always use the folder containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_teams():
    teams = []
#defines the exact file path with the csv files
    file_path = os.path.join(BASE_DIR, "team.csv")
#uses a try so that an exception can be raised if it is not found
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                teams.append(row)

    except FileNotFoundError:
        print("\nERROR: team.csv was not found.")
        print("Expected location:", file_path)

    return teams
#______________________________CHATGPT CODE OVER________________________

#after I saw the CHATGPT code I replicated it with the player csv file so it would be the same function 
def read_players():
    players = []

    file_path = os.path.join(BASE_DIR, "player.csv")

    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                players.append(row)

    except FileNotFoundError:
        print("\nERROR: player.csv was not found.")
        print("Expected location:", file_path)

    return players

#first function this one is pretty simple
def display_teams():
    teams = read_teams()
#                ^reads csv file
    if len(teams) == 0:
        print("\nNo teams found.")
        return
# just in case no data is there
    teams.sort(key=lambda team: team["Team"])
#print the list of teams to the user
    print("\nTeam List")
    print("-" * 40)
#prints the data from the csv file (found this on w3)
    for team in teams:
        print(f"{team['Team']} ({team['Sport']}) - {team['City']}")

# Relatively similar but there is more data per player
def display_players():
    teams = read_teams()

    if len(teams) == 0:
        return
#print so users can see teams to choose a player from
    print("\nTeams")
    print("-" * 40)

    for team in teams:
        print(team["Team"])
#user selects player
    selected_team = input("\nEnter team name: ").strip()

    players = read_players()

    team_players = []
#making sure that a player exists in that team and if it does not it stops
    for player in players:
        if player["Team"].lower() == selected_team.lower():
            team_players.append(player)

    if len(team_players) == 0:
        print("\nNo players found for that team.")
        return

    team_players.sort(key=lambda player: player["Player"])
#prints the players
    print("\nPlayers")
    print("-" * 40)
#and prints their respective data
    for player in team_players:
        print(
            f"{player['Player']} | "
            f"{player['Position']} | "
            f"#{player['Number']} | "
            f"Age {player['Age']}"
        )

#this one was suprisingly easier than I thought
def add_player():
    teams = read_teams()
#cant add a player without any teams
    if len(teams) == 0:
        return

    print("\nTeams")
    print("-" * 40)

    for team in teams:
        print(team["Team"])
#user chooses the team they want to add a player to
    team_name = input("\nEnter team name: ").strip()
#all of the .strips are to remove whitespaces that might confuse the program
    player_name = input("Player name: ").strip()
    position = input("Position: ").strip()
    number = input("Jersey number: ").strip()
    age = input("Age: ").strip()

    players = read_players()
#making sure that the player does not already exist on a team so there is no duplicates
    for player in players:
        if (
            player["Player"].lower() == player_name.lower()
            and player["Team"].lower() == team_name.lower()
        ):
            print("\nPlayer already exists on that team.")
            return
#adds the information onto the actual csv file with each type of data from previous input statements
        
    file_path = os.path.join(BASE_DIR, "player.csv")

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            player_name,
            team_name,
            position,
            number,
            age
        ])
##everything went smoothly
    print("\nPlayer added successfully.")

#relatively same as add in terms of difficulty but definitely different
def delete_player():
    teams = read_teams()
#this is all the same making sure that the team and player actually exists
    if len(teams) == 0:
        return

    print("\nTeams")
    print("-" * 40)

    for team in teams:
        print(team["Team"])

    team_name = input("\nEnter team name: ").strip()

    players = read_players()

    team_players = []
#prevents deleting a player from a playerless team
    for player in players:
        if player["Team"].lower() == team_name.lower():
            team_players.append(player)

    if len(team_players) == 0:
        print("\nNo players found for that team.")
        return

    print("\nPlayers")
    #i use lots of these statements throughout to make the text look more professional
    print("-" * 40)

    for player in team_players:
        print(player["Player"])
#user chooses the player to delete
    player_name = input("\nEnter player name to delete: ").strip()

    found = False
    updated_players = []
#uses lowercase methods and determines the data associated with the player
    for player in players:
        if (
            player["Player"].lower() == player_name.lower()
            and player["Team"].lower() == team_name.lower()
        ):
            found = True
        else:
            updated_players.append(player)
#cant delete a player that does not exist
    if not found:
        print("\nPlayer not found.")
        return
#navigates back to csv file to delete the data associated with the chosen player
    file_path = os.path.join(BASE_DIR, "player.csv")

    with open(file_path, "w", newline="") as file:
        fieldnames = [
            "Player",
            "Team",
            "Position",
            "Number",
            "Age"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(updated_players)

    print("\nPlayer deleted successfully.")

    print("\nUpdated Team Roster")
    print("-" * 40)

    for player in updated_players:
        if player["Team"].lower() == team_name.lower():
            print(player["Player"])

#This one was crazy but I really wanted to implement this
#i like to use this for number changes and trades but CHATGPT had to help me a bit here (which i cite)
def edit_player():
    teams = read_teams()

    if len(teams) == 0:
        return
#very similar printing data to other functions to choose which team
    print("\nTeams")
    print("-" * 40)

    for team in teams:
        print(team["Team"])

    team_name = input("\nEnter team name: ").strip()

    players = read_players()

    team_players = []
#making sure data aligns in csv files with user input
    for player in players:
        if player["Team"].lower() == team_name.lower():
            team_players.append(player)

    if len(team_players) == 0:
        print("\nNo players found for that team.")
        return

    print("\nPlayers")
    print("-" * 40)

    for player in team_players:
        print(player["Player"])
#user inputs which player they want from that team to edit
    player_name = input("\nEnter player name: ").strip()
#this makes sure that the player exists and if it does not it returns to the beginning
    player_found = None

    for player in players:
        if (
            player["Player"].lower() == player_name.lower()
            and player["Team"].lower() == team_name.lower()
        ):
            player_found = player
            break

    if player_found is None:
        print("\nPlayer not found.")
        return
##prints out options to edit
    print("\nEdit Options")
    print("1. Name")
    print("2. Team")
    print("3. Position")
    print("4. Number")
    print("5. Age")

    choice = input("Choose field to edit: ").strip()
#relativley simple input functions into new variables that will change in future
    if choice == "1":
        new_value = input("Enter new name: ").strip()
        player_found["Player"] = new_value

    elif choice == "2":
        new_value = input("Enter new team: ").strip()
        player_found["Team"] = new_value

    elif choice == "3":
        new_value = input("Enter new position: ").strip()
        player_found["Position"] = new_value

    elif choice == "4":
        new_value = input("Enter new jersey number: ").strip()
        player_found["Number"] = new_value

    elif choice == "5":
        new_value = input("Enter new age: ").strip()
        player_found["Age"] = new_value

    else:
        print("\nInvalid choice.")
        return
#________________________________________AI GENERATED CODE FROM CHATGPT STARTS_______________________________
#I was able to find out how to gather all of the data and inputs of what needed to be changed but i just could not figure out how to actually implement the changes
#Basically all chatgpt i used was just for the outside files and csv organization
    file_path = os.path.join(BASE_DIR, "player.csv")

    with open(file_path, "w", newline="") as file:
        fieldnames = [
            "Player",
            "Team",
            "Position",
            "Number",
            "Age"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(players)
#_________________________________________________CHATGPT CODE ENDS_____________________________________________
    print("\nPlayer updated successfully.")
#the actual menu of what is happening that starts out the entire thing
#python has all of the functions defined above so now it is just about executing them when they are chosen
def display_menu():
    print("\n" + "=" * 25)
    print("Sports Data")
    print("=" * 25)
    print("1. Display Teams")
    print("2. Display Players")
    print("3. Add Player")
    print("4. Delete Player")
    print("5. Edit Player")
    print("6. Exit Program")
    print("=" * 25)

#final debug tool for finding csv folders 
def main():
    print("Script Folder:")
    print(BASE_DIR)

    print("\nFiles Found:")
    print(os.listdir(BASE_DIR))
#if they choose the option, do the option function, its great.
    #keeps menu open as user chooses different things
    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_teams()

        elif choice == "2":
            display_players()

        elif choice == "3":
            add_player()

        elif choice == "4":
            delete_player()

        elif choice == "5":
            edit_player()

        elif choice == "6":
            print("\nThank you for using Sports Data.")
            break

        else:
            print("\nInvalid selection. Choose 1-6.")


if __name__ == "__main__":
    main()
