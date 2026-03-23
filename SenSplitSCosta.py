import re
import sys


def split_into_sentences(paragraph):

    # Split sentances/ .,! or ? folowed by a space or spaces
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())

    # Remove any and all empty strings
    return [s for s in sentences if s]


def display_sentences(sentences):

    # Displays each sentences and the total count.
    print("Individual Sentences: ")

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}, {sentence}" )

    print(f" Total Sentences: {len(sentences)}")

def main():
    paragraph = input("Enter a Paragraph: ")

    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()