from deliveryService.rawIngredients import Ingredient, Recipe

ingredientList = []

def Register(ingredient):
    # log setup
    ingredient.Setup()
    ingredientList.append(ingredient)

