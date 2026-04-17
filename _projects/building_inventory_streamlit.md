---
name: Illinois Building Inventory — Streamlit App
tools: [Python, Streamlit, Altair]
image: assets/pngs/cars.png
description: An interactive Streamlit app exploring Illinois state building inventory data, featuring agency building counts and construction history trends.
---

# Illinois State Building Inventory Analysis

This project is a Streamlit web app hosted on HuggingFace Spaces that explores the Illinois state building inventory dataset. The app contains two Altair visualizations and a detailed write-up.

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://huggingface.co/spaces/0xkxx/is445-building-inventory" text="Open Streamlit App" %}
</div>

<br><br><br>

## Visualization 1: Top 15 Agencies by Building Count

This horizontal bar chart highlights the distribution of state-owned buildings across the top 15 Illinois government agencies. The primary feature emphasized is the stark disparity in building ownership — a small number of agencies account for a disproportionately large share of buildings. Bars are sorted in descending order so the most prominent agencies appear immediately at the top. A sequential blue color scale is tied to the count to add a secondary visual cue reinforcing the ranking. If I had more time, I would add an interactive slider letting users set the cutoff (top 5 through top 30 agencies) and display each agency's percentage share of the total in the tooltip.

**Overlap with Homework 5:** This visualization uses the `building_inventory.csv` dataset, which was not used in Homework 5. Homework 5 used the Bigfoot sightings dataset (`bfro_reports_fall2022.csv`). The plot type (horizontal sorted bar chart of agency counts) is also entirely different from anything submitted in Homework 5. There is no overlap in dataset or plot type.

## Visualization 2: Square Footage vs. Year Constructed (Interactive)

This scatter plot explores the relationship between when an Illinois state building was constructed and how large it is, with color encoding distinguishing agencies. The key feature highlighted is the temporal trend in building size — older buildings cluster at smaller square footages, while mid-20th-century construction shows a broader spread. A logarithmic y-axis is used because square footage spans several orders of magnitude. The primary interactivity is a **Streamlit agency dropdown** that filters the scatter plot to a single agency — this goes beyond pan/zoom or basic tooltips by letting users isolate and compare each agency's construction history over time. If I had more time, I would link this chart to Visualization 1 via brush selection, so clicking a bar automatically filters the scatter.

**Overlap with Homework 5:** This visualization also uses the `building_inventory.csv` dataset, which is entirely different from the Bigfoot dataset used in Homework 5. The scatter plot comparing square footage versus year constructed is a different variable pairing and plot purpose from the Homework 5 weather scatter plot (temperature vs. humidity). There is no overlap in dataset, variables, or analytical focus.
