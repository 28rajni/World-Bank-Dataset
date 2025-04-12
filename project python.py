import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#loading dataset
data=pd.read_csv("C:\\Users\\ASUS\\OneDrive\\LPU\\SEM. 4\\INT375 Python\\WorldBankDataSet.csv")
print(data)
#exploring dataset
print("Information: \n",data.info())
print("Description: \n",data.describe())
#Remove duplicates rows if present
data = data.drop_duplicates()
#Handling missing values
print("missing values", data.isnull().sum())
data = data.dropna(subset=["GDP (USD)", "GDP per capita (USD)", "Life expectancy at birth (years)"])
#missing numeric values with column mean
numeric_cols = data.select_dtypes(include="number").columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
print("final DataFrame shape:", data.shape)
print("\nRemaining missiing values:\n", data.isnull().sum())
print("\nData info:")
data.info()
#after cleaning dataset
data.to_csv("WorldBank_Cleaned.csv", index=False)
print("new dataset")
#Basic operation performed
print("1st 10 rows of Dataset: \n",data.head(10))
print("1st 10 rows of Dataset: \n",data.tail(10))
print("Shape of Dataset: \n",data.shape)
print("Column of Dataset: \n",data.columns)
#rename the columns name
data.rename(columns={
    "GDP (USD)": "GDP",
    "GDP per capita (USD)": "GDPperCapita"
}, inplace=True)
# Group by Year and get global average GDP and GDP per Capita
global_trends = data.groupby("Year")[["GDP", "GDPperCapita"]].mean().reset_index()
# Plot of Global GDP & GDP per Capita Trends Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=global_trends, x="Year", y="GDP", label="Global Avg GDP", marker="o")
sns.lineplot(data=global_trends, x="Year", y="GDPperCapita", label="Global Avg GDP per Capita", marker="s")
plt.title("Global Economic Growth: GDP & GDP per Capita Over Time")
plt.xlabel("Year")
plt.ylabel("USD")
plt.show()
# Group by Region and Year
region_trends = data.groupby(["Region", "Year"])[["GDP", "GDPperCapita"]].mean().reset_index()
# Plot GDP per capita trend by region
plt.figure(figsize=(14, 7))
sns.lineplot(data=region_trends, x="Year", y="GDPperCapita", hue="Region", marker="o")
plt.title("GDP per Capita Trends by Region Over Time")
plt.xlabel("Year")
plt.ylabel("GDP per Capita (USD)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
#rename the columns name
data.rename(columns={
    "Infant mortality rate (per 1,000 live births)": "InfantMortality",
    "Life expectancy at birth (years)": "LifeExpectancy",
    "Death rate, crude (per 1,000 people)": "DeathRate"
}, inplace=True)
# Group by Year to get global averages
health_trends = data.groupby("Year")[["InfantMortality", "LifeExpectancy", "DeathRate"]].mean().reset_index()
# Plot Global Health Trends Over Time
plt.figure(figsize=(14, 6))
sns.lineplot(data=health_trends, x="Year", y="InfantMortality", label="Infant Mortality", marker="o")
sns.lineplot(data=health_trends, x="Year", y="LifeExpectancy", label="Life Expectancy", marker="s")
sns.lineplot(data=health_trends, x="Year", y="DeathRate", label="Death Rate", marker="^")
plt.title("Global Health Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Rate")
plt.legend()
plt.tight_layout()
plt.show()
# Group by Region and Year
region_health = data.groupby(["Region", "Year"])[["InfantMortality", "LifeExpectancy", "DeathRate"]].mean().reset_index()
# Plot: Life Expectancy by Region
plt.figure(figsize=(14, 6))
sns.lineplot(data=region_health, x="Year", y="LifeExpectancy", hue="Region", marker="o")
plt.title("Life Expectancy by Region Over Time")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
#rename the columns name
data.rename(columns={
    "Birth rate, crude (per 1,000 people)": "BirthRate",
    "Population density (people per sq. km of land area)": "PopulationDensity",
    "Unemployment (% of total labor force) (modeled ILO estimate)": "UnemploymentRate"
}, inplace=True)
# Group by Year for global average trends
pop_trends = data.groupby("Year")[["BirthRate", "PopulationDensity", "UnemploymentRate"]].mean().reset_index()
#plot: birth rate over time
plt.figure(figsize=(10, 6))
sns.barplot(data=pop_trends, x="Year", y="BirthRate", hue="Year", palette="viridis", legend=False)
plt.title("Global Average Birth Rate Over Time")
plt.ylabel("Birth Rate (per 1,000 people)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#plot: population density over time
plt.figure(figsize=(10, 6))
sns.barplot(data=pop_trends, x="Year", y="PopulationDensity", hue="Year",  palette="mako", legend=False)
plt.title("Global Average Population Density Over Time")
plt.ylabel("People per sq. km")
plt.xticks(rotation=45)
plt.show()
#plot: unemployment rate over time
plt.figure(figsize=(10, 6))
sns.barplot(data=pop_trends, x="Year", y="UnemploymentRate", hue="Year",  palette="rocket", legend=False)
plt.title("Global Average Unemployment Rate Over Time")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()
#rename the columns
data.rename(columns={
    "Individuals using the Internet (% of population)": "InternetUsers"
}, inplace=True)

# number of countries by income group
#plot:
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="IncomeGroup", hue="IncomeGroup",  palette="pastel", legend=False)
plt.title("Number of Countries by Income Group")
plt.xlabel("Income Group")
plt.ylabel("Count")
plt.show()
# Check for non-null values in Internet usage column
data["InternetDataAvailable"] = data["InternetUsers"].notnull()
#availability of internet access data
plt.figure(figsize=(6, 4))
sns.countplot(data=data, x="InternetDataAvailable", hue="InternetDataAvailable", palette="Set2", legend=False)
plt.title("Availability of Internet Access Data")
plt.xlabel("Internet Data Available")
plt.ylabel("Count")
plt.xticks([0, 1], ["No", "Yes"])
plt.show()
#GDP by income group
#plot:
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="IncomeGroup", y="GDP", hue="IncomeGroup",  palette="coolwarm", legend=False)
plt.title("GDP Distribution by Income Group")
plt.ylabel("GDP (USD)")
plt.xticks(rotation=45)
plt.show()
#life expectancy by income group
#plot:
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="IncomeGroup", y="LifeExpectancy", hue="IncomeGroup", palette="Set2", legend=False)
plt.title("Life Expectancy by Income Group")
plt.ylabel("Life Expectancy (Years)")
plt.xticks(rotation=45)
plt.show()
# correlation heatmap of world bank indicators
numeric_data = data.select_dtypes(include=["float64", "int64"])
numeric_data = numeric_data.dropna(axis=1, thresh=int(0.6 * len(numeric_data)))  # keep cols with >=60% non-NA
#Compute correlation matrix
corr_matrix = numeric_data.corr()
#Plot the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, square=True)
plt.title("Correlation Heatmap of World Bank Indicators", fontsize=14)
plt.show()
#kde plot: life expectancy by income group
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data, x="LifeExpectancy", hue="IncomeGroup", fill=True, common_norm=False, palette="muted")
plt.title("Life Expectancy Distribution by Income Group")
plt.xlabel("Life Expectancy (Years)")
plt.ylabel("Density")
plt.show()
#Scatter plot: Internet Users vs GDP per capita
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="GDPperCapita", y="InternetUsers", hue="IncomeGroup", palette="Set1")
plt.title("Internet Usage vs GDP per Capita")
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Internet Users (% of Population)")
plt.show()
#Pair plot: Selected development indicators
# Select key columns
selected_cols = ["GDPperCapita", "LifeExpectancy", "InternetUsers", "IncomeGroup"]
pair_data = data[selected_cols].dropna()
sns.pairplot(pair_data, hue="IncomeGroup", palette="Set2", diag_kind="kde", corner=True)
plt.suptitle("Pair Plot of Selected Development Indicators", y=1.02)
plt.show()
#Pie plot: Proportions of records by income group
income_counts = data["IncomeGroup"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(income_counts, labels=income_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Proportion of Records by Income Group")
plt.axis("equal")  # Equal aspect ratio ensures pie is a circle
plt.show()
#Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="GDPperCapita", bins=30, kde=True, color="skyblue")
plt.title("Histogram of GDP per Capita")
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Frequency")
plt.show()

















