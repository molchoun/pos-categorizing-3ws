import pandas as pd

from scrape import fetch_article_text
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')


def get_pos(word_tags):
    pos = {}
    for word, tag in word_tags:
        if tag in ['NN', 'NNS', 'NNP', 'JJ']:
            if tag not in pos:
                pos[tag] = [word]
            else:
                pos[tag].append(word)

    df = {'Tags': [], 'Words': [], 'Count': []}

    for k in pos:
        df['Tags'].append(k)
        df['Words'].append(" ".join(pos[k]))
        df['Count'].append(len(pos[k]))

    return pd.DataFrame(df)


def main():
    url = "https://www.hindustantimes.com/world-news/air-raid-alerts-issued-throughout-ukraine-explosions-reported-101682646645985-amp.html"
    text = fetch_article_text(url)
    tokenized_text = word_tokenize(text)
    tagged_text = pos_tag(tokenized_text)
    df = get_pos(tagged_text)
    print(df)


if __name__ == "__main__":
    main()
