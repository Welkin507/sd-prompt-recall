# this file is used to read the ./WordList/words.csv and test the user
# the words.csv has 4 columns: word, meaning, total, correct
# total is the times of the word being tested
# correct is the times of the word being correct
# random select a word from the words.csv,
# which has the least times of correct.
# display the meaning and ask the user to input the word
# if the user input the correct word, total and correct will be added 1,
# otherwise, only total will be added 1.


import csv
import random

def load_word_list(file_path):
    with open(file_path, 'r', newline='', encoding='gbk') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_word_list(file_path, word_list):
    fieldnames = ['word', 'meaning', 'total', 'correct']
    with open(file_path, 'w', newline='', encoding='gbk') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(word_list)

def select_word(word_list):
    # Select the word with the least times of correct
    number_of_least_correct = min(int(word['correct']) for word in word_list)
    least_correct_list = [word for word in word_list if int(word['correct']) == number_of_least_correct]
    least_correct_word = random.choice(least_correct_list)
    return least_correct_word

def main():
    file_path = './WordList/words.csv'
    word_list = load_word_list(file_path)

    while True:
        # Select a word with the least times of correct
        selected_word = select_word(word_list)

        # Display the meaning and ask the user to input the word
        meaning = selected_word['meaning']
        user_input = input(f"Meaning: {meaning}\nEnter the word: ")

        # Check if the user input is 'pass'
        if user_input.lower() == 'pass':
            print("Pass!")
            selected_word['total'] = str(int(selected_word['total']) + 100)
            selected_word['correct'] = str(int(selected_word['correct']) + 100)
            continue

        # Check if the user input is correct
        if user_input.lower() == selected_word['word'].lower():
            print("Correct!")
            selected_word['total'] = str(int(selected_word['total']) + 1)
            selected_word['correct'] = str(int(selected_word['correct']) + 1)
        else:
            print(f"Wrong! The correct word is {selected_word['word']}.")
            selected_word['total'] = str(int(selected_word['total']) + 1)

        # Save the updated word list to the file
        save_word_list(file_path, word_list)

if __name__ == "__main__":
    main()
