"""
This was the first step of this project designing this for store the log
of the game. For future reference this is going to be used for AI agent used this data
to take a better decision.
"""

import datetime

def save_gameplay_to_file(player_name, game_result, board_state, moves):
    current_time = datetime.datetime.now() # Assuming you've imported datetime

    # Create a unique file name
    file_name = "game_record.txt"

    # Create the content to save
    content = f"Player Name: {player_name}\n"
    content += f"Date & Time: {current_time}\n"
    content += f"Game Result: {game_result}\n"
    content += f"Board State: {board_state}\n"
    content += f"Moves: {moves}\n" # Record the moves
    content += "---------------------------\n"

    # Save the content to the file
    with open(file_name, 'a') as file:
        file.write(content)
