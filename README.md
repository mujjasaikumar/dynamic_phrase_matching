
# Dynamic Phrase Matching

This Python script extracts phrases and sentences from an Excel file (.xlsx), then matches phrases in sentences and records their positions. The results are saved in a JSON file.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mujjasaikumar/dynamic_phrase_matching.git
   ```

2. **Add Input File:**
   Place your `phrases_and_sentences.xlsx` file containing phrases in the first column and sentences in the second column in the root directory of the repository.

3. **Run the Script:**
   ```bash
   python main.py
   ```

4. **View Results:**
   The script will create a file named `results.json` containing the matching results in JSON format.

## Files

- `main.py`: The main Python script containing the logic to match phrases in sentences fetched from an Excel file.
- `phrases_and_sentences.xlsx`: Input Excel file containing phrases in the first column and sentences in the second column.
- `results.json`: Output file containing the matching results in JSON format.

## Dependencies

- Python 3.x
- openpyxl (if using Excel file)

## Functionality

### Approach 1: Excel File
- The script loads phrases and sentences from the provided Excel file.
- It matches each phrase in each sentence, recording the start and end indices along with the phrase.
- The results are saved in a JSON file.

### Approach 2: Text Files
- Alternatively, the script can read phrases from `phrases.txt` and sentences from `sentences.txt`.
- It matches each sentence with all phrases, recording the start and end indices along with the phrase.
- The results are saved in a JSON file.

## Optimizations

- The script skips None values when processing phrases to avoid errors.
- It strips leading and trailing whitespace from phrases and sentences to ensure accurate matching.

```
