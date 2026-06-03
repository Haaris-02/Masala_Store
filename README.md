# Masala Store - Open QA Challenge 🚀

Welcome to the Masala Store! This is a sample E-commerce website built using Django and Bootstrap 5. 

On the outside, it looks like a simple website selling spices. But on the inside, I have intentionally added several bugs. This project is created for QA Engineers and Software Testers to practice their manual testing skills.

## Technology Used
* Backend: Python, Django
* Frontend: HTML, CSS, Bootstrap 5
* Database: SQLite

## How to Run the Project 🛠️

To run this project on your local computer, follow these simple steps:

1. Clone this repository to your computer.
2. Open your terminal or command prompt.
3. Install Django if you don't have it:
   `pip install django`
4. Go to the project folder and run the database setup:
   `python manage.py migrate`
5. Start the local server:
   `python manage.py runserver`
6. Open your web browser and go to `http://127.0.0.1:8000`

## The Challenge 🐞

Your task is to test this website and find the hidden bugs. There are a total of 6 intentional bugs. Some are frontend design issues, and some are critical backend logic errors.

**Testing Areas to Focus On:**
* Adding products to the cart (Try different numbers).
* Checking the cart count in the top menu.
* The total amount calculation on the checkout page.
* The Contact Us form submission.
* Clicking buttons on the products page.

**How to Report:**
If you find a bug, please go to the "Issues" tab in this GitHub repository and create a new issue. Write down the steps to reproduce the bug and what the expected result should be.

Good luck and happy bug hunting!