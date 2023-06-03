

## BackEnd for ReciBook

This project provides the backend for the Recibook. It has different models such as Recipeposts, Recipecomments etc which can be used by the front end¨for data retrieval.This project provides the backend api for the front end.

## Database Model
![Database Model](media/P5%20Database%20Model.png)


## Manual Testing for Back-End
User stories:
* Creation of the posts: As a developer I can create the posts and receive it in the my backend Recipeposts model
  * Result:Pass, I was able to create a post and was also found in the backend

* Editing of the posts:As a developer I can edit my posts and see those changes in the backend as well
  * Result:Pass, i could see the relevant changes in the backend

* Deleting of the posts: As a developer I can delete the posts and found these posts no more in the backend section
  * Result:Pass, I was able to delete a post and this recipes/post were also not found in the backend

* Receiving of all Recipes from the backend: As a developer, I was able to receive all the recipes from the backend
  * Result:Pass, it was possible to receive all the recipesfrom the backend

* Signup: As a developer i could signup and find the same user in the backend
  * Result:Pass, this was posible to find the same user in the backend as well

* Signin: As a developer, i could sign in and and access the relevant data from the backend
  * Result:Pass, i was able to signin and acess the data from the backend 


## Setup 
Making a Local Clone
Log in to GitHub and locate the GitHub Repository Under the repository name, click "Clone or download". To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. Open Git Bash Change the current working directory to the location where you want the cloned directory to be made. Type git clone, and then paste the URL you copied in Step 3. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY Press Enter. Your local clone will be created. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

Cloning into CI-Clone... remote: Counting objects: 10, done. remote: Compressing objects: 100% (8/8), done. remove: Total 10 (delta 1), reused 10 (delta 1) Unpacking objects: 100% (10/10), done. Running it from the github

After cloning the repo please run the following command to include all the neccesary apps in requirement.txt

pip install -r requirements.txt

and include the env.py file which should look like this and the user has to fill in these values
emote Heroku Deployment:
Create an account at Heroku.

Download CLI here.

Open up CMD (Windows) or Terminal (MacOS) and type the following and follow the instructions that appear.

heroku login Create a new Heroku app using the following code in your terminal: heroku create app-name-here With the Heroku app name you just created, modified the production.py file in the settings folder and update the following: ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1', 'localhost'] Open the Heroku apps webpage and click the app you created in Step 4.

Navigate to the Settings tab on the top horizontal bar, we will be adding the required environment variables here.

Click the 'Reveal Config Vars' button and add the below variables for the backend:
![Heroku vars](media/Heroku%20vars.png)


and the env.py file for the backend can look like this
![env.py parameteres](media/env%20example.png)

### API testing
- As I have created several posts i am able to call my api and all those posts from api and and read them
- As i have several posts in backend API I am able to call them view (in the view recipe, once i am logged in) them as well 
  as edit them from my api





