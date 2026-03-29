---
name: UFO Sightings Analysis
tools: [Python, Altair, Vega-Lite]
image: assets/pngs/cars.png
description: A comprehensive study of UFO shapes and their geographical distribution patterns.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# UFO Sightings: A Spatial and Morphological Study

In this project, I explore the global UFO sightings dataset to understand the most common shapes reported and their geographical distribution.

<div class="left">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/ufo-scrubbed-geocoded-time-standardized-00.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/Kai-UIUC/Kai-UIUC.github.io/blob/main/python_notebooks/Workbook.ipynb" text="The Analysis" %}
</div>

<br><br><br>

## Visualization 1: Distribution of UFO Shapes

<vegachart schema-url="https://kai-uiuc.github.io/assets/json/ufo_plot1.json" style="width: 100%"></vegachart>

The first visualization is a horizontal bar chart showing the frequency of different UFO shapes. I used a nominal encoding for the `shape` on the y-axis and a quantitative encoding for the count on the x-axis. The data is sorted to immediately highlight the most frequently reported shapes, such as 'light' and 'circle'. To ensure the web application remains performant, I performed data cleaning in Python, specifically handling malformed coordinates and extracting a random sample of 5,000 records.

<br>

## Visualization 2: Interactive Geographical Map

<vegachart schema-url="https://kai-uiuc.github.io/assets/json/ufo_plot2.json" style="width: 100%"></vegachart>

The second visualization maps the sightings based on their geographic coordinates using quantitative encodings for both longitude and latitude. The key interactivity is a dropdown selection tool bound to the `shape` variable. This allows users to filter the map and observe if certain UFO shapes are more common in specific regions. When a selection is made, the matching points remain colored while others are grayed out, significantly improving the clarity of regional sighting patterns.
