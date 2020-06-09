import configparser
from peewee import *
import datetime 

# todo : move to utility class
config = configparser.ConfigParser()
config.read(r'../AppConfig.ini')
dbLocation = "../" + config['Main']['DbLocation']
db = SqliteDatabase(dbLocation)


class BaseModel(Model):
    class Meta:
        database = db
    
# region core model
class Recipe(BaseModel):
    runTime = DateTimeField()
    created_date = DateTimeField(default=datetime.datetime.now)


class IngredientType(BaseModel):
    action_type = TextField()
    application_type = TextField()


class Ingredient(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='ingredients')
    ingredient_type = ForeignKeyField(IngredientType, backref='ingredientTypes')
    comment_text = TextField()
    title_text = TextField()
# endregion 

# region app config
class HeartBeatLog(BaseModel):
    heart_beat = DateTimeField()


class SystemExceptions(BaseModel):
    message = TextField()
    message_from = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
# endregion