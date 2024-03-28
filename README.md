# Observing and Describing a Volcanic Eruption
## Names: 
- Jude Lowe, Lucas Holt, Jack Logan
## Background
- Geophysical methods are used to observe what is going on under the surface and can be used to see what volcanic processes occur.
- The heat (infrared electromagnetic radiation), gases, and seismic waves volcanoes release could be an indicator of volcanic activity.
- Displacement measurements can indicate deformation caused by volcanism.
- Our target is Sabancaya, an active stratovolcano in Peru. What can past data tell us about current and future volcanic activity for this area?
## Problem Statement
- What trends can we observe in geophysical data before, during, and after a volcanic eruption period?
## Data Sets
- [Mirova DB for heat](https://www.mirovaweb.it/)
- [Smithsonaion DB for eruptions](https://volcano.si.edu/database/search_eruption_results.cfm)
- [Deformation DB](https://comet.nerc.ac.uk/comet-volcano-portal/volcano-index/Search-All)
## Tools/Packages
- Python: We will use Python and Python libraries to visualize and process data
- ObsPy and Seisbench: ObsPy and Seisbench are two Python libraries that are used to analyze seismic data.
- Pandas: A python library with a useful data storage type (Series) and ways to read data from different file types (most notably, .csv).
- Numpy: Numpy is a python library that will help us manipulate data, as it is effective for mathematical and statistical operations.
- MatPlotLib: This python library allows us to use heatmaps, scatter plots, and other types of plots, along with useful visualization tools.
## Planned Methodology
- Examine an eruption case from Sabancaya (Peru) using heat, gas emissions, seismic, and deformation time series.
- Model these data with respect to time, along with known eruptions, to visualize trends before and after eruptions.
- Create 2d spatial plots of heat and deformation at fixed times before, during, and after an eruption.
## Present/Anticipated Challenges
- Finding multiple sets of data from before, during, and after the eruption of a volcano.
- Standardizing data to the same time period for a more clear comparison.
- Cloud cover obstructing thermal sensors.
## Expected Outcomes
- We expect heat, emissions, deformation, and seismic activity to increase leading up to an eruption.
- We also expect these properties to decrease following eruption.
- How will the post-eruption data compare to pre-eruption?

