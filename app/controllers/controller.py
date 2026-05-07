class RecipeRecommenderController:

    def __init__(self, model):
        self.model = model

    def process(self, ui_inputs):
        import streamlit as st

        if not ui_inputs["search_clicked"]:
            return

        tags = ui_inputs["tags"]
        ingredients = ui_inputs["ingredients"]
        # name = ui_inputs["name"]
        time = ui_inputs["time"]
        limit = ui_inputs["limit"]

        sort_name = ui_inputs["sort_name"]
        sort_time = ui_inputs["sort_time"]
        sort_tags = ui_inputs["sort_tags"]

        ingredients_list = [
            i.strip() for i in ingredients.split(",") if i.strip()
        ] if ingredients else []

        results = self.model.recommend(
            ingredients_input=ingredients_list,
            max_time=int(time) if time else 9999,
            tag=tags if tags else None,
            top_n=int(limit)
        )

        # if name:
        #     results = results[
        #         results['name'].str.contains(name, case=False, na=False)
        #     ]

        if sort_name == "A → Z 🔼":
            results = results.sort_values("name")
        elif sort_name == "Z → A 🔽":
            results = results.sort_values("name", ascending=False)

        if sort_time == "Croissant 🔼":
            results = results.sort_values("minutes")
        elif sort_time == "Décroissant 🔽":
            results = results.sort_values("minutes", ascending=False)

        if sort_tags == "A → Z 🔼":
            results = results.sort_values("tags")
        elif sort_tags == "Z → A 🔽":
            results = results.sort_values("tags", ascending=False)

        st.subheader("📊 Résultats")

        if results.empty:
            st.warning("Aucune recette trouvée 😢")
        else:
            st.success(f"{len(results)} recettes trouvées ✅")
            st.dataframe(results, use_container_width=True)
            







