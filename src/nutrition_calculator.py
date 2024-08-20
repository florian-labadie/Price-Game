def calculate_nutrition(ingredients):
    calorie_per_ingredient = {
        'carotte': 41,
        'apple': 52,
        'banana': 89,
    }
    
    total_calories = 0
    for ingredient in ingredients:
        ingredient_name = ingredient.lower().strip()
        calories = calorie_per_ingredient.get(ingredient_name, 0)
        total_calories += calories
    
    return total_calories
