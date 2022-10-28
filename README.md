# PyGeoSetter

A Python script that adds GPS information in image files. Additional Python modules, "pyexif" and "GPSPhoto" may be required.

## Usage

1. Edit the config file, "config.json". Currently, config file name and path are fixed (cannot be changed). While there are many items in the config file, only values of "DATESTAMP", "TIMESTAMP", "LATITUDE", "LONGITUDE" and "ALTITUDE" will be added to  image files.

```
{
    "gps": {
		    "DATESTAMP": "2022:10:23",
        "TIMESTAMP": "00:03:30",
        "LATITUDE_REF": "North",
        "LONGITUDE_REF": "East",
		    "LATITUDE": "35.05488",
		    "LONGITUDE": "134.74980",
		    "ALTITUDE": "220",
		    "SATELLITES": " ",
		    "MAP_DATUM": "WGS-48",
		    "STATUS": "Measurement Active",
		    "MEASURE_MODE": ""
    }
}
```

2. Run the Python script with the argument of a single image file (or wildcard).

```
python PyGeoSetter.py sample.jpg
```

```
python PyGetSetter.py dir/*.jpg
```
