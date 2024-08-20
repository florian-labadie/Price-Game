from src.recette_scraper import get_recipes
from src.nutrition_calculator import calculate_nutrition

def main():
    query = input("Enter ingredients: ")
    
    recipes = get_recipes(query)
        
    # Extraire tous les ingrédients de toutes les recettes
    all_ingredients = []
    for recipe in recipes:
        all_ingredients.extend(recipe['ingredients'])

    # Calculer les calories totales
    total_calories = calculate_nutrition(all_ingredients)
    
    print(f"Total Calories: {total_calories}")

if __name__ == "__main__":
    main()
