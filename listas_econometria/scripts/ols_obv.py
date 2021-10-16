# packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.iolib.summary2 import summary_col

# opening the data
df = pd.read_excel("listas_econometria\lista3\lista3.xlsx", sheet_name=0, header=0)
print(df)

# Context:
# we have a dataframe with 3,000 cities (municipio) which received (or not) three different public policies (pol_A, pol_B, pol_C).
# these policies wants to reduce the infant mortality rate (IMR, taxa de mortalidade infantil) on that cities.
# two policies were randomized, but the third one were focused on poor cities (pobreza; taxa de pobreza).
# besides that, two policies are measured in "r$/capita" and the latter is a simple binary variable.
# finally, we also have a variable which indicates if a city has suffered with drought (seca) or not.

# First exercise: identify which policies were randomized using descriptive statistics and OLS, if necessary

# we can do that by different ways:
# 1. matrix correlation (and corrplot)
dfcorr = df[["IMR", "pol_A", "pol_B", "pol_C", "pobreza", "seca"]]
corrmat = dfcorr.corr()
print(corrmat)

cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)
sns_plot = sns.heatmap(corrmat, cmap=cmap, vmin=-1, vmax=1, square=True, linewidths=5, cbar_kws={"shrink": .8})
title = 'Correlation matrix'
plt.title(title, loc='center', fontsize=14)
sns_plot = sns_plot.get_figure()
sns_plot.savefig("listas_econometria\outputs\corrplot.png")
plt.clf()

# 2. simple regression
reg1 = ols("pol_A ~ pobreza", df).fit() # pol_A ~ y
print(reg1.summary())

reg2 = ols("pol_B ~ pobreza", df).fit() # pol_B ~ y
print(reg2.summary())

reg3 = ols("pol_C ~ pobreza", df).fit() # pol_C ~ y
print(reg3.summary())

outreg = summary_col([reg1, reg2, reg3], stars=True)
print(outreg)

# 3. scatterplot + regression
ols_plot = sns.regplot(x="pobreza", y="pol_A", data=df) # pol_A ~ y
fig = ols_plot.get_figure()
fig.savefig("listas_econometria\outputs\ols_plota.png")
plt.clf()

ols_plot = sns.regplot(x="pobreza", y="pol_B", data=df) # pol_B ~ y
fig = ols_plot.get_figure()
fig.savefig("listas_econometria\outputs\ols_plotb.png")
plt.clf()

ols_plot = sns.regplot(x="pobreza", y="pol_C", data=df) # pol_C ~ y
fig = ols_plot.get_figure()
fig.savefig("listas_econometria\outputs\ols_plotc.png")
plt.clf()

# second exercise: interpreting ols and handling with ommited variable bias
reg1 = ols("IMR ~ pol_A", df).fit()
reg2 = ols("IMR ~ pol_B", df).fit()
reg3 = ols("IMR ~ pol_C", df).fit()
reg4 = ols("IMR ~ pol_A + pol_B + pol_C", df).fit()
reg5 = ols("IMR ~ pol_A + pol_B + pol_C + pobreza", df).fit() # pol_C reverses sign after controlling for poverty
reg6 = ols("IMR ~ pol_A + pol_B + pol_C + pobreza + seca", df).fit()

outreg = summary_col([reg1, reg2, reg3, reg4, reg5, reg6], stars=True)
print(outreg)

# third exercise: properties of multiple ols
