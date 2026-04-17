import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Illinois Building Inventory", layout="wide")

st.title("Illinois State Building Inventory Analysis")
st.write(
    "This app explores the Illinois state building inventory dataset, "
    "highlighting agency building counts and historical construction trends."
)

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
    return pd.read_csv(url, encoding="latin-1")

df = load_data()

# ── Visualization 1: Bar chart ──────────────────────────────────────────────

st.header("Visualization 1: Top 15 Agencies by Building Count")

agency_counts = (
    df["Agency Name"].value_counts().head(15).reset_index()
)
agency_counts.columns = ["Agency Name", "Count"]

bar = (
    alt.Chart(agency_counts)
    .mark_bar()
    .encode(
        x=alt.X("Count:Q", title="Number of Buildings"),
        y=alt.Y("Agency Name:N", sort="-x", title="Agency"),
        color=alt.Color(
            "Count:Q",
            scale=alt.Scale(scheme="blues"),
            legend=None,
        ),
        tooltip=["Agency Name:N", "Count:Q"],
    )
    .properties(width=750, height=420, title="Top 15 Illinois State Agencies by Building Count")
)

st.altair_chart(bar, use_container_width=True)

st.write(
    """
    **Write-up — Visualization 1:**
    This horizontal bar chart highlights the stark disparity in state-owned building
    ownership across Illinois government agencies. The primary feature I am emphasizing
    is that a small number of agencies — notably the Department of Natural Resources and
    Capital Development Board — account for a disproportionately large share of buildings.
    I chose a horizontal layout because agency names are long nominal strings that render
    far more cleanly on the y-axis than when rotated on the x-axis. Bars are sorted in
    descending order so the viewer's eye moves naturally from most to least. A sequential
    blue color scale is tied to the count to add a second visual cue reinforcing the
    ranking without introducing misleading categorical distinctions. If I had more time, I
    would add an interactive slider letting users set the cutoff (top 5 through top 30
    agencies) and display each agency's percentage share of the total in the tooltip.
    This visualization and the dataset are completely new compared to my Homework 5
    submission, which used the Bigfoot sightings dataset — there is no overlap in dataset
    or plot type.
    """
)

# ── Visualization 2: Interactive scatter plot ────────────────────────────────

st.header("Visualization 2: Square Footage vs. Year Constructed (Interactive)")
st.write(
    "Use the dropdown below to filter by agency. "
    "Pan and zoom are also enabled on the chart."
)

df2 = df[["Square Footage", "Year Constructed", "Agency Name", "City"]].dropna()
df2 = df2[
    (df2["Year Constructed"] > 1800)
    & (df2["Year Constructed"] <= 2024)
    & (df2["Square Footage"] > 0)
    & (df2["Square Footage"] < 2_000_000)
]

agencies = ["All"] + sorted(df2["Agency Name"].dropna().unique().tolist())
selected = st.selectbox("Filter by Agency:", agencies)

plot_df = df2 if selected == "All" else df2[df2["Agency Name"] == selected]

scatter = (
    alt.Chart(plot_df)
    .mark_point(opacity=0.45, size=35)
    .encode(
        x=alt.X(
            "Year Constructed:Q",
            title="Year Constructed",
            scale=alt.Scale(zero=False),
        ),
        y=alt.Y(
            "Square Footage:Q",
            title="Square Footage (log scale)",
            scale=alt.Scale(type="log"),
        ),
        color=alt.Color(
            "Agency Name:N",
            scale=alt.Scale(scheme="tableau20"),
            legend=alt.Legend(title="Agency", symbolLimit=20),
        ),
        tooltip=[
            "Agency Name:N",
            "City:N",
            "Year Constructed:Q",
            "Square Footage:Q",
        ],
    )
    .properties(
        width=750,
        height=480,
        title="Building Square Footage vs. Year Constructed",
    )
    .interactive()
)

st.altair_chart(scatter, use_container_width=True)

st.write(
    """
    **Write-up — Visualization 2:**
    This scatter plot explores the relationship between when an Illinois state building was
    constructed and how large it is, with color encoding distinguishing agencies. The key
    feature I am highlighting is the temporal trend in building size — older buildings tend
    to cluster at smaller square footages, while mid-20th-century construction shows a
    broader spread suggesting a period of large-scale public investment. I chose a
    logarithmic y-axis because square footage spans several orders of magnitude; a linear
    scale would compress the majority of points into an unreadable band near the bottom.
    The primary interactivity is the Streamlit agency dropdown, which goes well beyond
    pan/zoom: selecting a specific agency isolates its construction history, making it easy
    to compare each agency's building patterns over time without the distraction of
    unrelated points. I kept point opacity at 0.45 to reveal overplotting density. Given
    more time, I would link this chart to the bar chart above via a brush selection, so
    clicking a bar in Visualization 1 automatically filters the scatter to that agency.
    As with Visualization 1, the dataset and plot type are entirely distinct from my
    Homework 5 submission — Homework 5 used the Bigfoot sightings dataset with a grouped
    bar chart and a weather scatter plot.
    """
)
