# backend_gpx
* in `loc()`, instead of nested loops do a list compremension, since the are faster and the list dont have to be initialized and will therefore take up less meemory.
* develop a function that uses the Ramer-Douglas-Peucker algorithm to reduce the number of points used. Also visualize this in `log.md`for understanding and also to show the workprocess and thought about it.
* compare whats most effective in time and memory:
    * nested functions
    * decorator
    * separately defined functions
* maptrack the points to roads etc.
* come up with a fast and accurate way to calculate distance
* develop the algorithm that only uses the unique track and get rid of repeated tracks.