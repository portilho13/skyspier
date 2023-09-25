# Sky Spier | Capstone CS50W

</br>

# Overview

Sky Spier is a website whose purpose is to provide aviation enthusiasts with insider information about aircrafts for free. The user just needs to insert a company name or the registration of an aircraft and we provide the information about the aircraft, if available, such as aircraft model, engines, age, registration date, etc. We obtain this info via a complex database and API provided by an external entety named OpenSky Network.

</br>

# Distinctiveness and Complexity:

The Sky Spier database is made up of 520000 lines, each with around 24 different pieces of information where each line corresponds to a different aircraft, Sky Spier is also capable through communications with an API to show all flights, if available, of the aircraft in the past 21 days as well as information about the duration, origin and destination of the flight accompanied by a simple, responsive, fast and effective search engine that provides the user with easy use of the website.

For more intuitive user experience I also implemented the Bootstrap Library and did the UI using native JS and did make my website mobile responsive.

I considered that in this projects I used all the things that I learned from CS50W and due to the amount of data in its database and the use of complex API to catch the flghts information I think Sky Spier is distinct and more complex than other projects provided by CS50W.

</br>

# Structure:

The website is structured as follows:

- **aircraftDatabase.csv**: Contains the 520000 aircrafts with their info that latter I imported on database.

- **opensky_api.py**: API provided by OpenSky API to catch the flights.

- **skyspier**: Home folder of the main Django App.

- **dictionary**: App that is responsible for displaying the flights and the aircrafts information.

</br>

# File Contents

## Front End:

- `./dictionary/`:

    - `./templates/`:

        - `index.html` - Main webpage of website (for now).

        - `aircraft.html` - Dedicated page to show the information about aircraft and its flights through its id in the database.

        - `layout.html` - Basic layout for the all the website.

        - `insert.html` - Temporary link used only to import csv file to database (not acessed by users).

    - `./static/`:

        - `styles.css` - CSS used for all website.

        - `searchbox.js` - JavaScript File responsible for the searchbox.

</br>

## Backend

### Models in the app

There are a total of 1 model in this app:

1. `Aircraft` - Model responsible for all the aircraft information stored in the database, each model has 24 columns.

### aircraftDatabase.csv

CSV file that countains information about 520000 aircrafts.

### opensky_api.py

File that countains the API provided by OpenSky Network.

### requirements.txt

File that countains all the libraries that need to be installed for the project to run without bugs.

### views.py

This file is responsible for all the functions associated with the webiste and its functionability.

### models.py

File responsible for storing each model in the webisite that latter are migrated to the database.

### settings.py

File responsible for handling the settings for the django framework.

### urls.py

File responsible for handling the URLs for our website.

### apps.py

File responsible for handling the different apps in our project.

### tests.py

File responsible for handling the tests to our project (did not implement tests on this project).

### admin.py

File responsible for handling the models that the programmer implemented in it and then will list it in the admin interface.

### wsgi.py

This file mainly concerns with the WSGI server and is used for deploying the web application on to the servers similar to apache, etc. (No changes to this file as well)

### init.py

This file is empty and remains that way. they are present only to tell that this particular directory is a package (no need to change).

</br>

# Installation & How to Setup

Using Django default port `:8000`

**Python**

```json
pip install -r requirements.txt
python manage.py runserver
```

**Python3 (used to build this project)**

```json
pip3 install -r requirements.txt
python3 manage.py runserver
```

# Important Notes:

## Webiste Runtimes:

Due to ammount of data present on the database the search box can have a lag of ~0.5 to 1s on the 1st or 2nd char typed, the website can also take a little more of time when selecting the aircraft due to the ammount of data in the database.

## API Runtimes:

Due to the API used on this project being free and due to ammounts of requests on it, if the time of the website request > 15s the API will reject the connection but theres nothing that I can do about it so maybe the page needs to be reloaded.

## Limitations:

Due to the lack of some info in the csv file of the aircrafts information some fields in the website could have `N/A` in the spot of the info. Due to google maps API beeing paid I could not implement a map with the aircraft route on each flight (something that I plan on doing in the future).

## Future Development

In the future I plan on adding the country of registration of the aircraft and a live google map that displays the route of the flight of an aircraft searched by the user. Such implementations aren't in the project yet due to the fact that a API with more is information and the google maps API key are paid.

## Thanks

Thanks to OpenSky Network for providing an incredible and free Aircraft Database and an API for flights info, could not do it without them, recommend all to pass on their website [OpenSky Network](https://opensky-network.org/) and a big thanks also to all involved in the CS50W course for giving this type of knowledge for free to the world.

### Project made by:

**Mario Portilho**, September 2023.


