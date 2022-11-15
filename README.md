# Description of Project

App Squared is a Job Application tracking app, where users input information about their Job Applications and App^2 will store the information and allow users to view a dynamic feed that will show users when they applied, the Job title, company and the status. This dynamic feed will also allow users to sort by days since applied (Ascending and Descending order) and status, as well as allow users to search their database of applications by title, company, and where they applied. This repo reflects the server, or back end, of this app. 

# Screenshot of my APP
<img width="1168" alt="Screen Shot 2022-11-15 at 12 01 18 PM" src="https://user-images.githubusercontent.com/107736662/201992756-4a1233d8-2d14-4bae-9da9-4b8550f41941.png">
<img width="1176" alt="Screen Shot 2022-11-15 at 12 02 46 PM" src="https://user-images.githubusercontent.com/107736662/201992940-18f20e4e-5efb-4f30-80f7-6c9d9f9370cb.png">
<img width="1181" alt="Screen Shot 2022-11-15 at 12 03 09 PM" src="https://user-images.githubusercontent.com/107736662/201993025-5b2f152e-fd1b-4a1a-8127-fafb6987a8e7.png">


# List of Technologies used:

## (Frontend)
- HTML
- CSS
- Javascript
- REACT
- Bootstrap
 
## (Backend)
- Python 
- Django

# Unlearned Technology:
- Bootstrap - Modals / Cards
- Django - User Authentication 


# Installation instructions

- Go to the website: [https://appsquared-db.herokuapp.com/]
- Click on the Menu and Sign Up (If you've signed up already, there is a link to login in the top right)
- Input your info and log in.


# User Stories

- AAU I want an app that will hold informations on all of the applications I've submitted
- AAU I want my homepage to contain recent applications I've put in
- AAU I on my home page I want each application to be represented by a card that displays the main application information and a field that displays how many days it's been since I applied
- AAU I want each card to be a link that will allow users to be either redirected to a page that holds all of the application information (can be modal)
- AAU I want to be able to have dynamic control over the sorting of the feed that holds application cards on my home page
- AAU I want to also be able to search my applications by job title / job application ID / Company
- AAU I want to be able to sort job applications

# Wireframes

![](https://user-images.githubusercontent.com/100657239/200192547-b75cb0e0-dc97-4195-b288-b0142bbf0955.png)
![](https://user-images.githubusercontent.com/100657239/200192660-9fb9b6ab-1020-42b1-aa9e-b94f150e2919.png)


# Unsolved problems/Major hurdles:

Unsolved Problems:

- The contact model is not fully navigable at deploy, but the work for it has begun.
- We'd like to revisit the user model in order to implement Profiles for users through the site, as it could allow for user to user interactivity. At the moment, there is some potential to build / customize user profiles, but we didn't reach that far into stretch goals.
- Token destruction is kind of shaky at the moment; there are bugs that might be related to this, but it will require further testing.

Major Hurdles:

- React FrontEnd w/ Django backend
- Heroku Deployment Issues
- DJANGO
- Restructuring from planning stage/ changing the approach
- Scheduling issues
- Compartmentalization of features/tasks
