# Steven's Function 
def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - number only please.")


# Steven's Function 
def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt).strip()
        if users_input.isalpha():
            return users_input
        print("Please enter a valid, non-empty string containing only letters.")


#Jack function sprint 3
def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Sorry - numbers only, please.")

#Jack function sprint 3
def runners_data():
    runners_name = []
    runners_id = []

    try:
        with open("runners.txt", "r") as input_file:
            lines = input_file.readlines()
        for line in lines:
            if "," in line:
                split_line = line.strip().split(",")
                runners_name.append(split_line[0].strip())
                runners_id.append(split_line[1].strip())
    except FileNotFoundError:
        print("Error: 'runners.txt' file not found.")
    except Exception as e:
        print(f"Error reading 'runners.txt': {e}")

    return runners_name, runners_id

# Steven's Function Sprint 3
def race_results(races_location):
    for i, races_location_item in enumerate(races_location, start=1):
        print(f"{i}: {races_location_item}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


# Steven's Function Sprint 3
def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip())
    return races_location


# Steven's Function
def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if time_taken[i] == quickest_time:
            winner = id[i]
            break  # Exit the loop once the winner is found
    return winner


#Jack Function sprint 3
def display_races(id, time_taken, venue, fastest_runner):
    SECONDS_IN_MINUTE = 60  # Fixed the conversion to use standard time units
    print(f"Results for {venue}")
    print(f"=" * 37)
    
    for i in range(len(id)):
        minutes = time_taken[i] // SECONDS_IN_MINUTE
        seconds = time_taken[i] % SECONDS_IN_MINUTE
        print(f"{id[i]:<10s} {minutes} minutes and {seconds} seconds")
    
    print(f"{fastest_runner} won the race.")


#Paul's Function 
def users_venue(races_location, runners_id):
    #Prompt for new venue
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
        print("This venue already exists. Please provide a new venue.")

    #Record the venue of the race
    races_location.append(user_location)
    with open("races.txt", "a") as race_file:
        print(user_location, file=race_file)

    #Input race times for competitors
    print("Input race times for competitors. Enter 0 if a competitor did not participate.")
    time_taken = []
    with open(f"{user_location}.txt", "w") as race_results_file:
        for runner_id in runners_id:
            time_for_runner = read_integer(f"Time for {runner_id} >> ")
            if time_for_runner >= 0:  
                time_taken.append((runner_id, time_for_runner))
                print(f"{runner_id},{time_for_runner}", file=race_results_file)
            else:
                print("Invalid time. Please enter a non-negative number.")
    
    print(f"Race results for {user_location} have been saved.")

#Jack sprint 3
def updating_races_file(races_location):
    try:
        with open("races.txt", "w") as connection:
            for race in races_location:
                connection.write(f"{race}\n")  # Write each race on a new line
        print("Races file successfully updated.")
    except Exception as e:
        print(f"Error updating races.txt: {e}")


# Jack's Function 
def competitors_by_county(name, id):
    county_dict = {}

    # Group competitors by county based on ID prefix
    for i in range(len(name)):
        county_code = id[i][:2]  # Extract county code from ID
        if county_code not in county_dict:
            county_dict[county_code] = []
        county_dict[county_code].append(f"{name[i]} ({id[i]})")

    # Sort counties alphabetically and display competitors within each county
    for county in sorted(county_dict.keys()):
        print(f"{county} County Competitors")
        print("=" * (len(county) + 19))
        for competitor in sorted(county_dict[county]):
            print(competitor)
        print()

# Jack function sprint 3
def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.strip().split(",")  # Correctly split the line on commas after stripping whitespace and newlines
        id.append(split_line[0])  # First part is the ID
        time_taken.append(int(split_line[1]))  # Second part is the time, converted to integer
    return id, time_taken


#Rory's Funtion
# Function which grabs all runners times and returns them
def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",")
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    return id, time_taken  # Changed to return all runners times


# Rory's Function
# Function displays the top three finishers for each race venue, showing their positions, runner IDs, and times.
def top_three_finishers(races_location):
    print(f"{'Venue':<20}{'Position':<10}{'Runner ID':<15}{'Time':<10}")
    print("=" * 55)
    # Loop to display results
    for venue in races_location:
        id, time_taken = reading_race_results_of_relevant_runner(venue)
        
        # All runner IDs and sorted by time
        runners = list(zip(id, time_taken))
        runners.sort(key=lambda x: x[1])  

        print(f"Results for {venue}")
        print("-" * 55)

        # Table that shows the top 3 race finishers
        for i, (runner_id, time) in enumerate(runners[:3], start=1):
            minutes, seconds = convert_time_to_minutes_and_seconds(time)
            print(f"{venue:<20}{i:<10}{runner_id:<15}{minutes}m {seconds}s")
        print("-" * 55)


# Steven's Function Sprint 3 
def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input - 1]
    return runner, id

# Steven's Function Sprint 3
def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 60  # Corrected minute length to 60 seconds
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


# Steven's Function Sprint 3
def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.strip().split(",")  # Fixed incorrect use of `strip` inside `split`
        t = int(split_line[1].strip())  # Removed unnecessary `strip("\n")` as `strip()` handles all trailing whitespace
        time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


#Jack function sprint 3
def displaying_race_times_one_competitor(races_location, runner, runner_id):
    print(f"{runner} ({runner_id})")
    print("-" * 35)
    found_any_race = False  # Track if the runner has participated in any race

    for race in races_location:
        try:
            # Read race results for the current race
            race_results = reading_race_results(race)
            ids, times = race_results
            
            # Check if the runner participated in the race
            if runner_id in ids:
                found_any_race = True
                runner_index = ids.index(runner_id)
                time_taken = times[runner_index]
                
                # Convert time to minutes and seconds
                minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
                
                # Get the runner's position and total participants
                position, total_runners = sorting_where_runner_came_in_race(race, time_taken)
                
                # Print results for the race
                print(f"{race:<15} {minutes} mins {seconds} secs ({position} of {total_runners})")
        
        except FileNotFoundError:
            print(f"Race file for {race} not found. Skipping.")
        except Exception as e:
            print(f"Error processing race {race}: {e}")

    if not found_any_race:
        print(f"No races found for {runner} ({runner_id}).")

#Rory function sprint 3
def finding_name_of_winner(fastest_runner, runners_id, runners_name):
    """
    Find the name of the runner based on their ID.
    """
    try:
        # Find the index of the fastest runner's ID in the runners_id list
        index = runners_id.index(fastest_runner)
        return runners_name[index]
    except ValueError:
        # Handle cases where the fastest_runner ID is not found
        return "Unknown Runner"


#Paul function sprint 3
def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    """
    Display the runners who have won at least one race.
    """
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    
    winners = set()  # Use a set to track unique winners by ID
    winner_details = []  # List to store (name, ID) tuples for display
    
    for location in races_location:
        # Read race results for the current location
        id, time_taken = reading_race_results(location)
        
        # Find the fastest runner for the race
        fastest_runner = winner_of_race(id, time_taken)
        
        # Avoid adding duplicate winners
        if fastest_runner not in winners:
            # Find the name of the runner
            name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
            
            # Add to sets/lists for unique identification
            winners.add(fastest_runner)
            winner_details.append((name_of_runner, fastest_runner))
    
    # Display the winners in a formatted output
    for name, runner_id in winner_details:
        print(f"{name} ({runner_id})")



def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 7)

    while input_menu == 7:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu != 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            top_three_finishers(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 7)
    updating_races_file(races_location)


main()
