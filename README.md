# Little-Lemon-Booking-system
This repository contains the completed final assessment for the Meta Back-End Developer Capstone Project on Coursera. The project demonstrates a full-stack implementation of a booking form feature for the fictional restaurant Little Lemon.


1.Features Implemented
 Backend (Django):

-Set up restaurant app and added it to INSTALLED_APPS

-Configured SQLite database in settings.py

-Performed migrations to initialize models

-Created a Booking model with fields: first_name, reservation_date, and reservation_slot

-Implemented validation to prevent duplicate bookings for the same date and time

-API endpoint returns JSON data of all bookings

-API supports date filtering (returns bookings for a specific date)

-If no bookings exist for a selected date, "No Booking" message is displayed

2.Frontend (HTML + JavaScript):

-Implemented a user-friendly booking form with:

-First name input

-Date selector using an input of type date

-Reservation slot dropdown

-Used the Fetch API to:

-Retrieve booking data from the API

-Automatically display booking data for the selected date

-Prevent user from booking an already taken time slot

-Automatically pre-selects today’s date when form is opened

-Dynamic UI updates when the date is changed

🔧 Technologies Used
Python 3.9

Django

Django REST Framework

HTML5 / JavaScript (Vanilla)

📁 Folder Structure
This repo includes 3 project folders (Lab 1, Lab 2, and Lab 3), each demonstrating incremental progress toward the full-stack implementation.
