# Speech to WordCloud

This project records speech from the microphone, processes it to extract the top 50 most frequent words (excluding stop words), and writes the results to a CSV file.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the project files to your local machine.

2. Open a Command Prompt and navigate to the project directory:
    ```sh
    cd ./speech-to-wordcloud
    ```

3. Install the required Python packages using `pip`:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have a working microphone connected to your computer.

## Running the Project

1. Open a Command Prompt and navigate to the project directory:
    ```sh
    cd ./speech-to-wordcloud
    ```

2. Run the Python script:
    ```sh
    python speech_to_wordcloud.py
    ```

3. The script will continuously listen for speech input and update the `output.csv` file with the top 50 most frequent words.

4. To stop the script, press `Enter` in the Command Prompt window.

## Notes

- The script fetches a list of English stop words from an online source. Ensure you have an active internet connection when running the script for the first time.
- The `output.csv` file will be created in the project directory if it does not already exist.
