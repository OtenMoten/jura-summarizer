# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

import os

from LegalTextSummarizer import LegalTextSummarizer


def read_legal_text(file_path_to_text):
    """
    📖 Open the case file and read its contents!

    This function reads the legal text from a file, like a legal clerk retrieving and
    opening a case file from the archives.

    Args:
        file_path_to_text (str): Path to the file containing the legal text.

    Returns:
        str: The contents of the legal text file.
    """
    with open(file_path_to_text, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":

    file_path = "input.txt"

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: The file {file_path} does not exist.")
    else:
        # Read the legal text from the file
        legal_text = read_legal_text(file_path)

        # Create our legal summarizer
        summarizer = LegalTextSummarizer()

        # Generate the summary
        summary = summarizer.summarize_legal_text(legal_text, num_sentences=10)

        print("🎉 Summary:")
        print(summary)
