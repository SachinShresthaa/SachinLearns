import os
import pandas as pd
from sklearn.linear_model import LinearRegression

csv_path = os.path.join(os.path.dirname(__file__), "scores.csv")
data = pd.read_csv(csv_path)

X = data[['Hours']]
y = data['Scores']

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(pd.DataFrame({'Hours': [11]}))

print("Predicted score for 11 hours:", prediction[0])