import streamlit as st


class RecipeRecommenderUI:

    def __init__(self):
        self.max_limit = 50  # limite max pour les résultats

    def render(self):
        st.set_page_config(page_title="Recipe Recommender", layout="wide")

        st.title("Systeme de recommandation des recettes")

        # ===================== INPUTS =====================
        st.subheader("🔍 Recherche")

        col1, col2, col3 = st.columns(3)

        with col1:
            tags = st.text_input("Categorie (diner, dejeuner)")

        with col2:
            ingredients = st.text_input("Ingrédients (séparés par des virgules)")


        col4, col5 = st.columns(2)

        with col4:
            time = st.number_input("Temps max (minutes)", min_value=0, step=5)

        with col5:
            limit = st.number_input(
                "Nombre de résultats",
                min_value=1,
                max_value=self.max_limit,
                value=5
            )

        search_button = st.button("🔎 Voir les recommandations")

        # ===================== FILTRES =====================
        st.subheader("⚙️ Filtres")

        col6, col7, col8 = st.columns(3)

        with col6:
            sort_name = st.selectbox(
                "Nom",
                ["A → Z 🔼", "Z → A 🔽"]
            )

        with col7:
            sort_time = st.selectbox(
                "Temps de cuisson",
                ["Croissant 🔼", "Décroissant 🔽"]
            )

        with col8:
            sort_tags = st.selectbox(
                "Catégories",
                ["A → Z 🔼", "Z → A 🔽"]
            )

        # ===================== RESULTATS =====================
        st.subheader("📊 Résultats")

        # Table vide pour l'instant (pas d'implémentation)
        st.empty()

        # ===================== RETOUR DES VALEURS =====================
        return {
            "tags": tags,
            "ingredients": ingredients,
            "time": time,
            "limit": limit,
            "sort_name": sort_name,
            "sort_time": sort_time,
            "sort_tags": sort_tags,
            "search_clicked": search_button
        }