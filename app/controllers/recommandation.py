import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

recipes_clean = pd.read_csv("recipes_clean.csv")

# nettoyage sécurité
recipes_clean = recipes_clean.fillna("")

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(recipes_clean['recombined_text'])


def recommend_recipes(ingredients_input, max_time=60, tag=None, top_n=5):

    input_text = " ".join(ingredients_input)
    input_vec = vectorizer.transform([input_text])
    similarity = cosine_similarity(input_vec, tfidf_matrix)[0]

    filtered = recipes_clean.copy()
    filtered['score'] = similarity

    filtered = filtered[filtered['minutes'] <= max_time]

    if tag:
        filtered = filtered[
            filtered['tags'].str.contains(tag, case=False, na=False)
        ]

    results = filtered.sort_values(by='score', ascending=False)

    return results[['name', 'ingredients', 'minutes', 'tags', 'score']].head(top_n)
    
    
    