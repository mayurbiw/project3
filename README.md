# Project 3

Web Programming with Python and JavaScript

Short description - The user can register to the application by providing their credentials such as username, first name, last name, password, and email. Once the user registers their information is stored into the database and they can come and log in anytime. After login, they will get to see a list of items that they can order. They can add the item into the shopping cart without any need to reload the page just press add corresponding to the item and done, the item is added into the shopping cart. The item in the cards will remain even if the user closes the browser window. They can go into the shopping cart and confirm the orders. The user can reset the shopping cart which will remove all the items from the shopping cart. Once the user places the order it will receive a confirmation mail. The site admin can add and remove new items in the menu, see the placed orders, and mark them completed by using the Django admin. The site manager will be provided with the additional template/view which will show all the orders. From this page (view orders) the admin can mark them completed. As soon as the admin mark the order completed the user will receive the mail saying that their order is completed. 

The models are added into orders/models.py
All the items from the Pinnochio’s menu are entered into the database by using Admin.

There are total 7 html pages

base.html -> the base.html contains the common html for all the other html pages. The common user interface items like navigation bar and page tittle.

register.html -> the user can register for the site using first name, last name, email, username, and password.

login.html -> the login.html contains the field that will be used when the user will login to the application. The fields are username and password and the button to submit.

menu.html -> the menu.html contains the html to display the list of items the user can have.

shoppingcart.html -> the user can view the added items in the shopping cart.

afterorderplaced.html -> the user will redirected to this page once the order is placed. From here the user can go to the menu.

placedorders.html -> the placedorders.html will be accessed through Django admin. The site manager will be able to see all the orders and mark them completed.

Static files -
->  main.js -> the main.js contains all the JavaScript code needed to run the application.
->  styles.css -> the styles.css contains all the CSS needed to style the application.
->  admin.js  -> the admin.js is used for the additional view for Django admin.

Personal touch -
1. The user can reset the shopping cart. The reset will remove all the items from the      shopping cart.
2. The user will receive the confirmation mail once the order is placed.
3. The admin can mark the order completed using additional view in the Django admin.
4. The user can add item into shopping cart without reloading of the webpage.
