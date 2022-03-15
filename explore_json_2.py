import json

infile = open("eq_data_30_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# converts json to python obj
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# create list of earthquakes
list_of_eqs = eq_data["features"]
print(len(list_of_eqs))

# create list of magnitudes, longitudes, latitudes
mags, lons, lats, hover_text = [], [], [], []
for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lon = eq["geometry"]["coordinates"][0]
    lons.append(lon)
    lat = eq["geometry"]["coordinates"][1]
    lats.append(lat)
    title = eq["properties"]["title"]
    hover_text.append(title)

# print first 10
print(mags[:10])
print(lons[:10])
print(lats[:10])

# create graph
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_text,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
