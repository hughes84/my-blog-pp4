# Nurtition 2023 - Nutrition Blog

"mock-up"

![GitHub last commit](https://img.shields.io/github/last-commit/hughes84/my-blog-pp4?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/hughes84/my-blog-pp4?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/hughes84/my-blog-pp4?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/hughes84/my-blog-pp4?color=green)
<hr>

## Table of Contents

- [Overview](#overview)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Project Goal](#project-goal)
- [Project Objectives](#project-objectives)
- [Design](#design)
- [Skeleton](#skeleton)

## Overview
This is a project designed and developed to create a friendly atmosphere for those looking to talk nutrition, providing clients with professional, evidence-based nutrition support that they can implement easily, to make long term sustainable changes. It allows the user to learn from professionals as well as gain ideas, tips and support from other users. There is a recipes section where the user can learn how to make simple, quick and healthy snacks and meals with simple ingredients and step by step methods.<br>

**Nurtition 2023** - Nutrition Blog was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://nutrition2023-ea03d13919e5.herokuapp.com/).<br><br>

[Back to Table of Contents](#table-of-contents)

# UX
This website was created using the Five Planes Of Website Design<br>

**User Stories**

User stories can be viewed here on the project [kanban board ](https://github.com/users/hughes84/projects/1)

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily navigate through website content |             
|                                       |1B| As a user, I want to know what the website is about without having to do too much reading|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the blog's theme|
|**USER REGISTRATION**                  |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|                                       |2D| As a user, I want to know that I've logged out successfully|
|**BLOGS**                              |  ||
|                                       |3A| As a logged-in user, I want to be able to see relevant blogs clearly|
|                                       |3B| As a logged-in user, I want to be able to select a blog and comment and/or like selected blog|
|                                       |3C| As a logged-in user, I want to be able to delete my own previous comments|
|**RECIPES**                            |  ||
|                                       |4A| As a user, I want to see the recipes individual overview clearly|
|                                       |4B| As a user, I want to be able to access ingredients and methods|
|                                       |4C| As a logged-in user, I want to be able to navigate through different recipes easily|
|**ADMINISTRATION**                     |  ||
|                                       |5A| As a logged-in admin member, I want to be able to access the admin page|
|                                       |5B| As a logged-in admin member, I want to be able to authenticate and authorise comments and posts|
|                                       |5C| As a logged-in admin member, I want to be able to publish new recipes|
|                                       |5D| As a logged-in admin member, I want to be able to create a new user, recipes, author and categories|
|                                       |5E| As a logged-in admin member, I want to be able to delete users, recipes, authors, categories and comments|
|**CONTACT**                            |  ||
|                                       |6A| As a user, I want to be able to contact the site with ease|
|                                       |6B| As a user, I want to get a reply that my messgae has been received|
|                                       |6C| As a user, I want to see contact information on the website|

[Back to Table of Contents](#table-of-contents)

**Project Goal:**

To create a blog for those with an interest in nutrition, seeking guidance, information tips or discuss their own experiences and ideas with others and staff members as well.

**Project Objectives:**

* To create a website with a simple and intuitive User Experience;
* To add content that is relevant to the topic and helps create a better understanding;
* To be able to differentiate between client and staff member accounts;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the blog features;
* To make the website responsive and functional on different devices.<br><br>

[Back to Table of Contents](#table-of-contents)

## Design

#### Colours

* The colour scheme is kept simple by opting mainly for a combination of white text set against the dark backgrounds and black text against the white backgrounds. For the navbar, I selected a bright colour from Bootstrap to highlight the site name as well as encouraging the surrounding colours. The social links and nav bar selections change colour when hovered over to highlight selection. The footer follows suit with this method. Throughout the site the user will see bright, welcoming colours like this when hovering over certain sections as well as colourful buttons on each page.

#### Typography

* The Roboto font is used as the main font for the whole project.

[Back to Table of Contents](#table-of-contents)

#### Imagery

* All images on the site are related to the recipes, blogs and website design. There are 3 static images throughout the site. The remaining images will be uploaded by the author to the database.

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile were created with [Miro]() tool and can be viewed below:<br>

<details>
  <summary>Wire Frames</summary>
  <h4>Home page</h4>
  <img src="docs/readme-images/wireframe-home.png"><br>
  <h4>About page</h4>
  <img src="docs/readme-images/wireframe-about.png"><br>
  <h4>About more</h4>
  <img src="docs/readme-images/wireframe-aboutmore.png"><br>
  <h4>Blog page</h4>
  <img src="docs/readme-images/wireframe-blog.png"><br>
  <h4>Blog user comments</h4>
  <img src="docs/readme-images/wireframe-comments.png"><br>
  <h4>Recipes</h4>
  <img src="docs/readme-images/wireframe-recipe.png"><br>
  <h4>Recipe details</h4>
  <img src="docs/readme-images/wireframe-recipedetail.png"><br>
  <h4>Contact us</h4>
  <img src="docs/readme-images/wireframe-contactpage.png"><br>
  <h4>Submit message</h4>
  <img src="docs/readme-images/wireframe-contactmsg.png"><br>
  <h4>User profile</h4>
  <img src="docs/readme-images/wireframe-profile.png"><br>
  <h4>Sign in</h4>
  <img src="docs/readme-images/wireframe-signin.png"><br>
  <h4>Sign up</h4>
  <img src="docs/readme-images/wireframe-signup.png"><br>
</details>
</details><br>

[Back to Table of Contents](#table-of-contents)

**FLOWCHARTS**<br>
The Flowchart for my program was created using <b>[draw.io](https://app.diagrams.net/)</b> and it visually represents how the system works.<br>
<img src="docs/readme-images/flowchart.png"><br>
<br><br>

### Surface<hr>
#### Colour Scheme
* The primary colour scheme was used for body, headers and nav elements<br> 
<img src="docs/readme-images/primary-green.png" width="30%">
<img src="docs/readme-images/primary-white.png" width="30%">
<img src="docs/readme-images/primary-black.png" width="30%">
<img src="docs/readme-images/primary-grey.png" width="30%">
<img src="docs/readme-images/primary-orange.png" width="30%">
<br>

* The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.<br>
<img src="docs/readme-images/secondary-blue.png" width="30%">
<img src="docs/readme-images/secondary-gray.png" width="30%">
<img src="docs/readme-images/secondary-green.png" width="30%">
<img src="docs/readme-images/secondary-lightblue.png" width="30%">

[Back to Table of Contents](#table-of-contents)

#### Visual Effects
* **Box shadows** <br>
Multiple box shadows were used for the cover, buttons and images. <br>
* **Animation**<br>
Some animations were used for creating a dynamic and attractive design

## Features

### Home Page

![Home Page](docs/readme-images/screen-home.png)

* The hero image welcomes the user with a short message advertising what the website is about. There is a nutrition 
themed image in the background and a button that takes the user straight to the blogs page.<br>

