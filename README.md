# Dessert Island

[View published site on Heroku](https://p4-dessert-island.herokuapp.com/).

![](#)

Image from [Am I Responsive](http://ami.responsivedesign.is/).

## Project Overview

Dessert Island is a website that aims to provide a blog-style recipe website for various desserts which user can view and interact with via comments and likes by signing up and creating an account or logging into and existing one. This site has been created as part of my Portfolio Project 4 for Code Institute.

## Table of Contents

1. [User Experience (UX)](#ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Design](#design)
        * [Colours](#colours)
        * [Typography](#typography)
        * [Imagery](#imagery)
    * [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
2. [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
3. [Technologies Used](#tech-used)
4. [Testing](#testing)
    * [User Stories Testing](#user-testing)
    * [Validation Testing](#validation-testing)
    * [Known Issues and Resolutions](#issues)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX) <a name="ux"></a>

## Strategy <a name="strategy"></a>

### Project Goals <a name="project-goals"></a>

The main business goal for Dessert Island is to provide users with a blog-style website with various dessert recipes accessible for the user to view. The user can create an account to be able to further interact with these blog posts via likes and adding comments. 

The main target audience for this website are cooking/baking and dessert fanatics who enjoy experiencing new type of desserts and following recipes coming from different levels of background with their cooking/baking skills. This is also a website for users to be able to share their comments and reviews of the recipes with the community.


### User Stories <a name="user-stories"></a>

* __Site User Goals:__

  * As a Site User I can like or unlike a post so that I can interact with the content
  * As a Site User I can leave comments on a post so that I can be involved in the conversation
  * As a Site User I can register an account so that I can comment and like
  * As a Site User/Admin I can view comments on an individual post so that I can read the conversation
  * As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral
  * As a Site User I can click on a post so that I can read the full text
  * As a Site User I can view a list of posts so that I can select one to read
  * As a Site User I can locate their social media accounts so I can receive updates and see their following and how well they are known and reliable
  * As a Site User I can navigate easily through the site and find the relevant information with ease
  * As a Site User I can learn more about the site the purpose of the web app
  * As a Site User I can search keywords for specific recipes


* __Site Owner Goals:__

  * As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
  * As a Site Admin I can create draft posts so that I can finish writing the content later
  * As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
  * As a Site User/Admin I can view comments on an individual post so that I can read the conversation
  * As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral
  * As a Site Admin I can prevent unauthorised users from having access so that they cannot access admin content or other users' profiles


## Scope <a name="scope"></a>

To achieve the strategy goals, I want to implement the following features:

* A navigation bar fixed at the top of the screen which will allow the user to easily navigate and find the relevant sections.
* A Home section which will allow the user to find out about the website and view posts.
* An About Us page to inform the user about this website.
* A Login page for existing users to access their account to allow to like and add comments.
* A Register/Signup page to allow new users to create an account.
* A Blog post page to view the selected post in more detail for the recipes and add comments/like the post.
* A Search bar to allow users to enter specific keywords to be able to locate desired recipes.
* A Footer located at the bottom of the website which allows the user to access social media links.
* A fully responsive design that will work on different devices including desktop, tablets, and mobile devices, allowing users to access the site anytime and anywhere.


## Design <a name="design"></a>

### Colours <a name="colours"></a>

I have used white for the overall background colour for the website, accompanied by black and #212529 for the header and footer to notably distinguish this from the main content. 

For the text, black has been used against the white background and white has been used against the black header and footer. This opposite contrast has been chosen for ease of visibility, so users are able to read the text without any additional difficulty.

In addition, rgb(214, 170, 255) has been used as a complementing accent to the website for the logo and hover links without causing any distractions to the user viewing the website.


### Typography <a name="typography"></a>

The fonts were obtained from [Google Fonts](https://fonts.google.com/).

For my logo text I have used Pacifico.

For the heading text I have used Poppins.

For the main text I have selected Montserrat which complements the font used for my headings and logo. 

I have avoided using overly stylised fonts, which can be difficult to read for users, therefore ensuring the website is more accessible to users with visual impairments.

In the event the font fails to load, I have used sans-serif as a back-up font.


### Imagery <a name="imagery"></a>

Images are obtained from the [Freepik](https://www.freepik.com/), [Unsplash](https://unsplash.com/) and [BBC Good Food](https://www.bbcgoodfood.com/) websites.

I have used imagery appropriate to the website’s content to provide a more visual experience to the user.

Please see further details in the __Credits__ section for the specific images used within the project.


## Skeleton <a name="skeleton"></a>

### Wireframes <a name="wireframes"></a>

Wireframes were created using [Balsamiq Wireframes](https://www.balsamiq.com/).

The wireframes have examples of desktop, tablet, and mobile phone displays.

* [Home](docs/images/home.png)
* [About Us](docs/images/about-us.png)
* [Blog Post](docs/images/blog-post.png)
* [Register](docs/images/register.png)
* [Login](docs/images/login.png)

Overall, the finished project design is similar to what I had originally intended to create as per my wireframes. However, there are some different choices I have made for the end website such as:

* I have decided to remove the 'Recipes' section from the nav as per the original wireframes. The original intention was that a user can click on this and will be taken to a new page where they are able to view all the posted recipes. However, this was a redundant idea as the posts were already displayed on the 'Home' page. Therefore, for final submission I opted for a search bar to replace this. The user instead can utilise the search bar to locate specific recipes with the use of keywords which in return will present recipes (if any found).

* There are also some minor differences on the blog post section with the arrangement of the content. 


## Features <a name="features"></a>

### Current Features <a name="current-features"></a>

For this project I opted for a website with different pages accessed by clicking the nav links, this is fully responsive and consists of a header, footer and the following main sections; Home, About Us, Blog Post, Sign Up, Login and Search.

__Navigation__:

* This feature is present on all the pages/sections and is fixed to the top.
* The header section has a fully responsive navigation bar which consists of the logo, located on the left-hand side.
* The navigation buttons for Home, About Us, Sign Up, Login (located left-hand side after the logo) and a Search bar (located on the right-hand side).
* Style has been applied to the logo and buttons on the left-hand side so the user is able to hover over these to signify that the links can be clicked.
* The Search bar has placeholder text to indicate to the user that they can enter text in the box provided. 
* Style has also been applied to the search button next to the input box to indicate to the user that this has been selected and can be clicked.

__Home__:

* This is the default page displayed when the user accesses the website.
* This page can also be viewed by clicking the Dessert Island logo or the home button from the navigation.
* An introductory message displayed to the user.
* Recipe blog posts displayed (max of 6) per page.
* There is a 'Next' button that allows user to click and navigate to the next page to view more recipes.
* Alternatively 'Prev' button can be clicked to return a page back.
* Recipe blog posts are displayed from most recent to oldest.
* Each post is displayed in a card style with an image, author, date, title and like count.
* Style has been applied so the user can hover over the text for the posts which will underline to indicate that this can be selected.
* Selecting the clickable text will take the user to the 'Blog Posts' page to display the full content of the recipe post.

__About__:

* User can access this section by clicking the 'About' button from the navigation.
* A parallax header image added at the top (after the navigation).
* User is able to scroll further down the page and access the text which provides more detail about the website and it's purpose.
* For new users, a sign up link is also within the text which will take them to the 'Sign Up' page and allow the user to create an account.

__Blog Post__:

* Accessed once the user selects a recipe post from the 'Home' or 'Search' page.
* Recipe title and image displayed at the top (image is not displayed on smaller devices).
* Content is then followed by the ingredient list and method steps.
* Further below is the comment section which users can view even if not logged in.
* Comment section is available and displayed for logged in users who can submit a comment.
* This is then sent for approval which is a feature only the Admin can access.
* Alert is displayed to indicate the comment has been sent for approval.
* Approved comments can be viewed on the post.

__Sign Up__:

* Accessed from the navigation bar by selecting the 'Sign Up' button. 
* Once selected, the user is taken to the 'Sign Up' page.
* A parallax header image added at the top (after the navigation).
* New users are prompted to enter a username, email (optional), password and password again to confirm.
* All fields apart from the email (optional) are required for the user to be able to create an account, otherwise an error is displayed.
* Upon successful creation the user is then able to login to the account.
* Alert is displayed to indicate that the user has signed in.
* Existing users are provided with the sign in link to take them to the 'Login' page.

__Login__:

* Accessed from the navigation bar by selecting the 'Login' button. 
* Once selected, the user is taken to the 'Login' page.
* A parallax header image added at the top (after the navigation).
* Existing users can enter their username and password and click the login button.
* Upon successful login, user is taken to the 'Home' page.
* Alert is displayed to indicate that the user has signed in.
* Incorrect username and password will faily to log the user into their account and a message will be displayes on the 'Login' page to indicate this.
* New users are provided with the register link to take them to the 'Sign Up' page to create an account.

__Logout__:

* Option only available to users who are currently logged in.
* Accessed from the navigation bar by selecting the 'Logout' button.
* Once selected, user will be taken to the 'Sign Out' page to confirm that they wish to sign out from their account.
* A parallax header image added at the top (after the navigation).
* User can select the sign out button option which will successfully sign out the user from their account and return them to the home page.
* Alert added to indicate that the user has signed out.

__Search__:

* Accessed from the navigation bar in the top right-hand corner. 
* Placeholder text added to indicate to the user that text can be entered in the input box.
* User cannot submit an empty search and user has to enter a max of 2 characters otherwise an error is displayed.
* User is able to click the search button once the requirements are met (as stated above), this will take the user to the 'Search' page.
* A parallax header image added at the top (after the navigation).
* User is able to scroll down and view the displayed results of the recipes which match the keywords entered.
* Prior to the search results, the user is displayed with the keyword searched and below the results are displayed.
* For any successful matches display the recipe card (same as the ones on the 'Home' page), the user can click this and be taken to the recipe page.
* For any unsuccessful matches, the user is displayed with a message to state that no results have been found for this keyword.

__Footer__:

* This feature is present on all the pages/sections and is fixed to the top.
* Social media links can be accessed by the user.
* Hover style applied to signal to the user which link they are selecting and opening. 
* Links open in a new tab so the user is not taken away from the main website and can easily return.

__Features Exclusive to Admin__:

* Only the Admin can approve and delete user comments.
* Only the Admin can create posts.


### Future Features <a name="future-features"></a>

Due to time constraints, I was unable to apply additional features, in the future I would like to implement the following:

* Allow users to edit/delete their own posted comments. Verification would need to be added to ensure that the user is only able to edit/delete their own comments and be restricted from amending any other users' comments.

* Allow users to create their own posts, this would go to Admin for approval to ensure that the content is consistent and appropriate to the website.

* Add a tick list on the blog post section for the recipes. This will allow users to tick off against each of the ingredients to signify which items they have and which they do not. This was added as a User Story for the Poject section in GitHub, however was out of scope for this project at this moment in time as it was not necessary for the website to function.


## Technologies Used <a name="tech-used"></a>

For this project the main languages used are __HTML5__, __CSS3__, __JavaScript__, __Python__, __Django__ and __Heroku Postgres__.

I have also utilised the following frameworks, libraries, and tools:

* [Bootstrap v5.1.3](https://getbootstrap.com/): 
    * Bootstrap has been used for overall responsiveness of the website and for the layout with the addition of select classes.
* [jQuery](https://jquery.com/):
    * jQuery was used for additional function to display the modal sections in this project.
* [GitPod](https://www.gitpod.io/): 
    * I used GitPod as the IDE for this project and Git has been used for Version Control.
* [GitHub](https://www.github.com/): 
    * GitHub has been used to create a repository to host the project and receive updated commits from GitPod.
* [Balsamiq](https://balsamiq.com/): 
    * I used Balsamiq to create the wireframe for the website for the basic structure and layout.
* [Unsplash](https://unsplash.com/): 
    * Unsplash has been used for copyright free images for this project.
* [Freepik](https://www.freepik.com/): 
    * Freepik has been used for copyright free images for this project.
* [Google Fonts](https://getbootstrap.com/): 
    * I have used Google Fonts to import fonts for styling purposes for this project.
* [Font Awesome](https://fontawesome.com/): 
    * Font Awesome was used to apply icons in the Home, Exercises and Footer sections.
* [GIMP v2.10](https://www.gimp.org/): 
    * GIMP image manipulator program was used to edit the favicon used this project.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools): 
    * Chrome Dev Tools was used to test the site, assist with debugging issues and run reports from Lighthouse.
* [W3C Markup Validation Service](https://validator.w3.org/): 
    * The W3C Markup Validation Service was used to validate the HTML document for this project and to identify any issues with the code.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): 
    * The W3C CSS Validation Service was used to validate the CSS document for this project and to identify any issues with the code.
* [JSHint Validation Service](https://jshint.com/): 
    * The JSHint Validation Service was used to validate the JavaScript document for this project and to identify any issues with the code.
* [PEP8 Online Validation Service](http://pep8online.com/): 
    * The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.
* [Color Contrast Accessibility Validator](https://color.a11y.com/):
    * This was used to test the colour contrast accessibility for this project.
* [Heroku](https://www.heroku.com/): 
    * Heroku has been used to create a repository to host the project and receive updated commits from GitPod.
* [Django](https://docs.djangoproject.com/en/3.1/): 
    * Django was used as the main framework to build this project.
* [Cloudinary](https://cloudinary.com/): 
    * Cloudinary was used to store all media and static files for this project.
* [Python](https://www.python.org/): 
    * Various Python modules were used to build this project as detailed below and as seen in the requirements.txt file:
      * asgiref==3.4.1
      * cloudinary==1.28.0
      * dj-database-url==0.5.0
      * dj3-cloudinary-storage==0.0.6
      * Django==3.2.9
      * django-allauth==0.46.0
      * django-crispy-forms==1.13.0
      * django-summernote==0.8.20.0
      * gunicorn==20.1.0
      * oauthlib==3.1.1
      * psycopg2==2.9.2
      * PyJWT==2.3.0
      * python3-openid==3.2.0
      * pytz==2021.3
      * requests-oauthlib==1.3.0
      * sqlparse==0.4.2


## Testing <a name="testing"></a>

### User Stories Testing <a name="user-testing"></a>



### Validation Testing <a name="validation-testing"></a>



### Known Issues and Resolutions <a name="issues"></a>



## Deployment <a name="deployment"></a>



## Credits <a name="credits"></a>

### Content



### Media



### Code



## Acknowledgements <a name="acknowledgements"></a>

* I would like to thank my family and friends for their support throughout this project and for assisting with the testing stage and providing valuable feedback.
* My mentor, Guido Cecilio, for being of great support and providing valuable guidance and feedback throughout this process.
