import pandas as pd
data = pd.read_excel("bikers.xlsx")

# create a copy whose is yes
bike_purchasers = data[data["Purchased Bike"] == "Yes"].copy()

bike_purchasers["Income"] = bike_purchasers["Income"].apply(
    lambda x: float(str(x).replace("$", "").replace(",", ""))
)

total_income = bike_purchasers["Income"].sum()
bike_purchased_count = len(bike_purchasers)

# Calculate the average income
if bike_purchased_count > 0:  
    avg_income = total_income // bike_purchased_count
print("The average income of people who purchased a bike is:", avg_income)


# create a copy whose is No
bike_purchasers1 = data[data["Purchased Bike"] == "No"].copy()
bike_purchasers1["Income"] = bike_purchasers1["Income"].apply(
    lambda x: float(str(x).replace("$", "").replace(",", ""))
)

total_income = bike_purchasers1["Income"].sum()
bike_purchased_count = len(bike_purchasers1)
if bike_purchased_count > 0:  
    avg_income = total_income // bike_purchased_count
    print("The average income of people who  doesn't purchased a bike is:", avg_income)
print()

#Regions
countregions = data["Region"].value_counts()
print("Regions represented here:")
for region, count in countregions.items():
    print(f"{region}: {count}")
print()


# Region-wise purchase percentage
data["purchased"] = data["Purchased Bike"].map({"Yes": 1, "No": 0})
region_percent = data.groupby("Region")["purchased"].mean() * 100
print("Percentage of citizens buying the bike by region:")
for region, percent in region_percent.items():
    print(f"{region}: {round(percent, 2)}%")
print()


#percentage of male and female buying the bike
data["Gender_update"] = data["Gender"].map({"M": 1, "F": 0})
region_percent_1 = data.groupby("Gender_update")["purchased"].mean() * 100
print("Gender Based Purchase of Bikes")
print("Female buying Bike",region_percent_1[0],"%")
print("Male buying Bike",float(region_percent_1[1]),"%")
print()