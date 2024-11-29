#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.


with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines() # pega todos os nomes do arquivo 
    clean_names = []

for name in names:
    clean_names.append(name.strip()) # remove espaços e \n, adicionando cada nome "limpo" à lista

for name in clean_names:
    personalized_letter = letter_content.replace("[name]", name)    
    
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w") as new_letter_file:
        new_letter_file.write(personalized_letter)

