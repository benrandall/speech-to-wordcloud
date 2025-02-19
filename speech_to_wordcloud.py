import speech_recognition as sr
import csv
import requests
from datetime import datetime
from collections import Counter

r = sr.Recognizer()
csv_file = "output.csv"
word_limit = 50

# Fetch the list of English stop words
stopwords_list = requests.get(
    "https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt"
).content
stopwords = set(stopwords_list.decode().splitlines())

# Ensure CSV has a header when first run
def initialize_csv():
    try:
        with open(csv_file, "x", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Word", "Count", "Last Updated"])  # Column headers
    except FileExistsError:
        pass  # File already exists, do nothing

# Function to record text from the microphone
def record_text():
    while True:
        try: 
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText.lower()  # Convert to lowercase for consistency
        
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        
        except sr.UnknownValueError:
            print("Unknown error occurred")

# Function to write only the top 50 most repeated words to CSV (excluding stop words)
def output_text(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Read existing data to maintain word count
    word_count = Counter()
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) == 3:
                    word, count, _ = row
                    word_count[word] = int(count)
    except FileNotFoundError:
        pass  # Start fresh if file doesn't exist

    # Process new words (excluding stop words)
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    word_count.update(filtered_words)

    # Keep only the top 50 most repeated words
    top_words = word_count.most_common(word_limit)

    # Write back to CSV with updated data
    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count", "Last Updated"])  # Write header again
        for word, count in top_words:
            writer.writerow([word, count, timestamp])  # Each word gets its own row

# Initialize CSV if not present
initialize_csv()

# Continuous recording and updating of CSV
while True:
    text = record_text()
    if text:
        output_text(text)
        print(f"Recorded: {text}")