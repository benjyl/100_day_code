# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# invited = "Input/Names/invited_names.txt" # relative path
invited = "/Users/benjy/OneDrive/Coding/100_day_code/day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
guest_list = [line.rstrip() for line in open(invited)]

# letter =
# with open

print(guest_list)
