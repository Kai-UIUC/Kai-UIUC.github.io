---
name: Bigfoot Sightings Web Development Homework
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/cars.png
description: Exploring Bigfoot sightings across different seasons and weather conditions.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# Bigfoot Sightings: Exploring Seasons and Weather

Below are the links to the original dataset and the Jupyter Notebook containing the Python/Altair analysis:

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/Kai-UIUC/Kai-UIUC.github.io/blob/main/python_notebooks/hw5_viz.ipynb" text="The Analysis" %}
</div>

<br><br><br>

## Visualization 1: Bigfoot Reports by Season

<vegachart schema-url="{{ site.baseurl }}/assets/json/bigfoot_plot1.json" style="width: 100%"></vegachart>

The first visualization is a bar chart that displays the total number of Bigfoot reports across different seasons, broken down by their report classification. For the design choices, I used a nominal encoding for the x-axis (`season`) and a quantitative encoding for the y-axis (count of reports). I chose to color the bars by `classification` (a nominal variable) using Altair's default categorical color scheme, which provides distinct, easily distinguishable hues for the qualitative categories (Class A, B, and C). On the analysis and data transformation side in Python, since the dataset exceeds Altair's default 5,000-row limit, I applied `alt.data_transformers.disable_max_rows()`. To keep the exported JSON lightweight and adhere to GitHub's hosting limits, I passed the raw CSV URL directly into the chart rather than a Pandas DataFrame, relying on Altair's built-in `count()` aggregation to process the data dynamically.

<br>

## Visualization 2: Weather Conditions During Sightings

<vegachart schema-url="{{ site.baseurl }}/assets/json/bigfoot_plot2.json" style="width: 100%"></vegachart>

The second visualization is a scatter plot exploring the weather conditions—specifically Average Temperature and Humidity—present during these sightings. I used quantitative encodings for both the x-axis (`temperature_mid`) and y-axis (`humidity`), and again mapped the `classification` to color. To address potential overplotting, I adjusted the mark opacity to 0.6. For the interactivity component, I implemented a dropdown selection tool bound to the `season` variable. When a specific season is selected, the non-matching points dynamically fade to light gray. This conditional color encoding makes the visualization significantly more clear and interesting, as it allows users to isolate and observe seasonal weather patterns without losing the visual context of the overall dataset. Additionally, I included detailed tooltips showing geographic locations and exact weather metrics to support deeper user exploration.
