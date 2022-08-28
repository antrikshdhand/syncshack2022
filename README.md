# SYNCS Hack 2022
## Introduction
Study Buddy is a social and study app catered towards USYD students. You can visit the site yourself at https://usyd-study-buddy.azurewebsites.net/index.html. 

## What we did
We have 3 major aspects in our project. 
- The Front End - HTML, CSS and JS
- The Back End - Python + Flask +
- The Data Store - SQLite3

Our program allows students to register themselves on our site. During this process we collect information about the student and the units that they take. We take this information and create a new user (ideally) stroing it securely in our local server database. Following the registration process student can search for study partners that are current studying the same units they are. All in click of button, students make them selves open to invites. Student can also open themselves to study with students with the same Degree and Faculty if they wish to.

Our flask application handels all the HTTP request redirecting to different pages when needed. While we have fully implemented the SQL storage and querying of data we unfortunately have not been able to implement transfer of data from our SQL API to our main application. 
