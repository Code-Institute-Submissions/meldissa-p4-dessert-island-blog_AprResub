# Dessert Island

[View published site on Heroku](https://p4-dessert-island.herokuapp.com/).

![](docs/images/responsive-img-header.png)

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
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used to create the header image for the README file.
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

From the Home page, the user is presented with the navigation which consists of the Dessert Island logo, Home button, About button, Sign Up button, Login button and on the right-hand side is the search bar with the Search button. Each of these buttons are functionable that the user can click or utilise. The following actions will occure once the user clicks the following buttons:

* Dessert Island Logo -> Defaults to the Home page, user can click this to take them back to the Home page
* Home button -> Links to the Home page, user can click this to take them back to the Home page
* About button -> Links to the About page, user can click this to take them to the About page 
* Sign Up button -> Links to the Sign Up page, user can click this to take them to the Sign Up page
* Login button -> Links to the Login page, user can click this to take them to the Login page
* Search button -> Links to the Search page, user can only click this once the search criteria has been met (cannot be blank and a minimum of 2 characters), this will then allow for the form to be submitted

The user can easily access the navigation as this is fixed at the top of the page and is accesable from all the pages of the website. On desktop view the navigation can be viewed in full but in mobile view this then collapses and is accsessed from the burger menu.

![](docs/images/usertest-nav.png)

Further down from the navigation, the user is presented with a greeting introductory message for the Dessert Island website. This gives the user an idea that this is a recipe blog even without checking the About page for full details.

![](docs/images/usertest-intro.png)

The main section of the Home page displays the posted recipes, there is a max of 6 recipes displayed per page. The user can navigate between the recipe pages by clicking Next button to go to the next page to view more recipes or clicking Prev button to go to the previous page. The recipes are displayed in date order, the most recent posts are displayed first and the older posts will be displayed at the very end (or on a different page if exceeding 6 posts per page). Each recipe is presented with a card style with an imagine, the author, recipe title, recipe description, posted date and time, and a like count. The user can select any recipe from the available posts by clicking the recipe title or description. This action will take the user to the recipe post page of that particular recipe.

![](docs/images/usertest-home1.png)

![](docs/images/usertest-home2.png)

At the bottom of the page is the footer. The footer is present and can be accessed from any page of the website. The footer provides social media links to the user which they are able to click to take them to the respective social media platforms. The social media links open in a new tab once clicked, this provides for a better user experience as the original website is not lost and the user is able to easily navigate back from where they left off. Further down from there is the copyright text for the website.

![](docs/images/usertest-footer.png)

The following user stories have been achieved from this section:

* As a Site User I can click on a post so that I can read the full text
* As a Site User I can view a list of posts so that I can select one to read
* As a Site User I can locate their social media accounts so I can receive updates and see their following and how well they are known and reliable
* As a Site User I can navigate easily through the site and find the relevant information with ease

Selecting the About button from the navigation will take the user to the About page. The top of the page has a parallax style banner image and further down is the About Us section with text the user is able to read. From here the user is able to find out more information about the website and the aim of Dessert Island. Any new users viewing this section are also provided with a link encouraging them to sign up and create and account to join the community. The sign up link from this section will take the user to the Sign Up page.

![](docs/images/usertest-about1.png)

![](docs/images/usertest-about2.png)

The following user stories have been achieved from this section:

* As a Site User I can learn more about the site the purpose of the web app

Selecting the Sign Up button from the navigation will take the user to the Sign Up page. This page can also be accessed by clicking the links available on the About page and/or Login page. The top of the page is displayed with a parallax style banner image and further down is the Sign Up section, any existing users with an account are prompted to go to the login page provided from the link. Any new users are prompted to enter the required details to be able to sign up. The fiels username, password and password (again) are required fields, therefore the user cannot submit a blank form for these. However the E-mail is an optional field as stated on the form, therefore the user does not need to enter this to sign up to become a member.

![](docs/images/usertest-signup1.png)

![](docs/images/usertest-signup2.png)

If the password section does not match for both fields, then the user will be presented with a message to state that they must type the same password each time to be able to create the account.

![](docs/images/usertest-error1.png)

If the password is too similar to the username the user will also be displayed with an error message. This is a security feature on the form to ensure the user's account cannot be acessed easily by creating a different and strong password.

![](docs/images/usertest-error2.png)

Once the sign up form fields have been successfully filled out and the user clicks the sign up button, then the user will be taken back to the Hope page and an alert message will be displayed at the top (below the navigation) to indicate that the user is signed is as their 'username' name. The navigation will now be updated to remove Sign Up and Login buttons with the Logout button.

![](docs/images/usertest-nav2.png)

Alternatively for any existing users with an account already created, by selecting the Login button from the button, this will take the user to the Login page. The link is also accessed from the sign up page for existing users. The top of the page is displayed with a parallax style banner image and further down is the Login section, any new users are prompted to go to the sign up page provided from the link. Any existing users are prompted to enter the required details to be able to login. The user is required to enter their username and password which they previously used to create the account. The user also has an option to tick the 'Remeber Me' checkbox. 

![](docs/images/usertest-login.png)

![](docs/images/usertest-login2.png)

Once the user has entered the relevant details and clicked the login button to submit the form, they will be taken back to the Home page and an alert will be displayed at the top of the page (below the navigation) to notify the user that they have logged in successfully. The navigation bar will be changed once logged in as described above in a previous point.

Logged in users have the option to Logout from their account by selecting the Logout button from the navigation. By selecting the Logout button this will take the user to the Logout page. The top of the page is displayed with a parallax style banner image and further down is the Sign Out section, the message prompts the user to confirm if they wish to sign out. Selecting the sign out button will confirm this choice and the user will be taken back to the Home page, and an alter will be displayed to confirm that the user has signed out. Users who do not wish to logout can click back to the Home page from the navigation (or any other page) to undo this action.

![](docs/images/usertest-signout.png)

![](docs/images/usertest-signout2.png)

Users with an account that are logged in have the option to add comments and like posts on the post detail page once a recipe is selected.

The main section of the recipe post is exactly the same for logged in users as is for users who are not logged in. The recipe title, author, time and date and image are displayed at the top. Then further down is the main post body with the ingridient list and method. At the end of the method section, there is a like counter and comment counter displayed which will show how many users have liked the post and how many comments does a post have.

![](docs/images/usertest-post.png)

With likes and comments:

![](docs/images/usertest-likes.png)

With no likes and comments:

![](docs/images/usertest-likes2.png)

After the main recipe post, logged in users will be displayed with the comments section (on the left) where any posted comments which have been approved by the admin can be viewed, and the comment box (on the right) where the user can submit a comment. The comment box is only available for logged in users, whereas the comments section is visible to both logged in users and users not logged in.

Logged in user view:

![](docs/images/usertest-post2.png)

Generic view for non-members:

![](docs/images/usertest-post3.png)

The comment box provides details to the user as to who they are posting as which corresponds to the username they have logged in with. Further down is the main comment body section where the user is able to enter a comment. Once clicking the submit button, the user will be presented with an altert message to state that the comment has been sent for approval. Only the admin can approve comments. Once the admin has approved the comment, this can now be viewed on the recipe post.

![](docs/images/usertest-comment.png)

![](docs/images/usertest-comment2.png)

The logged in user is also able to like a post by clicking the heart icon, this will increase the like acount by 1. Alternatively, the user can also unlike the post by clicking on the heart icon again which will decrease the count by 1.

The following user stories have been achieved from this section:

* As a Site User I can register an account so that I can comment and like
* As a Site User I can like or unlike a post so that I can interact with the content
* As a Site User I can leave comments on a post so that I can be involved in the conversation
* As a Site User/Admin I can view comments on an individual post so that I can read the conversation
* As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral

Users are also able to utilise the search functionality on the website. This feature is accsessed from the navigation bar located on the right-hand side. 

![](docs/images/usertest-search.png)

The user is able to enter a keyword corresponding to the desired recipe they would like to locate in the input box. Once this has been filled out, the user can click the submit button which will take them to the Search page. Users cannot submit a blank form as this field is required, in addition there is a requirement of minimun of 2 characters to be added before the form can be submitted.

![](docs/images/usertest-search2.png)

On the Search page, there is a parallax type header image at the top, and further down is the search result section.

![](docs/images/usertest-search3.png)

For the search results sections, the user is presented with the keyword searched and below that any successful returns of the keyword will display the recipes which match this. The recipe results are displayed in the same manner as the blog posts on the Home page. The user is able to click on the recipe post which will take them to the post detail page for that recipe. 

![](docs/images/usertest-search4.png)

Any unsuccessful matches to the user's search will be displayed with a message to say so.

![](docs/images/usertest-search5.png)

The following user stories have been achieved from this section:

* As a Site User I can search keywords for specific recipes

__Admin Only User Story Testing__

This section tests the user stories for the Admin only functions of the website.

The admin section is accessed by entering 'admin/' at the end of the url for the website. This displayed the login page for the admin from which they can login.

![](docs/images/usertest-admin.png)

The site admin has various actions available to be able to manage the website such as:

* Delete users
* Create/edit/delete posts and drafts
* Approve and delete comments

From the home section of the admin page, by selecting the Users link under 'Authentication and Authorization' the admin can view the lists of users currently signed up to the website. The admin also has the permission to delete the users by selecting the username and from the drop down selecting the delete user option.

From the home section, the admin can also view comments added by users some of which are pending approval. This is accessed from the Comments link under the 'Blog' section. Approved comments are indicated with a green tick under the Approved column. Comments pending approval have the red cross icon. To approve the comment the admin has to tick the unapproved comment from the list, then from the action drop down select the 'Approve comments' option. By clicking Go button this will proceed to carry out the action to approve the selected comment. Once the comment has been approved the red cross icon will now become a green tick icon to indicate that the comment has now been approved. The approved comment can also be viewed on the website now.

![](docs/images/usertest-admin2.png)

![](docs/images/usertest-admin3.png)

Alternatively selecting the 'Delete selected comments' action will proceed to delete the comment selected. Users will also no longer be able to view the comment on the website.

From the home section, the admin can also view the posts on the website, create new posts and edit/delete any existing ones. This can be accessed from the Posts link under the 'Blog' section. By selecting this link, this will display all the current posts submitted on the website.

![](docs/images/usertest-admin4.png)

The admin can delete any of these posts by selecting the 'Delete selected posts' action from the Action drop down.

The admin can also click on an existing posts by selecting the post tile to view the editor. From this section the admin can edit the posts content, and also has the option to delete the post or to save the changes.

![](docs/images/usertest-admin5.png)

The admin can also create new posts by selecting the Add Post + button. This will open up the editor page which will allow the fields to be populated. The status of the post can also be toggled between Draft or Published. The Published posts can then be viewed on the website, whereas Draft posts cannot.

These particular admin only permissions cannot be accessed by any other users, and users cannot edit or delete comments or posts or access another users account.

The following user stories have been achieved from this section:

* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
* As a Site Admin I can create draft posts so that I can finish writing the content later
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
* As a Site Admin I can prevent unauthorised users from having access so that they cannot access admin content or other users' profiles


### Validation Testing <a name="validation-testing"></a>

To test the HTML code, I used the __W3C Markup Validation Service__.

* Home Page (index.html):

![](docs/images/valtest-home.png)

* About Page (about.html):

![](docs/images/valtest-about.png)

* Sign Up (signup.html):

![](docs/images/valtest-signup.png)

* Login Page (login.html):

![](docs/images/valtest-login.png)

* Logout Page (logout.html):

![](docs/images/valtest-logout.png)

* Search Page (search.html):

![](docs/images/valtest-search.png)

* Post Detail (Recipe) Page (post_detail.html):

![](docs/images/valtest-post.png)

![](docs/images/valtest-post2.png)

An error was located when testing the post_detail.html indicating that there was a closing p tag without an opening p tag. However, upon further inspection the opening p tag is present as displayed in the above screenshot (row 115 opening p tag and row 117 closing p tag). For some reason the HTML validator seems to throw out this error, this could potentially be due to content loading in between the p tags for the post detail. The opening and closing p tag is also present on the post_detail.html rows 28 and 30. Therefore, this does not seem to be a valid error.

Please note that the base.html has been validated as part of the above pages as the code was inclusive of the testing.

To test the CSS code, I used the __W3C CSS Validation Service__.

* style.css:

![](docs/images/valtest-css.png)

No errors were detected in the code.

To test the JavaScript code, I used the __JSHint Validation Service__.

* script.js:

![](docs/images/valtest-js.png)

No errors were detected in the code. Warnings were detected in the code however this was due to the use of the new ES6 syntax in the code.

To test the Python code, I used the __PEP8 Online Validation Service__.

All files passed through the validator and no issues were detected with the exception of the settings.py (rows 112, 115, 118, 121 and 144) and 0001_initial.py (rows 21, 26, 29, 30, 31, 40 and 46) files. This was due to the rows in question being too long, however as these are auto generated by Django or the link name being too long in the case of row 144 on the settings.py file for the cloudinary url, these rows were not amended and left as they are.


### Known Issues and Resolutions <a name="issues"></a>



## Deployment <a name="deployment"></a>

The project was developed using GitPod and was deployed via the GitHub repository to Heroku.

The following steps were followed to deploy this project:

1. From the Heroku dashboard, select 'New' in the top right-hand corner.
2. Click 'Create new app'.
3. Enter the app name and choose region as Europe. 
4. Click 'Create app'.
5. Select the 'Settings' tab, and scroll down to 'Buildpacks'. 
6. Add 'Python' and save changes.
7. Scroll down to 'Config Vars' section, and add the 'KEY' and 'VALUE' for the CLOUDINARY_URL, DATABASE_URL and SECRET_KEY to run the app.
8. At the top of the page, click on the 'Deploy' section.
9. Select Github as deployment method.
10. Select 'Connect to Github', and locate the repository name and click on 'Connect' to link my Heroku app to my Github repository code.
11. To add the Postgres Database, click on the 'Resources' tab.
12. Under Add-ons, search for 'Heroku Postgres', click on the search result for this.
13. Select the 'Hobby Dev-Free' option and click submit order form which will add this to the Add-ons section.
14. Scroll further down, select 'Enable Automatic Deploys' and then select 'Deploy Branch' to deploy project.
15. After it has successfully deployed a 'view' button appears on screen and when clicked opens the deployed application.


## Credits <a name="credits"></a>

### Content

All recipes were obtained from [BBC Good Food](https://www.bbcgoodfood.com/), details below for each individual recipe used:

* Dark Chocolate & Cherry Bar - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/dark-chocolate-cherry-bar)
* Toffee Apply Bread & Butter Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/toffee-apple-bread-butter-pudding)
* Quick & Easy Tiramisu - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/quick-easy-tiramisu)
* Apply Crumble Sundae - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/apple-crumble-sundae)
* Rhubard & Custard Meringue Tart - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/rhubarb-custard-meringue-tart)
* Lemon Drizzle Sponge Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/lemon-drizzle-sponge-pudding)
* Rice Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/a-nice-rice-pudding)
* Victoria Sponge Loaf Cake - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/victoria-sponge-loaf-cake)
* White Chocolate Cheesecake - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/white-chocolate-cheesecake)
* Perfect Pavlova - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/perfect-pavlova)


