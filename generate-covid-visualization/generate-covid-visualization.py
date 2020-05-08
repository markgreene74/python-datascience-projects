"""
Ref https://www.kaggle.com/giuseppecunsolo/eu-open-data-covid-19-analysis
"""
from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# generate a date str for today
_today = date.today().isoformat()
# set the common title for all the graphs
graph_title = "UK - COVID-19 Deaths after March 1st 2020 - Updated: " + _today

# Load the dataset
xls_dataset = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
covid_dataset = pd.read_excel(xls_dataset)

# create two new columns:
# - deaths per 100_000 population
# - deaths per 100 cases
# (note: population data updated in 2018)
covid_dataset["deaths_per_100k"] = (
    covid_dataset["deaths"] / covid_dataset["popData2018"] * 100_000
)
covid_dataset["deaths_per_100cases"] = (
    covid_dataset["deaths"] / covid_dataset["cases"] * 100
)

# find the data we want to plot
# plot_this contains the data that we want to plot:
# deaths, cases, deaths_per_100k, deaths_per_100cases in a single country ("United_Kingdom")
# after March 1st 2020
country_uk = covid_dataset["countriesAndTerritories"] == "United_Kingdom"
from_01_03 = covid_dataset["dateRep"] >= "2020-03-01"
data_uk_march_01 = covid_dataset[country_uk & from_01_03]
plot_this = data_uk_march_01[
    ["dateRep", "cases", "deaths", "deaths_per_100k", "deaths_per_100cases"]
].sort_values("dateRep")

# plot the data using seaborn and save to png, pdf files
sns.set()

# graph 01
# create a graph using seaborn which display separately deaths per 100k and deaths per 100 cases
_filename = _today + "-COVID-19-UK-data-visualization-01"

fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(14, 10))
fig.suptitle("UK - COVID-19 Deaths after March 1st 2020 - Updated " + _today)

ax1.set_title("deaths_per_100k")
ax1.plot(plot_this["dateRep"], plot_this["deaths_per_100k"])

ax2.set_title("deaths_per_100cases")
ax2.plot(plot_this["dateRep"], plot_this["deaths_per_100cases"])

plt.xlabel("date")
plt.xticks(rotation=45)
# plt.show()
plt.savefig(_filename + ".png")
plt.savefig(_filename + ".pdf")


# graph 02
# plot deaths and cases in a single graph using seaborn
_filename = _today + "-COVID-19-UK-data-visualization-02"

plt.figure(figsize=(14, 10))
g1 = sns.lineplot(
    x="dateRep", y="deaths", data=plot_this, palette="blue", label="deaths"
)
g2 = sns.lineplot(
    x="dateRep", y="cases", data=plot_this, palette="orange", label="cases"
)
plt.ylabel("")
plt.xlabel("")
plt.suptitle(graph_title)
plt.xticks(rotation=45)

# plt.show()
plt.savefig(_filename + ".png")
plt.savefig(_filename + ".pdf")
