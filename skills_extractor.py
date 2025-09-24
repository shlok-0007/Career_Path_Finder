import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import json

# Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# Load the skill dataset (you can load it from a file or database)
with open('skills.json') as f:
    skills_dataset = json.load(f)

def extract_skills_from_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Extract skills by matching tokens with the predefined skills dataset
    extracted_skills = set()
    for skill in skills_dataset:
        if skill.lower() in filtered_tokens:
            extracted_skills.add(skill)
    
    return list(extracted_skills)
