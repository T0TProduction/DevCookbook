from enum import Enum


class RecipeCategory(Enum):
    APPETIZER = "appetizer"
    ENTREE = "entree"
    MAIN = "main"
    DESSERT = "dessert"
    OTHER = "other"