from app.models.team import Team
from app.models.player import Player
from app.models.youngster import Youngster

def display_menu():
    print("\n--- Sports Analyzer CLI ---")
    print("1. View all teams")
    print("2. Add a team")
    print("3. Update a team")
    print("4. Delete a team")
    print("5. View all players")
    print("6. Add a player")
    print("7. Update a player")
    print("8. Delete a player")
    print("9. View all youngsters")
    print("10. Add a youngster")
    print("11. Update a youngster")
    print("12. Delete a youngster")
    print("13. Exit")

def cli():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            teams = Team.all()
            for t in teams:
                print(f"ID: {t[0]}, Name: {t[1]}, League: {t[2]}")

        elif choice == "2":
            name = input("Team name: ")
            league = input("League: ")
            Team.create(name, league)
            print("Team added!")

        elif choice == "3":
            id = int(input("Team ID to update: "))
            name = input("New name (leave blank to skip): ") or None
            league = input("New league (leave blank to skip): ") or None
            Team.update(id, name, league)
            print("Team updated.")

        elif choice == "4":
            id = int(input("Team ID to delete: "))
            Team.delete(id)
            print("Team deleted.")

        elif choice == "5":
            players = Player.all()
            for p in players:
                print(f"ID: {p[0]}, Name: {p[1]}, Position: {p[2]}, Team ID: {p[3]}")

        elif choice == "6":
            name = input("Player name: ")
            position = input("Position: ")
            team_id = int(input("Team ID: "))
            Player.create(name, position, team_id)
            print("Player added!")

        elif choice == "7":
            id = int(input("Player ID to update: "))
            name = input("New name (leave blank to skip): ") or None
            position = input("New position (leave blank to skip): ") or None
            team_id = input("New team ID (leave blank to skip): ")
            team_id = int(team_id) if team_id else None
            Player.update(id, name, position, team_id)
            print("Player updated.")

        elif choice == "8":
            id = int(input("Player ID to delete: "))
            Player.delete(id)
            print("Player deleted.")

        elif choice == "9":
            youngsters = Youngster.all()
            for y in youngsters:
                print(f"ID: {y[0]}, Name: {y[1]}, Academy: {y[2]}, Player ID: {y[3]}, Team ID: {y[4]}")

        elif choice == "10":
            name = input("Youngster name: ")
            academy = input("Academy: ")
            player_id = int(input("Player ID: "))
            team_id = int(input("Team ID: "))
            Youngster.create(name, academy, player_id, team_id)
            print("Youngster added!")

        elif choice == "11":
            id = int(input("Youngster ID to update: "))
            name = input("New name (leave blank to skip): ") or None
            academy = input("New academy (leave blank to skip): ") or None
            player_id = input("New player ID (leave blank to skip): ")
            player_id = int(player_id) if player_id else None
            team_id = input("New team ID (leave blank to skip): ")
            team_id = int(team_id) if team_id else None
            Youngster.update(id, name, academy, player_id, team_id)
            print("Youngster updated.")

        elif choice == "12":
            id = int(input("Youngster ID to delete: "))
            Youngster.delete(id)
            print("Youngster deleted.")

        else:
            print("Invalid choice. Try again.")            