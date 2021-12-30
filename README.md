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


### Future Features <a name="future-features"></a>



## Technologies Used <a name="tech-used"></a>

For this project the main languages used are __HTML5__, __CSS3__ and __JavaScript__.

I have also utilised the following frameworks, libraries, and tools:

* [Bootstrap v5.0.2](https://getbootstrap.com/): 
    * Bootstrap has been used for overall responsiveness of the website and for the layout with the addition of select classes.
* [jQuery](https://jquery.com/):
    * jQuery was used for additional function to display the modal sections in this project.
* [GitPod](https://www.gitpod.io/): 
    * I used GitPod as the IDE for this project and Git has been used for Version Control.
* [GitHub](https://www.github.com/): 
    * GitHub has been used to create a repository to host the project and receive updated commits from GitPod.
* [Balsamiq](https://balsamiq.com/): 
    * I used Balsamiq to create the wireframe for the website for the basic structure and layout.
* [Flaticon](https://www.flaticon.com/): 
    * I used Flaticon website to obtain the favicon image used for this project.
* [Freepik](https://www.freepik.com/): 
    * Freepik has been used for copyright free images for this project.
* [Google Fonts](https://getbootstrap.com/): 
    * I have used Google Fonts to import fonts for styling purposes for this project.
* [GIMP v2.10](https://www.gimp.org/): 
    * GIMP image manipulator program was used to change contrast for the background image used this project.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools): 
    * Chrome Dev Tools was used to test the site, assist with debugging issues and run reports from Lighthouse.
* [W3C Markup Validation Service](https://validator.w3.org/): 
    * The W3C Markup Validation Service was used to validate the HTML document for this project and to identify any issues with the code.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): 
    * The W3C CSS Validation Service was used to validate the CSS document for this project and to identify any issues with the code.
* [JSHint Validation Service](https://jshint.com/): 
    * The JSHint Validation Service was used to validate the JavaScript document for this project and to identify any issues with the code.
* [Color Contrast Accessibility Validator](https://color.a11y.com/):
    * This was used to test the colour contrast accessibility for this project.
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used to create the header image for the README file.

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
