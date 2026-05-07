
import streamlit as st
from views.recommandation_page import RecipeRecommenderUI
from controllers.controller import RecipeRecommenderController
from model.Recommandation_entite import RecipeRecommenderModel

@st.cache_resource
def load_model():
    return RecipeRecommenderModel("recipes_clean.csv")

model = load_model()
controller = RecipeRecommenderController(model)

ui = RecipeRecommenderUI()
inputs = ui.render()

controller.process(inputs)