# Observing and Describing a Volcanic Eruption
## Names: 
- Jude Lowe, Lucas Holt, Jack Logan
## Background
- Geophysical methods are used to observe what is going on under the surface and can be used to see what volcanic processes occur.
- The heat (infrared electromagnetic radiation), gas, and seismic waves volcanoes release could be an indicator of volcanic activity.
- Displacement measurements can indicate deformation caused by volcanism.
- Our target is Sabancaya, an active stratovolcano in Peru. It has been actively erupting since 2016.
## Problem Statement
- What trends can we observe in geophysical data before, during, and after a volcanic eruption period?
## Data Sets
- [Mirova DB for heat](https://www.mirovaweb.it/)
- [Smithsonaion DB for eruptions](https://volcano.si.edu/database/search_eruption_results.cfm)
- [Deformation DB](https://comet.nerc.ac.uk/comet-volcano-portal/volcano-index/Search-All)
- [Sulfur Dioxide Data](https://disc.gsfc.nasa.gov/datasets/OMPS_NPP_NMSO2_PCA_L2_2/summary?keywords=sulfur%20dioxide)
- [Seismic Data](https://earthquake.usgs.gov/earthquakes/map/?extent=-16.90443,-73.17169&extent=-15.1066,-70.25482&range=search&listOnlyShown=true&baseLayer=ocean&timeZone=utc&search=%7B%22name%22:%22Search%20Results%22,%22params%22:%7B%22starttime%22:%222010-01-01%2000:00:00%22,%22endtime%22:%222024-04-04%2023:59:59%22,%22minlatitude%22:-17.719,%22maxlongitude%22:-70.497,%22minlongitude%22:-77.528,%22latitude%22:-15.787,%22longitude%22:-71.857,%22maxradiuskm%22:50,%22minmagnitude%22:2.5,%22orderby%22:%22time%22%7D%7D)
## Tools/Packages
- Python: We will use Python and Python libraries to visualize and process data
- Pandas: A python library with a useful data storage type (Series) and ways to read data from different file types (most notably, .csv).
- Numpy: Numpy is a python library that will help us manipulate data, as it is effective for mathematical and statistical operations.
- MatPlotLib: This python library allows us to use heatmaps, scatter plots, and other types of plots, along with useful visualization tools.
- Cartopy: This python library pairs with MatPlotLib to create geolocated maps.
- h5py: This python library allows the program to read hdf5 files and load them into numpy arrays and pandas DataFrames
## Planned Methodology
- Examine an eruption case from Sabancaya (Peru) using heat, gas emissions, seismic, and deformation time series.
- Model these data with respect to time, along with known eruptions, to visualize trends before and after eruptions.
- Create 2D spatial plots of heat and deformation at fixed times before, during, and after an eruption.
## Present/Anticipated Challenges
- Finding multiple sets of data from before, during, and after the eruption of a volcano.
- Standardizing data to the same time period for a more clear comparison.
- Cloud cover obstructing thermal sensors.
## Expected Outcomes
- We expect heat, emissions, deformation, and seismic activity to increase leading up to an eruption.
- We also expect these properties to decrease following eruption.
- How will the post-eruption data compare to pre-eruption?

