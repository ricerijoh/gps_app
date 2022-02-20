# Description of GPS app (name is not decides)

This gps app aims to combine serveral different gpx files and combining all the
waypoints that is created into a single track. From this will the total
kilometers traveled be calculated together with height gain. But the special
thing about this is that only unique segments will be counted towrads to total
kilometers traveled and height gained.

## How it will be done (continious and changable)

The general layout and how the task will performed
* Build core algorithm in Python using different a variety of libraries to accomplish the task
* Build backend code using Django
* Build frontend code using React (**not decided which language**)
### Python code base for the core algorithm

* Parse .gpx files
* Use Ramer-Douglas-Peucker algorithm to deduce the number of **waypoints** for
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
