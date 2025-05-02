import os
import json
import datetime
from rich.console import Console
from rich.table import Table
console = Console()

os.system("clear")
console.print("Welcome to FocusIT!\n", style="bold underline blue")

def listActions():
    console.print("<l> to list your weekly activity")
    console.print("<s> to start your current session")
    console.print("<x> to exit\n")

listActions()

# session variables
MAIN = True
SESSION_SAVE = False
SESSION_LIST = False

def start_save():
    global SESSION_SAVE, MAIN, SESSION_LIST
    SESSION_SAVE = True
    MAIN = False
    SESSION_LIST = False

def start_list():
    global SESSION_SAVE, MAIN, SESSION_LIST
    SESSION_LIST = True
    MAIN = False
    SESSION_SAVE = False

def start_main():
    global SESSION_SAVE, MAIN, SESSION_LIST
    MAIN = True
    SESSION_SAVE = False
    SESSION_LIST = False

def getSessionData():
    if not os.path.exists("session.json"):
        return []
    with open("session.json", "r") as data_file:
        content = data_file.read()
        if content.strip():
            return json.loads(content)
        return []


def saveSessionData(data):
    prev_data = getSessionData()
    prev_data.append(data)
    with open("session.json", "w") as data_file:
        json.dump(prev_data, data_file, indent=4)

def overwriteSessionData(new_data):
    with open("session.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)


def collectGarbage():
    current_time = datetime.datetime.now()
    all_session_data = getSessionData()
    valid_sessions = []

    for session in all_session_data: 
        session_start = datetime.datetime.fromisoformat(session["start"])
        if current_time - session_start <= datetime.timedelta(days=7):
            valid_sessions.append(session)

    overwriteSessionData(valid_sessions)

collectGarbage() # clear up garbage if any

# main session
while MAIN == True:
    console.print("Your command:", style="yellow")
    user_input = input()

    if user_input == "l" or user_input == "<l>":
        os.system("clear")
        start_list()
    elif user_input == "s" or user_input == "<s>":
        print("<session started>")
        start_save()
    elif user_input == "x" or user_input == "<x>":
        print("exiting...")
        MAIN = False
    else:
        console.print("Requested command not found.", style="bold red")

# recording session
while SESSION_SAVE == True:
    print("Give your session a name:")
    session_name = input()

    if session_name:
        start_time = datetime.datetime.now()
        print("Press enter when you are done.")
        event_listener = input()

        if event_listener or event_listener == "":
            end_time = datetime.datetime.now()

            sessionDataRecorded = {
                "start": start_time.isoformat(),
                "end": end_time.isoformat(),
                "label": session_name
            }
            saveSessionData(sessionDataRecorded)
            start_main()
    
# list all weekly session inference
while SESSION_LIST == True:
    os.system("clear")

    table = Table(title="User weekly performance")
    table.add_column("Date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Label", style="magenta")
    table.add_column("Time Spend", justify="right", style="green")

    session_data = getSessionData()
    for session in session_data: 
        session_date = datetime.datetime.fromisoformat(session["start"]).strftime("%x")
        current_time = datetime.datetime.now()
        time_diff = datetime.datetime.fromisoformat(session["end"]) - datetime.datetime.fromisoformat(session["start"])
        hours, remainder = divmod(time_diff.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_difference = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

        table.add_row(session_date, session["label"], time_difference)

    console.print(table)
    print("Press enter to exit")
    user_input = input()
    if user_input or user_input == "":
        start_main()