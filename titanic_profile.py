import pandas as pd
import pandas_profiling as pdp
df = pd.read_csv('titanic.csv')
pdp.ProfileReport(df)