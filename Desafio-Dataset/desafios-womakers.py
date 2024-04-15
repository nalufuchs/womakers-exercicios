import pandas as pd
from pydataset import data
df_plants = data('plantTraits')
print(df_plants.head())
df_plants.shape
df_plants.info()
type(df_plants)