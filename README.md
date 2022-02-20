# Description of GPS app (name is not decides)
This gps app aims to combine serveral different gpx files and combining all the
waypoints that is created into a single track. From this will the total
kilometers traveled be calculated together with height gain. But the special
thing about this is that only unique segments will be counted towrads to total
kilometers traveled and height gained.

## How it will be done (continious and changable)
The general layout and how the task will performed
### Python code base
* Parse .gpx files
* **mapmatch** tracks to roads with [link]https://leuvenmapmatching.readthedocs.io
    * Here I think its better to mapmatch every each .gpx individually and based 
    on the updated track it should be easier to distigush unique tracks
