import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

data = pd.read_csv('data/GlobalLandTemperaturesByCountry.csv', encoding = "latin1").dropna(how='any')
# data.head(10)

data['AverageTemperature'] = pd.to_numeric(data['AverageTemperature'])
data['dt'] = pd.to_datetime(data['dt'])
df = data.copy()

# time_check = pd.Timestamp(1949, 12, 1)
# time_filter = df['dt'] >= time_check
# df = df[time_filter]

# df = df.groupby(df['dt'].dt.year).agg(['sum', 'mean'])
# df.reset_index()
# # Deleting 0 values
# df = df[df['AverageTemperature']['sum'] != 0]

#Grafica de correlacion
# plot_acf(df['AverageTemperature'])
# plt.show()

arima_model = ARIMA(df['AverageTemperature'], order=(1,1,1))
model = arima_model.fit()
print(model.summary())