import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Page Settings
favicon = "images/favicon.ico"
st.set_page_config(page_title="Happy Holiday Season", page_icon=favicon)

# Load Data in Dataframe
@st.cache(suppress_st_warning=True)
def get_data():
    df = pd.read_excel("data/Japan-1950-2020.xlsx")
    return df


df = get_data()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    "<h1 style='text-align: center;'>Happy Holiday Season</h1>", unsafe_allow_html=True
)
st.write("")

year = st.slider("Select Year:", min_value=1950, max_value=2020, value=1950)
st.markdown(f"**Population Pyramid Japan {year}**")
mask = df["Year"] == year
y = df[mask]["Age"]
x1 = df[mask]["M"]
x2 = df[mask]["F"] * -1

# Create Data for "Tree Trunk"
tree_data = {
    "Age": ["-", "--"],
    "M": [1000000, 1000000],
    "F": [-1000000, -1000000],
}
tree_trunk = pd.DataFrame.from_dict(tree_data)
y_tree_trunk = tree_trunk["Age"]
x1_tree_trunk = tree_trunk["M"]
x2_tree_trunk = tree_trunk["F"]


fig = go.Figure()

# Tree Trunk
fig.add_trace(
    go.Bar(
        y=y_tree_trunk,
        x=x1_tree_trunk,
        showlegend=False,
        orientation="h",
        marker=dict(
            color="rgba(102, 51, 0, 1)",
            line=dict(color="rgba(102, 51, 0, 1.0)", width=3),
        ),
    )
)
fig.add_trace(
    go.Bar(
        showlegend=False,
        y=y_tree_trunk,
        x=x2_tree_trunk,
        orientation="h",
        marker=dict(
            color="rgba(102, 51, 0, 1)",
            line=dict(color="rgba(102, 51, 0, 1.0)", width=3),
        ),
    )
)


# Population Data
fig.add_trace(
    go.Bar(
        y=y,
        x=x1,
        name="Male",
        orientation="h",
        marker=dict(
            color="rgba(0, 135, 62, 0.6)",
            line=dict(color="rgba(0, 135, 62, 1.0)", width=3),
        ),
    )
)
fig.add_trace(
    go.Bar(
        y=y,
        x=x2,
        name="Female",
        orientation="h",
        marker=dict(
            color="rgba(0, 135, 62, 0.6)",
            line=dict(color="rgba(0, 135, 62, 1.0)", width=3),
        ),
    )
)


# Decoration
fig.add_trace(
    go.Scatter(
        y=y,
        x=x1,
        name="Male",
        showlegend=False,
        mode="markers",
        marker_color=x1,
        marker_size=10,
    )
)

fig.add_trace(
    go.Scatter(
        y=y,
        x=x2,
        name="Female",
        showlegend=False,
        mode="markers",
        marker_color=x1,
        marker_size=10,
    )
)


# Fig Layout
fig.update_layout(
    margin=dict(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=40,  # top margin
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    title="🎇",
    title_font_size=24,
    title_x=0.535,
    title_y=0.91,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title="Age Group",
        titlefont_size=14,
        tickfont_size=12,
        showgrid=False,
        titlefont_color="#f5f5f5",
        tickfont_color="#f5f5f5",
    ),
    xaxis=dict(
        title="Population in Mio",
        showgrid=False,
        titlefont_size=14,
        tickfont_size=12,
        titlefont_color="#f5f5f5",
        tickfont_color="#f5f5f5",
        tickvals=[-4000000, -2000000, 0, 2000000, 4000000],
        ticktext=["4M", "2M", "0", "2M", "4M"],
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor="rgba(255, 255, 255, 0)",
        bordercolor="rgba(255, 255, 255, 0)",
    ),
    barmode="relative",
    bargap=0.0,  # gap between bars of adjacent location coordinates.
    bargroupgap=0,  # gap between bars of the same location coordinate.
)

st.plotly_chart(fig)
st.markdown(f"*Datasource: https://www.populationpyramid.net/japan/{year}/*")
