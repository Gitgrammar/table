import pandas
df= pandas.read_csv(
		'data.csv',
		encoding='Shift_JIS',
)
df_sliced=df.iloc[1:4]
print(df_sliced)
		
