# read "words.txt"
# each line, if not empty, is the word and its meaning
# extract the word and its meaning
# save as "words.csv", each line has 4 columns:
# word, meaning, 0, 0.
# in future, the last two columns will be used to record
# the times of the word being tested
# and the times of the word being correct


import csv

def process_line(line):
    # Split the line into word and meaning
    parts = line.strip().split()
    word = parts[0]
    meaning = ' '.join(parts[1:])

    return word, meaning

# Read from "words.txt" and write to "words.csv"
with open("words.txt", "r", encoding="utf-8") as infile, \
    open("words.csv", "w", newline="", encoding="gbk") as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(["word", "meaning", "total", "correct"])  # Write header

    for line in infile:
        if line.strip():  # Check if the line is not empty
            word, meaning = process_line(line)
            csv_writer.writerow([word, meaning, 0, 0])
            
print("Conversion complete. Check 'words.csv'.")