### Media

The images used for this project we obtained from the following sources:

Favicon:

* Cupcake Icon - from [Freepik](https://www.freepik.com/free-vector/vector-cupcake-with-pink-whipped-cream-cherry-close-up-isolated-white-background_11060360.htm#page=1&query=cupcake%20icon&position=0&from_view=search)

Header/Parallax Images:

* About Us - from [Unsplash](https://unsplash.com/photos/6k1PJQpzFQo)
* Sing Up - from [Unsplash](https://unsplash.com/photos/yCKZFRcX5W4)
* Login - from [Unsplash](https://unsplash.com/photos/yCKZFRcX5W4)
* Logout - from [Unsplash](https://unsplash.com/photos/6k1PJQpzFQo)
* Search Results - from [Unsplash](https://unsplash.com/photos/HG1pJiQHXzs)

Recipe Images:

* Default - from [Freepik](https://www.freepik.com/free-photo/cooking-kitchen_877588.htm#page=1&query=baking&position=11&from_view=search)
* Dark Chocolate & Cherry Bar - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/dark-chocolate-cherry-bar)
* Toffee Apply Bread & Butter Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/toffee-apple-bread-butter-pudding)
* Quick & Easy Tiramisu - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/quick-easy-tiramisu)
* Apply Crumble Sundae - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/apple-crumble-sundae)
* Rhubard & Custard Meringue Tart - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/rhubarb-custard-meringue-tart)
* Lemon Drizzle Sponge Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/lemon-drizzle-sponge-pudding)
* Rice Pudding - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/a-nice-rice-pudding)
* Victoria Sponge Loaf Cake - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/victoria-sponge-loaf-cake)
* White Chocolate Cheesecake - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/white-chocolate-cheesecake)
* Perfect Pavlova - from [BBC Good Food](https://www.bbcgoodfood.com/recipes/perfect-pavlova)


### Code

* To build the search functionality for the website, code from the following [YouTube](https://www.youtube.com/watch?v=AGtae4L5BbI) video tutorial was used to assist with this.

* A large part of this project code was used and inspired from the Code Institute's I Think Therefore I Blog walkthrough to be able to build a base skeleton project. Please note some of the borrowed code has been customised by me to fit this project. I have also added my own code for additional functions for the project.

## Acknowledgements <a name="acknowledgements"></a>

* I would like to thank my family and friends for their support throughout this project and for assisting with the testing stage and providing valuable feedback.
* My mentor, Guido Cecilio, for being of great support and providing valuable guidance and feedback throughout this process.
