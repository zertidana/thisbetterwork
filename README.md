# Online Newspaper Web Application :desktop_computer:

## Introduction :technologist:
This project, undertaken by our team of four students, aims to create an online newspaper web application similar to prominent news portals like BBC News, The Times, or The Guardian. Our application is built using the Django framework and incorporates advanced web technologies for a seamless user experience.

## Features :electron:
- **User Authentication :mag:**: Custom User model based on Django's AbstractUser. Includes functionalities for account creation, login, and logout using Django's authentication framework.
- **Profile Management :bust_in_silhouette:** : Users can update their profile image, email, and date of birth on a dedicated profile page. Profile updates are handled via Ajax using Vue and the fetch API.
- **News Browsing :earth_africa:**: The app allows users to browse news articles categorized into various sections like Sport, World, Finance, etc.
- **Personalized News Feed :star2:**: Users can select their favorite news categories in their profile, and the app will tailor the news feed to show articles from these categories.
- **Interactive Comments :busts_in_silhouette:**: Users can post, reply, edit, and delete comments on articles. Comment management is also facilitated through Ajax.
- **Technologies Used :globe_with_meridians:**: The Vue frontend utilises TypeScript with static typing, including custom interfaces for news articles and categories. The Python backend is enhanced with type annotations for static type checking.

## Deployment and Testing :atom:
- **Platform**: The application will be deployed on the EECS OpenShift platform.
- **Testing Accounts**: Includes 5 test users and 10 news articles across at least three categories.
- **Admin Access**: Login credentials for the admind page will be provided.

## Access and Submission
- **Application URL**: https://group15-web-apps-ec21715.apps.a.comp-teach.qmul.ac.uk/
- **Test User Credentials**: List of usernames and passwords for the test users.
- **Admin Credentials**: Username: admin password:123456789

## Technical Requirements :memo:
- **Django Version**: Django 4.2
- **Python Version**: Python 3

## Credits :test_tube:
* Dana Zerti : Full-stack Developer
    - Modelling of application data, including users, news articles, categories, and comments
    - Using frontend routing (Vue router) and a global store (pinia)
    - Profile page included, with profile picture, email, date of birth and list of favourite news categories (all editable via Ajax)
    - Users are able to post comments on news articles, and reply to previous comments via Ajax
    - Completed README.md

* Visard Neza : Full-stack Developer 
    - Account creation and login 
    - Using Django's AbstractUser model with required fields and Django's authentication framework
    - Using frontend routing (Vue router) and a global store (pinia)
    - Modelling of application data, including users, news articles, categories, and comments
    - Used  static types both in Python (type annotations) and Vue (typescript)
    - Deployed app to Openshift

* Reesha Lad : Frontend Developer
    - Profile page included, with profile picture, email, date of birth and list of favourite news categories
    - Page with a list of news article included, with articles grouped by category



* Aqib Kabir : Frontend Developer
    - Profile page included, with profile picture, email, date of birth and list of favourite news categories
    - Page with a list of news article included, with articles grouped by category
    - Users are able to comment on news articles
    - Created the articles
