import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

df = pd.read_csv(r"C:\Users\ferna\OneDrive - Universidad Politécnica de Madrid\IIT\Machine Learning\Project\ProjectCSV\scaled_df_eur.csv", index_col=0)

X = df["eur_deaths"]
y = df["Price"]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train, y_train = X[:144], y[:144]
X_test, y_test = X[144:], y[144:]

X_train, X_test, y_train, y_test = X_train.to_numpy(), X_test.to_numpy(), y_train.to_numpy(), y_test.to_numpy(),

#%%
regression = linear_model.LinearRegression()
#%%
X_train_reshaped = X_train.reshape(X_train.shape[0],1)
X_test_reshaped = X_test.reshape(X_test.shape[0],1)
y_train_reshaped = y_train.reshape(y_train.shape[0],1)
y_test_reshaped = y_test.reshape(y_test.shape[0],1)

regression.fit(X_train_reshaped, y_train_reshaped)
   #%%
prediction = regression.predict(X_test_reshaped)
#%%
print("Coefficients: \n", regression.coef_)

print("The mean squared error: %.2f" %mean_squared_error(y_test, prediction))

print("Coefficient of determination: %.2f" %r2_score(y_test, prediction))
#%%

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, prediction, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

#%%
# Building a model with cross validation
X_arr, y_arr = X.to_numpy(), y.to_numpy()
X_arr_reshaped = X_arr.reshape(X_arr.shape[0],1)
y_arr_reshaped = y_arr.reshape(y_arr.shape[0],1)

cv = KFold(n_splits=5, random_state=1, shuffle=True)

model = linear_model.LinearRegression()

scores = cross_val_score(model, X_arr_reshaped, y_arr_reshaped, scoring="r2", cv=cv, n_jobs=-1)

mean_score = scores.mean()
print(mean_score)




































