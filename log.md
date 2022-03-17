# Logging
Here will the process be documented with the creation of the application

## 220220

* Looked into how to design a webapplication. Decided to go with HTML and CSS to create the website. Looked into the basics of HTML and CSS and uploaded test scripts to GitHub. both HTML and CSS seem realtively intuitive. Setup git and cloned repo to my mac. Seem to work fine. 
* Fixed margin in .css for background using:

```css
body {
    margin: 0;
}
```
## 220221
Started to develop the backend with a function that extracts the latitude, longitude and elevation from the gpx file. Next step is to utilize the Ramer-Douglas-Peucker algorithm to deduce the number of points needed to describe the route.

## 220221
Looked into how to calculate the distance. Tried using geopy.distance.distance method. Seems slow and inaccurate? will look into haversine formula to calculate the distances. Since it is an math formula and using numpy I assume it will be faster. Will use the lonlat from `loc()` and haversine to calculate the distance.

## 220224
Updated `README.md` about how to integrate `backend_gpx.py` in the `HTML`. Think the Flask library might be good enough for this since the site only will collect `.gpx`files and use the functions in `backend_gpx.py` to apply the necessary algorithms to the data. Have also been thinking to use a database to store the data that is being put in by the user since the user might add quite many files and a good practice on working with databases and SQL
## 220226
Added ideas into `README.md` about working with databases and also updated `todo.md` on how to design the front end

## 220307
developed the function rdp_gps which uses the Ramer-Douglas-Peucker algorithm to reduce the number of points used, this will most likley need some tweeking in order to get good number of points. But with the setting now and the test file `Walk1.gpx` I reduced the number of points from 1600 to 129. Tried to use listcomprehension to loop all the late and lons into a variable, but did not manange to, will look mer on that in the future. because this step takes som time to do and this is only one relatively small .gpx file.

## 220316
Think I solved the core o this application. I can now take coordinates from two gpx files and reduce their points and make thos two tracks into one. Which is what I wanted, now those updated coordinates must be mapmatched to existing roadsi and plotted onto said roads. Distance calculation has to be done as well.