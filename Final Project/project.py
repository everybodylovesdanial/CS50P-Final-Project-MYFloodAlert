import requests
import sys
import os
from rich.console import Console
from tabulate import tabulate
from pyfiglet import Figlet

figlet = Figlet(font = "big")
console = Console()

response = requests.get("https://api.data.gov.my/flood-warning")
data = response.json()


# Level 1
def get_states(data, user_input=None):
    states = set() # get all of states within malaysia
    for entry in data:
        states.add(entry["state"])

    numbered_states = [] # store the states in a list with numbers
    for i, state in enumerate(sorted(states)):
        numbered_states.append((i+1, state))

    if user_input is not None: # for testing
        try:
            select = int(user_input)
            if 1 <= select <= len(numbered_states):
                selected_state = numbered_states[select - 1][1]
                return selected_state
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_states)} only")
        except ValueError:
            console.print ("[dark_orange]Enter an integer")

    else: # printing the table
        table = tabulate(numbered_states, tablefmt="rounded_outline")
        console.print(f"[turquoise2]{table}")

    while True:
        try:
            select = int(input("Select from list: "))
            if 1 <= select <= len(numbered_states):
                selected_state = numbered_states[select - 1][1]  # "[select - 1]" because list starts from 0. "[1]" because [0] is the list number and [1] is the state.
                return selected_state
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_states)} only")
        except ValueError:
            console.print ("[dark_orange]Enter an integer")


# Level 2
def get_districts(state_data, user_input=None):   # user_input allow for automated testing without using input()
    districts = set()
    for entry in state_data:
        districts.add(entry["district"])

    numbered_districts = []
    for i, district in enumerate(sorted(districts)):
        numbered_districts.append((i+1, district))

    if user_input is not None:
        select = str(user_input)
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(numbered_districts):
                selected_district = numbered_districts[select - 1][1]
                return selected_district
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_districts)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")

    else:
        table = tabulate(numbered_districts, tablefmt="rounded_outline")
        console.print(f"[turquoise2]{table}")

        console.print(f"[yellow1]Select from 1-{len(numbered_districts)}")
        console.print("[yellow1]Enter 'b' to go back")

    while True:
        select = input("Input: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(numbered_districts):
                selected_district = numbered_districts[select - 1][1]
                return selected_district
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_districts)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")



