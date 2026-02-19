import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import plotly.express as px
    return mo, pl, px


@app.cell
def _(mo):
    mo.md(r"""You may use any and all AI tools for this assignment. You may NOT collaborate with any other human.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Task 1: Read the Data
    Use the chicago_crime_2001_2025.parquet file.
    """
    )
    return


@app.cell
def _(pl):
    df = pl.read_parquet('chicago_crime_2001_2025.parquet')
    df.shape
    return (df,)


@app.cell
def _(df):
    df.glimpse()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Task 2: Prep the Data
    Perform Necessary Modifications for the data set. Convert data types, add columns required for analysis
    """
    )
    return


@app.cell
def _(df, pl):
    df2 = df.with_columns(pl.col('Date').str.to_datetime("%m/%d/%Y %I:%M:%S %p"))
    df2 = df2.with_columns(
        pl.col('Date').dt.year().alias('year'),
        pl.col('Date').dt.month().alias('month'),
        pl.col('Date').dt.day().alias('day'),
        pl.col('Date').dt.hour().alias('hour'),
        pl.col('Date').dt.minute().alias('minute')
        )
    df2.glimpse()
    return (df2,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Task 3: Most Violent Districts
    List the Top 5 districts with the most Violent Crimes in 2024

    Add a markdown cell explaining which crimes you chose as violent and why.
    """
    )
    return


@app.cell
def _(df2):
    #Find the crime types
    crime_types = df2['Primary Type'].unique().sort()
    crime_types
    return


@app.cell
def _(df2, pl):
    violent_crimes = ['HOMICIDE', 'ASSAULT', 'BATTERY', 'CRIMINAL SEXUAL ASSAULT', 'DOMESTIC VIOLENCE', 'CRIM SEXUAL ASSAULT']
    violent_2024= (df2
        .filter((pl.col('year') ==2024) &
                (pl.col('Primary Type').is_in(violent_crimes)))
        .group_by('District')
        .agg(pl.col('ID').n_unique().alias('violent_crime_count'))
        .sort('violent_crime_count', descending=True)
        .head(5)
    )
    violent_2024
    return (violent_crimes,)


@app.cell
def _(mo):
    mo.md(r"""I chose Homicide because that is harming someone to death, assault because that is the attack on someone else, battery because that is repeated physical attacks, crim sexual assult/ criminal sexual assault because that is sexual violence to someone, and domestic violence because that is the harm of a family member.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Task 4: Breakdown by Crime Type
    Provide the Same list as above, but include a breakdown of crime type
    """
    )
    return


@app.cell
def _(df2, pl, violent_crimes):
    crime_breakdown = (df2
        .filter((pl.col('year') ==2024) &
                (pl.col('Primary Type').is_in(violent_crimes)))
        .group_by(['District', 'Primary Type'])
        .agg(pl.col('ID').n_unique().alias('crime_count'))
        .sort(['District', 'crime_count'], descending=[False, True])
        .head(5)
    )
    top_5 = (crime_breakdown
        .group_by('District')
        .agg(pl.col('crime_count').sum().alias('total_crimes'))
        .sort('total_crimes', descending=True)
        .head(5)
        .select('District')
    )
    filtered_crime = (crime_breakdown
                     .join(top_5, on='District')
                     .sort(['District', 'crime_count'], descending=[False, True])
                     )
    filtered_crime
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Task 5: Murder Beats
    Create a polars dataframe showing the top 10 beats by most homicides. Include the District, Community Area, and Homicide count as columns. Sort by homicide count from most to least.
    """
    )
    return


@app.cell
def _(df2, pl):
    homicide_beats = (df2
                     .filter(pl.col('Primary Type') == 'HOMICIDE')
                      .group_by(['Beat', 'District', 'Community Area'])\
                      .agg(pl.col('ID').n_unique().alias('homicide_count'))
                      .sort('homicide_count', descending=True)
                      .head(10)
                     )
    homicide_beats
    return


@app.cell
def _(mo):
    mo.md(r"""Bonus Task 6: Create a heat map of the areas in Chicago with the highest murder rate""")
    return


@app.cell
def _(df2, pl, px):
    homicide_map = (df2
                   .filter((pl.col('Primary Type') == 'HOMICIDE') &
                        (pl.col('Latitude').is_not_null()) &
                        (pl.col('Longitude').is_not_null())
                          )
                   )
    homicide_map = homicide_map.select(['Latitude', 'Longitude', 'Community Area', 'District'])
               
    fig_heatmap = px.density_mapbox(
            homicide_map,
            lat='Latitude',
            lon='Longitude',
            radius=10,
            center=dict(lat=41.8781, lon=-87.6298),
            zoom=10,
            mapbox_style='open-street-map',
            title='Chicago Homicide Heat Map',
            height=700
        )
    fig_heatmap.show()
    return


if __name__ == "__main__":
    app.run()
