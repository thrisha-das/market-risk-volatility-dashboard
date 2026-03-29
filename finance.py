import pandas as pd

df = pd.read_csv("finance_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.head()
df['Return'] = df.groupby('Stock')['Price'].pct_change()
print(df)
volatility = df.groupby('Stock')['Return'].std()
print(volatility)
import numpy as np

var_95 = df['Return'].quantile(0.05)
print("Value at Risk (95%):", var_95)
import numpy as np

price = 180
simulations = 1000
days = 30

results = []

for i in range(simulations):
    prices = [price]
    for j in range(days):
        change = np.random.normal(0, 0.02)
        prices.append(prices[-1] * (1 + change))
    results.append(prices)

print("Simulation done")
import matplotlib.pyplot as plt

for sim in results[:50]:
    plt.plot(sim)

plt.title("Monte Carlo Simulation")
plt.show()
df.to_csv("finance_output.csv", index=False)