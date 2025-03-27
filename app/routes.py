from app import app_obj
from flask import render_template
from flask import redirect
from app.forms import RecipeForm
from app.models import Recipe
from app import db

#Recipes page
#returns an ordered list of every recipe with each recipe being represented as a title
#see __repr__ in Recipe class within ./models.py
@app_obj.route("/recipes")
def recipes_page():
    all_recipes = db.session.query(Recipe).all()
    return render_template("recipes.html", all_recipes=all_recipes)

#Recipe creation page
#Asks the user to fill 4 text fields for a new recipe's title, description, ingredients, and instructions (form)
#creates an object "new_recipe" and commits it to the database
#redirects the user to the /recipes URL page
@app_obj.route("/recipe/new", methods=['GET', 'POST'])
def new_recipe_form():
    form = RecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
        )
        db.session.add(new_recipe)
        db.session.commit()
        return redirect("/recipes")
    return render_template("recipe_form.html", form=form)

#searches and returns a single recipe on the page based on the URL <integer> parameter as the key
@app_obj.route("/recipe/<integer>")
def show_recipe(integer=0):
    recipe_to_show = db.session.query(Recipe).get(integer)
    if (recipe_to_show):
        return render_template("single_recipe.html", recipe=recipe_to_show)

#Locates and deletes a recipe from the database based on the URL <integer> parameter as the key
#redirects the user to the /recipes URL page after
@app_obj.route("/recipe/<integer>/delete")
def delete_recipe(integer=0):
    recipe_to_delete = db.session.query(Recipe).get(integer)
    if recipe_to_delete:
        db.session.delete(recipe_to_delete)
        db.session.commit()
    return redirect("/recipes")
