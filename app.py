'''
When you run the program, it should generate a new text file.
The program assigns a random name of 10 characters to the text file and also writes that random text inside the text file as content.
'''
import random_generator

random_text = random_generator.unique_string(10)

with open(f'{random_text}.txt','w') as file:
    file.write(random_text)
    file.close