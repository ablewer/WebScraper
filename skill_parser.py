"""
Extracts skills using word tokenization,
using the natural-language-processing library "spaCy".
"""
import docx
import pandas as pd
import spacy


def get_skills(resume):
    """Parses a resume in .docx format and returns a list of skills."""
    tokens1 = []
    tokens2 = []
    resume_skills = []

    # load pre-trained model
    nlp = spacy.load('en_core_web_sm')

    # load skill data
    skill_data = pd.read_csv("skills.csv")

    # extract values from skill data
    skills = list(skill_data.columns.values)

    # Load the full text of the resume
    full_resume_text = __get_full_text(resume)

    # Parse the text using the spaCy NLP library
    nlp_text = nlp(full_resume_text)

    # Remove "stop words" (https://en.wikipedia.org/wiki/Stop_words)
    # and run word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]

    # check for single words (one-grams - example: python),
    # and append any that match the skill data to the returned list
    for token in tokens:
        token = token.lower().strip()
        tokens1.append(token)
        if token.lower() in skills:
            resume_skills.append(token)

    # check for noun phrases (bi-grams and tri-grams - example: machine learning),
    # and append any that match the skill data to the returned list
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        tokens2.append(token)
        if token in skills:
            resume_skills.append(token)

    # Use a list comprehension and Python's set data type to return the skills list without duplicates
    return [i for i in set([i for i in resume_skills])]

def __get_full_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

