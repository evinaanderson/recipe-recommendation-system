import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecipeRecommenderModel:

    def __init__(self, data_path, max_features=5000):
        self.data_path = data_path
        self.max_features = max_features

        self.recipes = None
        self.vectorizer = None
        self.tfidf_matrix = None

        self.load_data()
        self.prepare_model() 

    # ===================== CHARGEMENT =====================
    def load_data(self):
        try:
            self.recipes = pd.read_csv(self.data_path)
        except Exception as e:
            raise Exception(f"Erreur chargement dataset: {e}")

    # ===================== PREPARATION =====================
    def prepare_model(self):
        try:
            # Vérification colonnes
            required_cols = ['name', 'ingredients', 'tags', 'minutes', 'recombined_text']
            for col in required_cols:
                if col not in self.recipes.columns:
                    raise Exception(f"Colonne manquante: {col}")


            # TF-IDF
            self.vectorizer = TfidfVectorizer(
                stop_words='english',
                max_features=self.max_features
            )

            self.tfidf_matrix = self.vectorizer.fit_transform(
                self.recipes['recombined_text']
            )

        except Exception as e:
            raise Exception(f"Erreur préparation modèle: {e}")

    # ===================== RECOMMANDATION =====================
    def recommend(self, ingredients_input=None, max_time=60, tag=None, top_n=5):

        if ingredients_input is None:
            ingredients_input = []

        # Texte utilisateur
        input_text = " ".join(ingredients_input)

        # Transformation TF-IDF
        input_vec = self.vectorizer.transform([input_text])

        # Similarité
        similarity = cosine_similarity(input_vec, self.tfidf_matrix)[0]

        # Copie des données
        results = self.recipes.copy()
        results['score'] = similarity

        # Filtrage temps
        results = results[results['minutes'] <= max_time]

        # Filtrage tag
        if tag:
            results = results[
                results['tags'].str.contains(tag, case=False, na=False)
            ]

        # Tri par score
        results = results.sort_values(by='score', ascending=False)

        # Résultat final
        return results[['name', 'ingredients', 'minutes', 'tags', 'score']].head(top_n)
        
    