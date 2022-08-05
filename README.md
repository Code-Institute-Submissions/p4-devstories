# Introduction
Devstories is a blog site for developers kinda like instagram but instead of posting pictures devs can talk about their projects etc and sign up on it and post pictures of their projects if they want to.

- Am I resonsive image here

## User Stories
- A user will be able to sign up on the website as a memember
- A user will be able to post written content on the site
- A user will be able to Edit Update and delete their own post
- A user will be able to Like and Comment on A blog post

# ER diagram

# Wireframes
## Mobile

![BalsamiqWireframes_955zaPLYtz](https://user-images.githubusercontent.com/43074374/179642827-41d3060b-3b33-457e-a81d-18760e198bbf.png)

## Tablet 

![BalsamiqWireframes_MqBanEFTby](https://user-images.githubusercontent.com/43074374/179642969-70eaefb1-9c0a-48b1-b7c6-b56e51ecb592.png)


## Desktop

![BalsamiqWireframes_AuQPsYYN0y](https://user-images.githubusercontent.com/43074374/179643135-b6b56729-cc39-450c-9e99-f42ee4b1ed90.png)

![BalsamiqWireframes_gonOFw2qC1](https://user-images.githubusercontent.com/43074374/179643218-4e8228af-937c-4df1-9885-fe73bf36658f.png)

# Technologies Used
- HTML
- Bootstrap & CSS
- Django 
- Postgres SQL
- Cloudinary 

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

python3 manage.py runsever 

# Steps For setting up skeleton project
- Create the heroku App
- Attach the PostgreSQL Database
- Prepare our enviroment and settings.py file
- Get our static and media files stored on cloudinary

# For testing & Setting up Database stuff
- Migration commands for Setting up the data base
- python3 manage.py runsever
- For testing use, python3 manage.py test
- python3 manage.py test todo.test_forms(name of file at the end)
- pip3 install coverage 
- For setting up the database
- pip3 install psycopg2-binary
- pip3 install gunicorn
- pip3 freeze --local > requirements.txt
- pip3 install dj_database_url
- pip3 install dj3-cloudinary-storage
- python3 manage.py migrate
Affter installing the requirements you need to migrate the changes to the database

