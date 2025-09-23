#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()


with open("Input/Names/invited_names.txt") as names_list:
    name_content = names_list.readlines()


for name in range(len(name_content)):
    new_content = content.replace("[name]", name_content[name].strip())
    with open(f"Output/ReadyToSend/letter_for_{name_content[name].strip()}.txt", mode="w") as new_file:
        new_file.write(new_content)
