import re
import spacy

# load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_details(text):

    doc = nlp(text)

    data = {
        "pet": None,
        "owner": None,
        "location": None,
        "phone": None
    }

    # extract PERSON and LOCATION using spaCy
    for ent in doc.ents:
        if ent.label_ == "PERSON" and data["owner"] is None:
            data["owner"] = ent.text

        if ent.label_ in ["GPE", "LOC"] and data["location"] is None:
            data["location"] = ent.text

    # extract phone number using regex
    phone_match = re.search(r"\b\d{10}\b", text)
    if phone_match:
        data["phone"] = phone_match.group()

    # simple pet detection
    pets = ["dog", "cat", "puppy", "kitten"]
    for pet in pets:
        if pet.lower() in text.lower():
            data["pet"] = pet.capitalize()

    return data