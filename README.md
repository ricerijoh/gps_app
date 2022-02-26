# Description of GPS app (name is not decided)

This gps app aims to combine serveral different gpx files and combining all the
waypoints that is created into a single track. From this will the total
kilometers traveled be calculated together with height gain. But the special
thing about this is that only unique segments will be counted towrads to total
kilometers traveled and height gained.

## How it will be done (continious and changable)

The general layout and how the task will performed
* Build core algorithm in Python using different a variety of libraries to accomplish the task
* Build backend front end integration using Flask or Django
    * Here I could go by using an Python script with all the functions needed to parse, and manipulate data to our liking. Then have for example a Python Flask script than integrates with the HTML. Maybe set up some kind of database to store the input data from the user? 
        * CREATE FLOWCHART FOR THIS
* Build frontend code using HTML and CSS

## Python code base for the core algorithm

* Parse .gpx files
* Use Ramer-Douglas-Peucker algorithm to deduce the number of **points** for
each .gpx file
    * This is done to make the code more effictive since we will work with 
    smaller datasets 
* **mapmatch** tracks to roads with https://leuvenmapmatching.readthedocs.io
    * Here I think its better to mapmatch every each .gpx individually and based 
    on the updated track it should be easier to distigush unique tracks
* Combine all maptracked tracks and distingush the unique tracks
    * This will be the core alogorithm and the whole idea for this application
* Use some kind of filter for height gain since it ususally can give inaccurate
height gains
    * Here I have to test different filters, a Kalman filter would be optimal to
    use to smooth the data. But this can take a lot of processing power.
    but to convolve the data with an mean kernel can be a good approximation.
    will compare different types of filters to see which gives the best result
    with least amount of processing.
## Python Flask script for routing and call functions from Python code base
The API of choice will be `Flask` as it seems to be easy straightforward and seem to have all he necessary functionality that I need to store files on, for example a server. 
## HTML script