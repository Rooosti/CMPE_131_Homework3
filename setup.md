## Homework 3 CMPE-131
# Setup instructions:

<p>Clone repo<br>
Navigate to folder</p>

run:
```
python3 -m venv venv
source venv/bin/activate
```

install necessary libraries using pip3:
```
pip3 install -r requirements.txt
```

run in terminal:
```
flask shell
from app import db
db.create_all()
exit()
python3 run.py
```

run in terminal to stop virtual environment:
```
deactivate
```

## Website routes:
# Pages:
```
/recipes
```
Shows an unordered list of all the recipes (titles) in the database.

```
/recipe/new
```
Returns a form to add a new recipe.

```
/recipe/<integer>
```
Returns a specific recipe and its details.

```
recipe/<integer>/delete
```
Deletes a recipe from the database.
