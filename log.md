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
Looked into how to calculate the distance. Tried using geopy.distance.distance method. Seems slow and inaccurate? will look into haversine formula to calculate the distances. Since it is an math formula and using numpy I assume it will be faster. Will use the lonlat from `get_lat_long_ele()` and haversine to calculate the distance.