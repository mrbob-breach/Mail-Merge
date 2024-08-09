PLACEHOLDER = "[name]"

invited_names = open("Input/Names/invited_names.txt")
names = invited_names.readlines()

letter = open("Input/Letters/starting_letter.txt")
letter_contents = letter.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    print(new_letter)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
