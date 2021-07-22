# Assessment 4: Django
- **Craigslist Jr**


## Rules / Process
- This test is fully open notes and open internet, but is not to be completed with the help of other students/individuals
- Do not open a pull request until Saturday at 8am.

## Requirements
- This assessment must be completed using Django. 
- You may use either SQLite3 or PostgreSQL for your database. (SQLite3 preferred)
- You can use either class or functional views

## Challenge
Everyone loves going on Craigslist to find interesting people and interesting items. The joy of Craigslist is that it doesn't upgrade itself to stay up to date with the times - it's the same old Craigslist that everyone knows and loves. The core schema has also remained relatively unchanged over the years. Today, you will build a basic Craigslist CRUD app with nested routes. We will call this site: Craigslist Junior.

Here are a list of the routes you will need to build:
- `/categories`: A page listing all the categories
- `/categories/new`: A page with a form to create a new category
- `/categories/:category_id`: A page to view the detail of a specific category and a list of all of its associated posts
- `/categories/:category_id/edit`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
- `/categories/:category_id/delete`: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
- `/categories/:category_id/posts/new`: A page with a form to create a new post, under the current category by default.
- `/categories/:category_id/posts/:post_id`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/:category_id/`)
- `/categories/:category_id/posts/:post_id/edit`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
- `/categories/:category_id/posts/:post_id/delete`: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.

NOTE: For creating, updating, or deleting data... all actions should automatically redirect to another appropriate page, if successful, or display an error message if unsuccessful.