
This project using Python, Django, Django REST, BS5 etc.
HTML and CSS compiled with BS5.
The backend is written in Django. Working with databases is done using django rest.


1) Written model for storing mortgage offers;
2) Write a ViewSet to implement the CRUD functionality of mortgage offers:
- POST and GET work on http://localhost:8000/api/offer/
- PATCH and DELETE work on http://localhost:8000/api/offer/102/ , where 102 is the id of the entry to change
3) Filtering mortgage offers, according to the entered parameters on main page project (http://localhost:8000/)
4) Implement a functionality that will calculate the payment for all valid mortgage offers.


Custom Script
The client enters the following data:
-The value of the property, in rubles without kopecks. Data type: integer
-Initial payment, in rubles without kopecks. Data type: integer
-Term, in years. Data type: integer

In response, he receives an array with objects of mortgage offers. Each object contains the following data:
-Name of the bank. Data type: string
-Mortgage rate, as a percentage. Data type: float
-Mortgage payment, in rubles without kopecks. Data type: integer
