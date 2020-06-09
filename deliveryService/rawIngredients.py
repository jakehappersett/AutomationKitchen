from enum import Enum 

class IngredientState(Enum):
    Initializing = 1


class Ingredient:
    def __init__(self, state, ingredient_type, action, media_title, post_title, comment):
        self.state = state
        self.type = ingredient_type  # reddit, twitter etc
        self.action = action # post, comment
        self.media_title = media_title
        self.post_title = post_title
        self.comment = comment # nullable, should only be expected for comment type ingredients

    def Setup(self):
        pass

    def Execute(self):
        pass


class Recipe:
    def __init__(self, runTime, ingredients):
        self.runTime = runTime
        self.ingredients = ingredients


class Reddit_Ingredient(Ingredient):
    def Setup(self):
        # do reddit api things that need to be done 
        pass 

    def Execute(self):
        # do reddit posting
        pass