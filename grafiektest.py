import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
sns.set()

df_url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/ilc_peps01n.tsv.gz"
df = pd.read_table(df_url, sep='\t', na_values=": ")


cols = ['2021 ', '2020 ', '2019 ', '2017 ', '2016 ']
df[cols] = df[cols].apply(lambda x: x.str.rstrip(" bp"))
df[cols] = df[cols].apply(lambda x: x.astype(float))

Headername = ["Type", "2021", "2020", "2019", "2018", "2017", "2016", "2015"]
df.columns= Headername
dfclean = df[df["Type"].str.contains("PC,TOTAL,T")]
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,EU']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,EU28']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,EA']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,EA18']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,AL']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,CH']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,EL']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,IS']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,ME']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,MK']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,NO']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,RS']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,TR']
dfclean = dfclean[dfclean['Type'] != 'PC,TOTAL,T,UK']

dfclean = dfclean.reset_index(drop=True)
dfclean = dfclean.set_index('Type')
dfclean = dfclean.rename(index={'PC,TOTAL,T,AT':'Austria',
                     'PC,TOTAL,T,BE':'Belgium',
                     'PC,TOTAL,T,BG':'Bulgaria',
                     'PC,TOTAL,T,CY':'Cyprus',
                     'PC,TOTAL,T,CZ':'Czechia',
                     'PC,TOTAL,T,DE':'Germany',
                     'PC,TOTAL,T,DK':'Denmark',
                     'PC,TOTAL,T,EA19':'Euro Area',
                     'PC,TOTAL,T,EE':'Estonia',
                     'PC,TOTAL,T,ES':'Spain',
                     'PC,TOTAL,T,EU27_2020':'Europe',
                     'PC,TOTAL,T,FI':'Finland',
                     'PC,TOTAL,T,FR':'France',
                     'PC,TOTAL,T,HR':'Croatia',
                     'PC,TOTAL,T,HU':'Hungary',
                     'PC,TOTAL,T,IE':'Ireland',
                     'PC,TOTAL,T,IT':'Italy',
                     'PC,TOTAL,T,LT':'Lithuania',
                     'PC,TOTAL,T,LU':'Luxembourg',
                     'PC,TOTAL,T,LV':'Latvia',
                     'PC,TOTAL,T,MT':'Malta',
                     'PC,TOTAL,T,NL':'Netherlands',
                     'PC,TOTAL,T,PL':'Poland',
                     'PC,TOTAL,T,PT':'Portugal',
                     'PC,TOTAL,T,RO':'Romania',
                     'PC,TOTAL,T,SE':'Sweden',
                     'PC,TOTAL,T,SI':'Slovenia',
                     'PC,TOTAL,T,SK':'Slovakia'})
dfclean = dfclean[['2021']]
dfsorted = dfclean.sort_values(by='2021', ascending=True)


index = dfsorted.index
values = dfsorted['2021']
bar = plt.barh(index, values)
plt.xlabel('Percentage of total population')
plt.suptitle('Risk of poverty or social exclusion in EU countries')
plt.title("Source: Eurostat 2021")
plt.show()
plt.savefig('Riskofpoverty.png')
