"""
Testing a method for extracting skills using word tokenization,
using the natural-language-processing library "spaCy".

After installing the requirements, run the following command to download
a pre-trained language model:
python -m spacy download en_core_web_sm
"""

import os

import docx
import spacy

def getText(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# load pre-trained model
nlp = spacy.load('en_core_web_sm')
# noun_chunks = nlp.noun_chunks

fileNames = []
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith("Resume.docx"):
            fileNames.append(filename)

for resume in fileNames:
    full_resume_text = getText(resume)
    # print(full_resume_text)

    nlp_text = nlp(full_resume_text)

    # removing "stop words" (https://en.wikipedia.org/wiki/Stop_words)
    # and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    # print(tokens)

    tokens1 = []
    tokens2 = []
    # check for one-grams (example: python)
    for token in tokens:
        tokens1.append(token)

    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        tokens2.append(token)

    print("One-grams:")
    print(tokens1)
    print()
    print("Bi-grams/tri-grams:")
    print(tokens2)
    print("======")

    # TODO: match the above results against a list of possible technical skills