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
print(len(univ_data))

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
print(len(uni))

name1, name2, name3, grad_women, aa_enroll, off_price = [], [], [], [], [], []
for i in uni:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        school_name = i["instnm"]
        name1.append(school_name)
        grad = i["Graduation rate  women (DRVGR2020)"]
        grad_women.append(grad)

for i in uni:
    if (
        i["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        > 10
    ):
        school_name = i["instnm"]
        name2.append(school_name)
        enroll = i["Graduation rate  women (DRVGR2020)"]
        aa_enroll.append(enroll)

for i in uni:
    try:
        price = int(
            i[
                "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
            ]
        )
    except TypeError:
        print("None")
    else:
        if price > 50000:
            school_name = i["instnm"]
            name3.append(school_name)
            price = i[
                "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
            ]
            off_price.append(price)

"""
#print checks
print(len(name1))
print(len(grad_women))
print(len(name2))
print(len(aa_enroll))
print(len(name3))
print(len(off_price))
"""
