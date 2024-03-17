
import openpyxl
import json


def find_matching_phrases(sentence, phrases):
    matches = []
    for phrase in phrases:
        if phrase is not None:  # Skip None values
            phrase = phrase.strip()
            start_index = sentence.find(phrase)
            while start_index != -1:
                end_index = start_index + len(phrase)
                matches.append({
                    "text": sentence,
                    "start": start_index,
                    "end": end_index,
                    "value": phrase
                })
                start_index = sentence.find(phrase, start_index + 1)
    return matches


def main():
    # Load the Excel file
    workbook = openpyxl.load_workbook("phrases_and_sentences.xlsx")
    worksheet = workbook.active

    # Extract phrases and sentences
    rows = list(worksheet.iter_rows(values_only=True))
    phrases = [row[0] for row in rows if row[0] is not None]  # Phrases are in the first column
    sentences = [row[1] for row in rows]  # Sentences are in the second column

    # # If phrases are given in phrases.txt file and sentences are given in sentences.txt file, uncomment the following code and run.
    # # Read sentences from sentences.txt
    # with open("sentences.txt", "r") as sentences_file:
    #     sentences = [line.strip() for line in sentences_file if line.strip()]
    #
    # # Read phrases from phrases.txt
    # with open("phrases.txt", "r") as phrases_file:
    #     phrases = [line.strip() for line in phrases_file if line.strip()]

    # Process each sentence
    results = []
    for sentence in sentences:
        sentence = sentence.strip()
        matches = find_matching_phrases(sentence, phrases)
        results.extend(matches)

    # # To Print the results in JSON format in console
    # print(json.dumps(results, indent=4))

    # Save the results in a JSON file
    with open("results.json", "w") as json_file:
        json.dump(results, json_file, indent=4)


if __name__ == "__main__":
    main()
