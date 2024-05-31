def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))




from sets_categories_data import ALCOHOLS

def check_drinks(drink_name, drink_ingredients):
    intersec=set(drink_ingredients).intersection(ALCOHOLS)
    if intersec==set():
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"

