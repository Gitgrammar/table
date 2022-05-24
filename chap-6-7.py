import pandas
from matplotlib import pyplot
df= pandas.read_csv(
		'data.csv',
		encoding='Shift_JIS'
)
df_stations= pandas.read_csv(
		'amedas_stations.csv',
		encoding='Shift_JIS',index_col=0
)
df=df.join(
		df_stations,
		on='station'
)

print(df[
				(df['station'].isin(['東京','札幌'])) & 
        (df['temp']<20)
			]
		)
print((df.plot.scatter('latitude','temp')))
print((df.plot.scatter('temp','latitude')))

df_sliced=df.iloc[1:4]
series_temp =df['temp']

mean_temp=series_temp.mean()

series_filled=series_temp.fillna(mean_temp)
		
