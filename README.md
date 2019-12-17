# [Cookie Django Milestone Project](linkgoeshere)

The purpose for this project is mainly to showcase different types of cookies, for visitors that could possible be customers.
Visitors will get information through the available content, encouraging them to sign up to be able to access more content.
Registered users can access the entire collection of cookies and if intrested they may procceed to purchase by adding products to the shopping cart.

[![Build Status](https://travis-ci.org/Ario124/Cookie-Django-Milestone-Project.svg?branch=master)](https://travis-ci.org/Ario124/Cookie-Django-Milestone-Project)

---
## UX

Visitors who are not logged in are welcomed to the site and encouraged to register, allowing them to access more
content on the site, such as the products available.

The visitors can access the **Login** and the **About** Page through the navigation bar at the top, this will let users
Login if they already have an account. 

The about page will give you information that you might be looking for, and once again encouraging registration.

They can also access **Sign Up** that is displayed at the center of the main page, this will redirect to the **Register** page.



#### Wireframes/Mockups

#### Mobile

* [Index-Mobile](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/index-mobile.png)
* [About-Mobile](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/about-mobile.png)
* [Cart-Mobile](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/cart_mobile.png)
* [Cookies-Mobile](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/cookies-mobile.png)
* [Checkout-Mobile](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/checkout_mobile.png)
---
#### Desktop

* [Index-Desktop](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/index-desktop.png)
* [About-Desktop](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/about-desktop.png)
* [Cart-Desktop](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/cart_desktop.png)
* [Cookies-Desktop](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/cookies-desktop.png)
* [Checkout-Desktop](https://github.com/Ario124/Cookie-Django-Milestone-Project/blob/master/wireframes/checkout_desktop.png)

#### User Stories

* As a visitor I can navigate through the main page and the navigation bar with access to the Login, About, and Registration page.
* As a visitor I am informed through **About** on the sites content and information on our cookies and offers, as well as contact email and phone.
* As a visitor I can load 'About' and click on 'Donate' to make a donation.
* As a visitor I can access the Github Icon Link at the bottom of the site to get to the github page.

1. As a user I can access 'Cookies' allowing me to browse through the products available.
2. As a user I can access cookies being displayed, click on 'Read More' to get more information about a specific product.
3. As a user I can click on 'Add to cart' to add items to the shopping cart.
4. As a user I can load and view the cart by simply clicking on the cart icon by the navigation bar.
5. As a user I can view the cart with selected items, where I can change the quantity of any item to the desired quantity and click 'Update' to apply changes,
   If quantity is set to 0 the item will be erased from the cart.
6. As a user I can proceed to the 'Checkout' page once the cart is loaded with items.
7. As a user I can access the 'Checkout' page to view a summary of the products that have been added to the cart, I can click on 'Adjust Order' if changes need to be done.
8. As a user I can load the 'Checkout' page to procceed and make a payment, I can fill out the forms and click on 'Submit Payment'

## Features

#### Website features for visitors
The website features for visitors are as follows:

* Visitors are able to navigate through the nav bar and access the About page.
* Visitors are able to register by clicking on the 'Buy Cookies' button that is located at the center of the page.
* Visitors can access the About page and procceed to click on 'Donate' to donate a small sum.
* Visitors may click on 'login' through the navigation bar to login if they already have an account.


#### Website features for registered users
The website features for registered users are as follows:

* Users can access the 'Cookies' page to get a look on whats available for purchase.
* Users can access the Shopping Cart Icon, located by the navigation bar. Allowing users to preview all items they have.
* Once the user has loaded the Shopping Cart they may procceed to make changes on quantity for each item.
* Users can access the 'Checkout' page where the payment form is.
* Users can submit a payment through the 'Checkout' page, by simply filling out the forms.

#### Features that can be implemented

* After customers buy items, they are redirected to "ordersent.html" where items bought should be displayed.
* Add "+" & "-" signs by the quantity, allowing users to click plus or minus, to change item quantity instead if typing in a number.

## Technologies used
These are the technologies used in this web application:

* [HTML](https://www.w3schools.com/html/) The use of HTML for this project was to build the structure and add content, putting everything in place.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) I have used CSS to style the website with nicely matched colors and a better user experience through keyframes and hover properties.
* [JavaScript](https://www.javascript.com/) My use of Javascript was mainly to activate Stripe. Also used minor jquery fade function.
* [Bootstrap](https://getbootstrap.com/) I have used Bootstrap to apply styling through the structure, using navbar, grids and containers.
* [Django](https://www.djangoproject.com/) This project is made with the use of Django.
* [Python](https://www.python.org/) The logic used in the backend for this project was done through the use of Python.
* [PostgreSQL](https://www.heroku.com/postgres) Database through Heroku PostgreSQL.
* [Stripe](https://stripe.com/) The payment system uses Stripe, through Javascript.
* [Github](https://github.com/) I have used Github to host my project by commits and push.
* [Heroku](https://heroku.com/) Heroku is also used for Hosting live version of the website.
* [Balsamiq](https://balsamiq.com/) Balsamiq used mainly to create the wireframes used for this project.


## Testing
I have tested the website to ensure that it is running smoothly and without major bugs/errors.

These manual tests have been carried out mainly for the following devices:

* Samsung Galaxy S10
* Desktop

#### Testing website
#### Manual Tests
User Stories:

1. Load the home page using Google Chrome, procceed to open Dev Tools and check to confirm that there are no errors showing up.
2. Load the web application on Chrome and open Dev Tools, try resolutions for Galaxy S10 and Desktop, these should be responsive. 
3. Load the home page and verify that the navigation bar follows when scrolling.
4. Verify that the Favicon is visible and shown on the tab once the homepage has been loaded.
5. Load the main page and verify that the navigation bar is responsive, it should expand on click if viewed from a mobile device.
6. Verify that the links on the navigation bar are working, redirecting to the specific pages.
7. Load the registration page and fill the form to create an account, verify that a message is shown, letting you know that the account has been created.
8. Load the login page and login with your details, verify that a message is shown letting you know if you've successfully logged in.
9. Verify that a message is shown once you've logged out, this message should let the user know this.
10. Load the cookies.html page and verify that the Cookies are on place properly shown and well displayed.
11. Verify that a cookie is added to the cart when clicking on 'Add to cart' it should result in the cart changing color from white to orange, also showing the amount.
12. Load the cart.html page and change the amount to any number, click on update to actualize the changes.
13. Load the cart.html page and proceed to click on 'Checkout' verify that it redirects to the checkoutpage with a summary of whats about to be ordered.
14. Load the checkout.html page and fill out the forms then verify the payment form works when clicking on 'Submit Payment'

#### Automated Tests

* Basic testing can be found on the cookie/tests.py

#### Validation

These tests were made to control and verify the code is clean and workig properly.

* **HTML** - Used [HTML Validator](https://validator.w3.org/) to validate the html, since the validator does not know about Jinja it gives warnings on "Bad Value" but is good otherwise.
* **CSS** - Used [CSS Validator](https://jigsaw.w3.org/css-validator/) to validate the css, and no errors were found here. 

#### Browsers

* [Google Chrome](https://www.google.com/intl/en/chrome/)
* [Mozilla Firefox](https://www.mozilla.org/)
* [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge)
* [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer)

## Deployment



## Media

## Credits

### Disclaimer