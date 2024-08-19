from src.recette_scraper import get_recipes
from src.nutrition_calculator import calculate_nutrition
from src.preference_manager import add_preference

def main():
    query = input("Enter ingredients: ")
    # new_preference = input("Enter a new dietary preference (e.g., vegetarian): ")
    
    recipes = get_recipes(query)
        
    # Extraire tous les ingrédients de toutes les recettes
    all_ingredients = []
    for recipe in recipes:
        all_ingredients.extend(recipe['ingredients'])

    # Calculer les calories totales
    total_calories = calculate_nutrition(all_ingredients)
    
    # add_preference(new_preference)
    # print(f"Total Calories: {total_calories}")

if __name__ == "__main__":
    main()
