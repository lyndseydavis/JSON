"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

import json

infile = open("univ.json", "r")

# converts json to python obj
univ_data = json.load(infile)

# count number of schools
# print(len(univ_data))

# create list of schools that match the correct conferences
# unable to make a single if statement with "or" and all number - wants to append all 649
uni = []
for i in univ_data:
    con = i["NCAA"]["NAIA conference number football (IC2020)"]
    con = int(con)
    if con == 102:
        uni.append(i)
    elif con == 107:
        uni.append(i)
    elif con == 108:
        uni.append(i)
    elif con == 127:
        uni.append(i)
    elif con == 130:
        uni.append(i)

# check length of uni list
# print(len(uni))

# create empty lists for all variables needed to make the 3 maps
(
    lat1,
    lon1,
    lat2,
    lon2,
    lat3,
    lon3,
    hover1,
    hover2,
    hover3,
    size1,
    size2,
    size3,
) = ([], [], [], [], [], [], [], [], [], [], [], [])
# create list of schools and grad rate of women if greater than 50%
for i in uni:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        school_name = i["instnm"]
        grad = i["Graduation rate  women (DRVGR2020)"]
        lon1.append(i["Longitude location of institution (HD2020)"])
        lat1.append(i["Latitude location of institution (HD2020)"])
        hover1.append(f"{school_name}, {grad}%")
        size = 0.0002 * float(i["Total  enrollment (DRVEF2020)"])
        size1.append(size)

# create list of schools and aa enrollment if greater than 10%
for i in uni:
    enroll = i[
        "Percent of total enrollment that are Black or African American (DRVEF2020)"
    ]
    if enroll > 10:
        school_name = i["instnm"]
        lon2.append(i["Longitude location of institution (HD2020)"])
        lat2.append(i["Latitude location of institution (HD2020)"])
        hover2.append(f"{school_name}, {enroll}%")
        size = 0.0005 * float(i["Total  enrollment (DRVEF2020)"])
        size2.append(size)

# create list of schools and off-campus costs if greater than $50,000
for i in uni:
    try:
        price = int(
            i[
                "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
            ]
        )
    except TypeError:
        print("")
    else:
        if price > 50000:
            school_name = i["instnm"]
            lon3.append(i["Longitude location of institution (HD2020)"])
            lat3.append(i["Latitude location of institution (HD2020)"])
            hover3.append(f"{school_name}, ${price}")
            size = 0.0005 * float(i["Total  enrollment (DRVEF2020)"])
            size3.append(size)

"""
# print checks
print(len(lon1))
print(len(lat1))
print(len(lon2))
print(len(lat2))
print(len(lon3))
print(len(lat3))
"""

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Map 1
data1 = [
    {
        "type": "scattergeo",
        "lon": lon1,
        "lat": lat1,
        "text": hover1,
        "marker": {"size": size1, "color": "green"},
        "locationmode": "USA-states",
    }
]

my_layout = Layout(
    title="Power 5 Conference Institutions with over 50% Grad Rate for Women"
)

fig = {"data": data1, "layout": my_layout}

offline.plot(fig, filename="women_grad.html")

# Map 2
data2 = [
    {
        "type": "scattergeo",
        "lon": lon2,
        "lat": lat2,
        "text": hover2,
        "marker": {
            "size": size2,
            "color": "green",
        },
    }
]

my_layout = Layout(
    title="Power 5 Conference Institutions with over 10% Black/African American Enrollment"
)

fig = {"data": data2, "layout": my_layout}

offline.plot(fig, filename="aa_enroll.html")

# Map 3
data3 = [
    {
        "type": "scattergeo",
        "lon": lon3,
        "lat": lat3,
        "text": hover3,
        "marker": {
            "size": size3,
            "color": "green",
        },
    }
]

my_layout = Layout(
    title="Power 5 Conference Institutions with Off-Campus Costs > $50,000"
)

fig = {"data": data3, "layout": my_layout}

offline.plot(fig, filename="off_cost.html")