# Level 3
def get_main_basins(state_data, user_input=None):
    main_basins = set()
    for entry in state_data:
        main_basins.add(entry["main_basin"])

    numbered_main_basins = []
    for i, main_basin in enumerate(sorted(main_basins)):
        numbered_main_basins.append((i+1, main_basin))

    if user_input is not None:
        select = str(user_input)
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(numbered_main_basins):
                selected_main_basin = numbered_main_basins[select - 1][1]
                return selected_main_basin
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_main_basins)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")

    else:
        table = tabulate(numbered_main_basins, tablefmt="rounded_outline")
        console.print(f"[turquoise2]{table}")

        console.print(f"[yellow1]Select from 1-{len(numbered_main_basins)}")
        console.print("[yellow1]Enter 'b' to go back")

    while True:
        select = input("Input: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(numbered_main_basins):
                selected_main_basin = numbered_main_basins[select - 1][1]
                return selected_main_basin
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(numbered_main_basins)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")




# Level 4
def get_sub_basins(state_data, user_input=None):
    sub_basins = set()
    for entry in state_data:
        sub_basins.add(entry["sub_basin"])

    index_sub_basins = []
    for i, sub_basin in enumerate(sorted(sub_basins)):
        index_sub_basins.append((1+i, sub_basin))


    if user_input is not None:
        select = str(user_input)
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(index_sub_basins):
                    selected_sub_basin = index_sub_basins[select - 1][1]
                    return selected_sub_basin
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(index_sub_basins)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")

    else:
        table = tabulate(index_sub_basins, tablefmt="rounded_outline")
        console.print(f"[turquoise2]{table}")

        console.print(f"[yellow1]Select from 1-{len(index_sub_basins)}")
        console.print("[yellow1]Enter 'b' to go back")

    while True:
        select = input("Input: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= len(index_sub_basins):
                selected_sub_basin = index_sub_basins[select - 1][1]
                return selected_sub_basin
            else:
                console.print (f"[dark_orange]Enter number from 1 - {len(index_sub_basins)} only")
        elif select.lower() == "b":
            return "back"
        else:
            console.print("[dark_orange]Enter a valid input")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print()
        text = figlet.renderText("MYFloodAlert")
        console.print(f"[deep_sky_blue1]{text}")
        console.print("              [bold turquoise2]List of States")
        state = get_states(data)

        state_data = []  # to add state datas into a list
        for entry in data:
            if entry["state"] == state:
                state_data.append(entry)

        while True:
            print()
            console.print(f"[bold turquoise2]List of Districts in {state}")
            district = get_districts(state_data)
            if district == "back":
                clear_console()
                break
            else:
                pass


            while True:
                print()
                console.print(f"[bold turquoise2]List of Main Basin in {district}")
                main_basin = get_main_basins(state_data)
                if main_basin == "back":
                    clear_console()
                    break
                else:
                    pass

                while True:
                    print()
                    console.print(f"[bold turquoise2]List of Sub-Basin in {main_basin}")
                    sub_basin = get_sub_basins(state_data)
                    if sub_basin == "back":
                        clear_console()
                        break
                    else:
                        for entry in state_data:
                            if entry["sub_basin"] == sub_basin:
                                print()
                                print()

                                location = [
                                    ["State:", state],
                                    ["District:", district],
                                    ["Main Basin:", main_basin],
                                    ["Sub-Basin:", sub_basin],
                                ]

                                # Print the tabulated data
                                table = tabulate(location, tablefmt="rounded_outline")
                                console.print(f"[medium_orchid]{table}")

                                current_level = entry["water_level_current"]
                                normal_level = entry["water_level_normal_level"]
                                danger_level = entry["water_level_danger_level"]

                                print(f"Normal water level: {normal_level}")
                                print(f"Danger water level: {danger_level}")

                                if None not in [current_level, normal_level, danger_level]:
                                    if current_level <= normal_level:
                                        console.print(f"Current water level: [bright_green]{entry['water_level_current']}")
                                    elif danger_level > current_level > normal_level:
                                        console.print(f"Current water level: [orange1]{entry['water_level_current']}")
                                    elif current_level >= danger_level:
                                        console.print(f"Current water level: [bright_red]{entry['water_level_current']}")
                                else:
                                    print("Current water level: None")

                                print()


                                rainfall = entry["rainfall_indicator"]
                                if rainfall != None:
                                    if rainfall == "NO_RAINFALL":
                                        console.print("Rainfall status: [bright_green]NO RAINFALL")
                                    elif rainfall == "LIGHT":
                                        console.print("Rainfall status: [bright_yellow]LIGHT")
                                    elif rainfall == "MODERATE":
                                        console.print("Rainfall status: [orange1]MODERATE")
                                    elif rainfall == "ERROR":
                                        console.print("Rainfall status: [bright_white]NO DATA")
                                else:
                                    print("Rainfall status: None")

                                water_condition = entry["water_level_indicator"]
                                if water_condition != None:
                                    if water_condition == "NORMAL":
                                        console.print("Water level condition: [bright_green]NORMAL")
                                    elif water_condition == "ALERT":
                                        console.print("Water level condition: [bright_yellow]ALERT")
                                    elif water_condition == "WARNING":
                                        console.print("Water level condition: [orange1]WARNING")
                                    elif water_condition == "DANGER":
                                        console.print("Water level condition: [bright_red]DANGER")
                                    elif water_condition == "ERROR":
                                        console.print("Water level condition: [bright_white]NO DATA")
                                else:
                                    print("Water level condition: None")


                                water_trend = entry["water_level_trend"]
                                if water_trend != None:
                                    if water_trend == "RISING":
                                        console.print("Water level trend: [bright_red]RISING")
                                    elif water_trend == "RECEDING":
                                        console.print("Water level trend: [bright_green]RECEDING")
                                    elif water_trend == "NO_CHANGE":
                                        console.print("Water level trend: [bright_white]NO CHANGE")
                                else:
                                    print("Water level trend: None")


                                print()

                                print(f"Last updated: {entry['water_level_update_datetime']}")

                                print()
                                sys.exit()



if __name__ == "__main__":
    main()





# pip install...
# python project.py
