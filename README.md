# Observing and Describing a Volcanic Eruption 
Jude Lowe (@judelowe): Ground Deformation Data
<br>Lucas Holt (@DimensionalSummation): Thermal Imaging Data
<br>Jack Logan (@jackplogan33): Seismic and SO<sub>2</sub> Data

## Project Summary
Using skills and tools learned in this course, we researched and analyzed different geophysical properties in the Sabancaya Volcano, Peru. We analyzed sulfur dioxide gas emissions, seismic events, ground deformation, and heat anomaly to decipher any correlations between these of volcanic processes during the volcano's eruptive period.

## How to use this repository
This repository contains a notebooks folder, a figures folder, presentation slides with our findings, and an environment file. Inside the notebooks folder are the final notebooks for each team member's contribution and the dev file that contains the developmental notebooks.

To reproduce our project, the data must be downloaded from the respective databases below. The environment file contains all of the software packages used in this project and must be downloaded to reproduce it properly. To reproduce the project for your own volcano, check with the Smithsonian Institute database for coordinates and events, then download the data for that specific volcano from each of the databases.

## Background

Volcanic eruptions are powerful geologic processes that can cause a lot of destruction and pose a threat to humans. It is estimated that 500 million people live in the shadow of an active volcano (Kitchen, 2023). Understanding more about the processes and trends in geophysical processes of active volcanoes can help us implement better warning systems for people who live near active volcanoes.

Volcanoes often give warning signs before they erupt. They can emit more gases, different types of gases, the ground can deform, earthquakes can increase in intensity and frequency, or alter their heat flow (USGS, 2019). Because of these processes, we chose to investigate the emissions of sulfur dioxide (SO<sub>2</sub>), seismic activity, heat, and ground deformation of an active volcano. 

Using the Smithsonian Institute's volcanic index, we found an active volcano in Peru called Vulcan Sabancaya. This volcano has been actively erupting since November 2016, with an explosive index as high as 3 (Global Volcanism Program | Sabancaya, n.d.). Sabancaya has coordinates of 15.787°S 71.857°W, and the volcano number 354006.

### Problem Statement
What trends can we observe in geophysical data during a volcanic eruption period?

## Data Sets
[Smithsonian Institution Database](https://volcano.si.edu/volcano.cfm?vn=354006)
- To find volcanoes and eruptions

[MIROVA Database](https://www.mirovaweb.it/?action=volcanoDetails_OLI&volcano_id=354006)
- For preprocessed thermal anomaly data

[COMET Database](https://comet.nerc.ac.uk/comet-volcano-portal/volcano-index/South%20America/Peru/Sabancaya/S1_analysis)
- For preprocessed deformation data

[NASA GES DISC](https://disc.gsfc.nasa.gov/datasets/OMPS_NPP_NMSO2_PCA_L2_2/summary?keywords=sulfur%20dioxide)
- For OMPS/NPP Sulfur Dioxide Data

[USGS National Earthquake Information Center](https://earthquake.usgs.gov/earthquakes/map/?extent=-16.90443,-73.17169&extent=-15.1066,-70.25482&range=search&listOnlyShown=true&baseLayer=ocean&timeZone=utc&search=%7B%22name%22:%22Search%20Results%22,%22params%22:%7B%22starttime%22:%222010-01-01%2000:00:00%22,%22endtime%22:%222024-04-04%2023:59:59%22,%22minlatitude%22:-17.719,%22maxlongitude%22:-70.497,%22minlongitude%22:-77.528,%22latitude%22:-15.787,%22longitude%22:-71.857,%22maxradiuskm%22:50,%22minmagnitude%22:2.5,%22orderby%22:%22time%22%7D%7D)
- Uses USGS sensors to find seismic events near the volcano
- Refined the search to a 50km radius around the peak.

## Tools/Packages
- [Python](https://www.python.org/): We will use Python and Python libraries to visualize and process data
- [Pandas](https://pandas.pydata.org/): A Python library with useful data storage processing (DataFrame) and ways to read data from different file types (most notably, .csv).
- [Numpy](https://numpy.org/): Numpy is a Python library that will help us manipulate data, as it is effective for mathematical and statistical operations.
- [MatPlotLib](https://matplotlib.org/): This python library allows us to use heatmaps, scatter plots, and other types of plots, along with useful visualization tools.
- [Cartopy](https://pypi.org/project/Cartopy/): This python library pairs with MatPlotLib to create geolocated maps.
- [h5py](https://www.h5py.org/): This python library allows the program to read hdf5 files and load them into numpy arrays and pandas DataFrames
- [imageio](https://pypi.org/project/imageio/): This library makes GIF animations from images to aid visualisation.

## Methodology/Approach
- Examine an eruptive period from Sabancaya, Peru using heat, gas emissions, earthquake, and deformation time series.
- Model these data with respect to time to visualize trends.
- Create 2D spatial plots of deformation, emissions, and seismic events at fixed times during the eruption.

## Summary of Results
- Seismic events tend to happen around/near the coordinates of deformation ​
- Seismic events appear to have a reverse correlation to Sulfur Dioxide emissions​
- Hot pixels in thermal images occur in clusters

## Future Directions
- Use an API to access a cloud version of TROPOMI S5-P data.
    - Sentinel 5 data has a higher resolution than the OMPS/NPP data used for the project, but the files are several magnitudes larger.
    - Using an API or cloud version would remove the need to download data.
- Look at a specific eruptive event on a shorter time frame from the [Smithsonian database](https://volcano.si.edu/volcano.cfm?vn=354006) eruptive history tab.
- Find and use Geospatial data for thermal anomalies
- Check other stratovolcanoes for similarities
- Apply machine learning algorithms to predict eruptions for the specific site

## Contribution Statement
Jack was responsible for all the data acquisition and processing of the sulfur dioxide emissions and seismic events. He also created all of the graphs and maps for the analysis of the sulfur dioxide and seismic data. 

Lucas was responsible for the processing and analysis of the thermal index data.

Jude was responsible for the processing and analysis of the deformation data. This included reproducing the maps from the COMET website and overlaying the seismic events on the same plot.

## References
Can Li, Nickolay A. Krotkov, Peter Leonard, Joanna Joiner (2020), OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km V2, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: Apr 14, 2024, 10.5067/MEASURES/SO2/DATA205

Global Volcanism Program | Sabancaya. (n.d.). Smithsonian Institution | Global Volcanism Program. https://volcano.si.edu/volcano.cfm?vn=354006

K, B. (2022, May 29). Visualizing the Invisible SO2 with NASA Data and Python. Medium. https://towardsdatascience.com/visualize-the-invisible-so2-with-nasa-data-and-python-2619f8ed4ea1

Kitchen, D. (2023, July 14). Living near the fire: 500 million people worldwide have active volcanoes as neighbors. Phys.org. https://phys.org/news/2023-07-million-people-worldwide-volcanoes-neighbors.html

USGS. (2019). How Can We Tell When a Volcano Will erupt? Usgs.gov. https://www.usgs.gov/faqs/how-can-we-tell-when-a-volcano-will-erupt
