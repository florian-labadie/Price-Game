import requests
from bs4 import BeautifulSoup

def get_recipes(query, max_recipes=10):
    url = f'https://www.marmiton.org/recettes/recherche.aspx?aqt={query}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page : {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    recipes = []
    for recipe in soup.find_all('div', class_='recipe-card-algolia', limit=max_recipes):
        title_tag = recipe.find('h4', class_='recipe-card__title')
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        
        recipe_link = recipe.find('a', href=True)['href']
        if recipe_link.startswith('/'):
            recipe_url = f"https://www.marmiton.org{recipe_link}"
        else:
            recipe_url = recipe_link
        
        recipe_response = requests.get(recipe_url)
        if recipe_response.status_code != 200:
            print(f"Erreur lors de la récupération de la recette : {recipe_url}")
            continue
        
        recipe_soup = BeautifulSoup(recipe_response.text, 'html.parser')
        
        ingredients_list = recipe_soup.find_all('div', class_='card-ingredient')
        ingredients = [ingredient.get_text(strip=True) for ingredient in ingredients_list]
        
        recipes.append({'title': title, 'ingredients': ingredients})
        
        if len(recipes) >= max_recipes:
            break
    
    if recipes:
        print("Recettes extraites :")
        for recipe in recipes:
            print(f"Title: {recipe['title']}")
            print("Ingredients:")
            for ingredient in recipe['ingredients']:
                print(f" - {ingredient}")
    else:
        print("Aucune recette trouvée avec les critères donnés.")
    
    return recipes
