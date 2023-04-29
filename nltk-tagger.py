import spacy
nlp = spacy.load('en_core_web_sm')


def get_subj(doc):
    who = []
    for token in doc:
        if ("subj" in token.dep_):
            who.append(str(doc[token.left_edge.i:token.right_edge.i+1]))
    return who


def get_vb(doc):
    what = []
    for token in doc:
        if token.pos_ == "VERB" and token.dep_ == 'ROOT':
            start = list(token.children)[1].i
            end = list(token.children)[-1].i
            what.append(str(doc[start:end]))
    return what


def get_advcl(doc):
    how = []
    for token in doc:
        if ("advcl" in token.dep_):
            how.append(str(doc[token.left_edge.i:token.right_edge.i+1]))
    return how


def main(doc):
    who = get_subj(doc)
    what = get_vb(doc)
    how = get_advcl(doc)
    print(f"Who: {who}\nWhat: {what}\nHow: {how}")


if __name__ == "__main__":
    text = "Ten police personnel and a civilian driver were killed after Naxals blew up a vehicle that was part of a convoy carrying security personnel in Chhattisgarh's Dantewada district on Wednesday. CM Bhupesh Baghel will today attend the wreath-laying ceremony of the personnel."
    doc = nlp(text)
    main(doc)
