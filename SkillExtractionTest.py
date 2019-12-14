"""
Testing a method for extracting skills using word tokenization,
using the natural-language-processing library "spaCy".

After installing the requirements, run the following command to download
a pre-trained language model:
python -m spacy download en_core_web_sm
"""

import os

import docx
import pandas as pd
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

# load skill data
skill_data = pd.read_csv("skills.csv")

# extract values from skill data
skills = list(skill_data.columns.values)

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
    resume_skills = []
    # check for one-grams (example: python)
    for token in tokens:
        token = token.lower().strip()
        tokens1.append(token)
        if token.lower() in skills:
            resume_skills.append(token)

    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        tokens2.append(token)
        if token in skills:
            resume_skills.append(token)

    # print("One-grams:")
    # print(tokens1)
    # print()


    print("Detected skills for " + resume + ":")
    print([i for i in set([i for i in resume_skills])]);
    print()

    print("Detected noun phrases: (Bi-grams/tri-grams):")
    print(tokens2)
    print("======\n")

    # TODO: match the above results against a list of possible technical skills