import pandas
df= pandas.read_csv(
		'data.csv',
		encoding='Shift_JIS',
)
df_sliced=df.iloc[1:4]
series_temp =df['temp']

mean_temp=series_temp.mean()

series_filled=series_temp.fillna(mean_temp)
df['temp']=series_filled
print(df)
		
