---
name: Bigfoot Sightings Visualization Project
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/cars.png
description: An interactive data visualization project exploring seasonal patterns and weather conditions in reported Bigfoot sightings.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# Bigfoot Sightings: Seasons, Classification, and Weather

This project shows how I used Python, Altair, and Vega-Lite to turn a raw sightings dataset into a lightweight web-based visualization. I wanted the final result to do two things well: summarize the dataset clearly and give users one interactive view that rewards exploration.

Below are the links to the original dataset and the notebook I used for the analysis:

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/Kai-UIUC/Kai-UIUC.github.io/blob/main/python_notebooks/Bigfoot_hw.ipynb" text="The Analysis" %}
</div>

<br><br><br>

## Visualization 1: Reports by Season

<vegachart schema-url="https://kai-uiuc.github.io/assets/json/bigfoot_plot1.json" style="width: 100%"></vegachart>

I started with a grouped bar chart to answer the most basic question first: when are sightings reported most often, and how does that differ by classification? I mapped `season` to the x-axis, used the count of records on the y-axis, and colored each bar by `classification` so the different report types stay easy to compare.

On the implementation side, I built the chart in Altair and kept the output web-friendly by pointing the visualization directly to the source CSV instead of embedding a large processed table. Because the dataset is larger than Altair's default row limit, I disabled the max-row restriction during development and relied on Vega-Lite's built-in aggregation for the final chart.

<br>

## Visualization 2: Weather Conditions During Sightings

<vegachart schema-url="https://kai-uiuc.github.io/assets/json/bigfoot_plot2.json" style="width: 100%"></vegachart>

For the second view, I moved from summary to exploration. This scatter plot compares `temperature_mid` and `humidity` to show the weather conditions associated with reported sightings. I kept the color encoding on `classification` for consistency across the page and lowered the point opacity to reduce overplotting.

The main interaction is a season dropdown. When a user selects a season, matching points stay highlighted while the rest fade into the background. That interaction makes it easier to compare seasonal clusters without losing context. I also added tooltips for state, county, season, temperature, and humidity so the chart can support both quick scanning and closer inspection.
