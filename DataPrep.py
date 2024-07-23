import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn import metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# Import Data
df = pd.read_csv("/Users/kharitetteh/Desktop/Coding/F1 Data Analysis/F1DriversDataset.csv")
print(df.head())
print(df.columns)

### What is the distribution of drivers' nationalities in the dataset?
# Driver nationalities
nationality_drivers = df['Nationality'].value_counts().sort_values(ascending=False).head(20)
print(nationality_drivers)

# Define the generate_chart function
def generate_chart(names, values):
    df = pd.DataFrame({'names': names, 'values': values})
    fig = px.pie(df, values=values, names=names, color_discrete_sequence=px.colors.sequential.RdBu)
    return fig

# Generate and display pie chart
fig = generate_chart(nationality_drivers.index, nationality_drivers.values)
fig.show()

### What is the correlation between the number of seasons a driver participates in and their number of race wins?
# Correlation between number of seasons and number of race wins 
df_winsvsyears = df[['Years_Active', 'Race_Wins']]
print(df_winsvsyears.head())

# Check for missing data
print(df_winsvsyears.isnull().sum())

# Convert to Numpy Array and Reshape
X = df_winsvsyears['Years_Active'].to_numpy().reshape(-1, 1)
y = df_winsvsyears['Race_Wins'].to_numpy().reshape(-1, 1).ravel()

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and Training the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=200, max_depth=None)

# Fitting the Model
rf_regressor.fit(X_train, y_train)

# Making predictions 
y_pred = rf_regressor.predict(X_test)

# Correlation Coefficient Calculation
corr_coef = df['Years_Active'].corr(df['Race_Wins'])

# Mean Squared Error Calculation 
mse = mean_squared_error(y_test, y_pred)

# Results
print("Mean Squared Error: ", mse)
print("Correlation Coefficient:", corr_coef)

### Pole positions vs Race wins of champions
# Find the number of champions 
df_champions = df.query('Championships > 0')
df_champions.head()

# Linear Regression model 
def linear_regression(df, predictor, target):   
    # Fit a linear regression model to the data
    X = df[predictor].values.reshape(-1, 1)
    y = df[target].values.reshape(-1, 1)
    
    regressor = LinearRegression()
    regressor.fit(X, y)
    
    # Calculate the R-squared value of the linear regression model
    r_squared = regressor.score(X, y)
    
    # Calculate the correlation coefficient 
    corr_coef = df[predictor].corr(df[target])
    
    # Predict the target variable using the predictor variable
    y_pred = regressor.predict(X)
    
    # Calculate the prediction score
    prediction_score = mean_squared_error(y, y_pred)
    
    # Create a scatter plot to visualize the relationship between the predictor and target
    plt.figure(figsize=(10, 6))
    sns.regplot(x=predictor, y=target, data=df)
    
    # Plot the regression line on top of the scatter plot
    plt.plot(df[predictor], regressor.predict(df[[predictor]]), color='red')
    plt.title('Race Wins vs Pole Positions')
    
    return corr_coef, r_squared, y_pred, prediction_score, plt

# Calls Linear Regression function
corr_coef, r_squared, y_pred, prediction_score, plt = linear_regression(df_champions, 'Pole_Positions', 'Race_Wins')
plt.show()
plt.close()  # Close the figure to avoid overlap with future plots
print('Prediction Score:', prediction_score)
print('Correlation Coefficient:', corr_coef)
print('R-squared:', r_squared)

### What does it take to become a Champion?

# Filter to include only numeric columns
numeric_df = df.select_dtypes(include=[float, int])

# Calculate and print the correlation matrix
print(numeric_df.corr())

# Correlation Matrix Heatmap
plt.figure(figsize=(12, 12))
dataplot = sns.heatmap(numeric_df.corr(), cmap="YlGnBu", annot=True, fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()  # Display the correlation matrix heatmap
plt.close()  # Close the figure to avoid overlap with future plots

# Scatter Plots - Linear Regression (Degree 1)
columns = ['Pole_Rate', 'Start_Rate', 'Win_Rate', 'Podium_Rate', 'FastLap_Rate', 'Years_Active']
plt.figure(figsize=(20, 15))
i = 0
for col in columns:
    i += 1
    plt.subplot(2, 3, i)
    sns.regplot(x=col, y='Championships', data=df, order=1)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the scatter plots with linear regression
plt.close()  # Close the figure to avoid overlap with future plots

# Scatter Plots - Quadratic Regression (Degree 2)
plt.figure(figsize=(20, 15))
i = 0
for col in columns:
    i += 1
    plt.subplot(2, 3, i)
    sns.regplot(x=col, y='Championships', data=df, order=2)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the scatter plots with quadratic regression
plt.close()  # Close the figure to avoid overlap with future plots

# Extract Target & Features
target = df['Champion']
features = df[['Race_Entries', 'Race_Starts', 'Pole_Positions', 'Race_Wins', 'Podiums', 'Fastest_Laps', 'Points']]

# Convert to NumPy Arrays
X = features.values
Y = target.values

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialise and train the model
clf = SGDClassifier(random_state=42)
model = clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Model evaluation
accuracy = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred, average="macro")
print("Accuracy:", accuracy)
print("Precision:", precision)

# Confusion Matrix
matrix = confusion_matrix(y_test, y_pred)
print(matrix)

# Create a new figure for the confusion matrix heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(matrix, annot=True, cmap='Reds', fmt='g')  # 'fmt="g"' for integer annotations
plt.title('Confusion Matrix')
plt.show()  # Display the confusion matrix heatmap
plt.close()  # Close the figure to avoid overlap with future plots

# Optionally, display the confusion matrix using ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap=plt.cm.Blues, normalize='true')
plt.show()  # Ensure the ConfusionMatrixDisplay plot is shown
plt.close()  # Close the figure to avoid overlap
