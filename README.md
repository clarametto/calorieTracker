# CalorieTracker

#### Latest version updated on:January 14th 2022
#### By :
CLARA METTO,
IAN OCHENGE,
DAVID MATHAGA,
MESHACK KIMUTAI
BRENDA KANALE and
LARVINE ASANDE

## Description
This application  tracks your weight and calculates a recommended daily calorie intake. It also has a well-designed food diary and an exercise log.
day. 
In addition, it shows your remaining recommended intake and the number of calories you’ve burned during the day.Provides a clear picture of how many calories you’ve consumed during the day.

## User Story 
* Sign in with the application to start using.
* Set up a personal profile.
* User can set a goal for calories consumed in a day.
* User can track the amount of calories consumed in a day.
* User can track the type of food consumed in a given day.
* User can add food consumed to check on calories.
* User can search on the food entered earlier.
* User can select on food consumed to get a summary of food consumed in that day.

##  Live Link 
https://calorieapp22.herokuapp.com/

## Technologies Used

- HTML 
- CSS 
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Python3.8](https://www.python.org/)
- [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)
- [Heroku](https://heroku.com)

## Setup and Installation 
##### Clone the repository: 
 ```bash
https://github.com/clarametto/calorieTracker.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd calorie-tracker, pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations calorie
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.

####  Admin- 

#### Password-



## Known Bugs

Incase of any concerns,ideas or queries feel free to contact us through email:
clara.metto@student.moringaschool.com,
ian.ochenge@student.moringaschool.com, 
david.mathaga@student.moringaschool.com,
brenda.kanale@student.moringaschool.com,
meshack.kimutai@student.moringaschool.com.



MIT License

Copyright (c) 2022 Claire Metto, larvine Asande, Ian Ochenge, David Mathaga, Brenda Kanale, Meshack Kimutai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
