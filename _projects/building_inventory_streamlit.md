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

A horizontal bar chart showing the distribution of state-owned buildings across the top 15 Illinois government agencies. Bars are sorted descending and colored with a sequential blue scale to reinforce ranking at a glance.

## Visualization 2: Square Footage vs. Year Constructed (Interactive)

A scatter plot comparing when buildings were constructed against their size in square footage, using a log y-axis to handle the wide range of values. A **Streamlit agency dropdown** provides meaningful interactivity — selecting an agency isolates its historical construction pattern without losing overall context. Color encodes agency identity across the full dataset.

---

*This dataset and both plot types are entirely distinct from the Homework 5 submission, which used the Bigfoot sightings dataset. There is no overlap in dataset or visualization type.*
