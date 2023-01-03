# invited = "Input/Names/invited_names.txt" # relative path
invited = "/Users/benjy/OneDrive/Coding/100_day_code/day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
guest_list = [line.rstrip() for line in open(invited)]

letter = "/Users/benjy/OneDrive/Coding/100_day_code/day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
with open(letter, mode="r") as invitation:
    invite = invitation.readlines()  # store generic invitation

# directory where want to store personal invites
output_dir = "/Users/benjy/OneDrive/Coding/100_day_code/day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/"

# personalise invite for each guest
for name in guest_list:
    with open(f"{output_dir}letter_for_{name}.txt", mode="w") as invitation:
        personal_invitation = [line.replace("[name]", name) for line in invite]
        for line in personal_invitation:
            invitation.write(line)
