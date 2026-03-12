"""
Project 5:  Text Analysis

Text Title: Alice's Adventures in Wonderland
Author: Lewis Carroll
Source: Project Gutenberg - https://www.gutenberg.org/files/11/11-0.txt
Approx. Word Count: ~2,500 

Reason for Choosing:
I chose this text because it is a famous literary work with strong narrative
structure and descriptive language, making it ideal for analyzing word frequency
and grammatical patterns using NLP tools.
"""
import spacy
import requests
import operator

nlp = spacy.load("en_core_web_sm")

def fetch_text(url):
    """Fetch text data from a URL."""
    response = requests.get(url)
    return response.text

def word_tokenization_normalization(text):
    """
    Process text by removing stopwords/punctuation and normalizing words.
    """
    doc = nlp(text)

    words = []
    for token in doc:
        if not token.is_stop and not token.is_punct and token.is_alpha:
            words.append(token.lemma_.lower())

    return words

def word_count(word_list):
    """Count occurrences of each word."""
    counts = {}

    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

    return counts

def print_top_15_frequent_words(word_counts):
    """Display the 15 most frequent words."""
    sorted_words = sorted(word_counts.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    print("\nTop 15 Most Frequent Words:\n")
    for word, count in sorted_words[:15]:
        print(word, ":", count)

def most_common_verbs(text):
    """
    Identify the 10 most common verbs using spaCy POS tagging.
    """
    doc = nlp(text)

    verbs = {}

    for token in doc:
        if token.pos_ == "VERB":
            lemma = token.lemma_.lower()
            verbs[lemma] = verbs.get(lemma, 0) + 1

    sorted_verbs = sorted(verbs.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    print("\nTop 10 Most Common Verbs:\n")
    for verb, count in sorted_verbs[:10]:
        print(verb, ":", count)
 
def main():
    url = "https://www.gutenberg.org/files/11/11-0.txt"

    raw_text = fetch_text(url)

    processed_words = word_tokenization_normalization(raw_text)

    counts = word_count(processed_words)

    print_top_15_frequent_words(counts)

    most_common_verbs(raw_text)

if __name__ == "__main__":
    main()

"""
Word frequency analysis 

The top frequent words in the text I chose, which is Alices Adventures in Wonderland, reflects how the story is driven more by actions and conversations than by long descriptions. Many of
the repeated words relate to thinking, speaking, or moving through different
situations, which matches how Alice is constantly reacting to her new and confusing
experiences. The story contains a handful of dialogue so it would makes sense that we are seeing
action-focused communication words. These results reassure the fictional narrative that is
centered on interaction and curiosity rather than setting or storytelling details. One surprising thing is that specific character names are not as frequent as I expected because the process uses meaningful verbs and ideas instead of just repeating names. While word frequency alone cannot capture the playful tone of the story, it does reveal the text’s emphasis on dialogue exploration, questioning, and constant change in Alice’s story.  

Extended analysis 

Looking specifically at the verbs shows how active and dialogue heavy the story
really is. The most common verbs, including “say,” “go,” “think,” “know,” and
“look,” suggest that the narrative is built around conversation and Alice’s
personal reactions to what she encounters. The high frequency of “say” especially
confirms that characters drive the story through speech rather than through a narration.
Verbs like “go” and “begin” also reinforce the sense of movement and transition that comes in a story like this one.



"""