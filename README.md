# Sports-Analyzer
Welcome to the Sports analyzer application where we can update you on the players you love most on a daily perspective using raw SQL.
Built with a modular pckage structure - Pipenv.

In this app we can use it to:
     1. Create
     2. View
     3. Update
     4. Delete
records for teams,players and youngsters.
We mainly focus on premier league teams and players.

The application has been organized with modular python files(models, connection, cli).

INSTALL DEPENDENCIES
Ensure you have installed Pipenv,the run:
pipenv install
pipenv shell

 SET UP THE DATABASE
Run the schema SQL script to create the tables:
sqlite3 sports.db < schema.sql

SEED THE DATABASE WITH SAMPLE DATA
python app/seed.py

RUN THE APPLICATION
python main.py