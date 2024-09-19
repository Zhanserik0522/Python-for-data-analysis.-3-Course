import numpy as np
import pandas as pd
from io import StringIO

iris = np.genfromtxt('iris.txt', skip_header=1, delimiter=',', dtype=float)
iris = iris[0:150,[0,1,2,3]]
iris1, iris2, iris3,iris4 = np.split(iris, 4,axis=1)

# 1. Find the max, min, mean and standard deviation for the columns of the iris and store the results in
# the arrays iris_max, iris_min, iris_avg, iris_std, iris_var respectively. The results must be rounded to
# not more than two decimal places.

# 2. Similarly find the max, min, mean and standard deviation for the columns of the iris1 , iris2 and
# iris3 and store the results in the arrays with appropriate names.


def math_operation(arr):
    # Calculate max, min, mean, std, and variance and round to 2 decimal places
    max_val = np.round(arr.max(), 2)
    min_val = np.round(arr.min(), 2)
    mean_val = np.round(arr.mean(), 2)
    std_val = np.round(arr.std(), 2)
    var_val = np.round(arr.var(), 2)  # Using variance function directly
    return max_val, min_val, mean_val, std_val, var_val


iris_max, iris_min, iris_avg, iris_std, iris_var = math_operation(iris)
iris1_max, iris1_min, iris1_avg, iris1_std, iris1_var = math_operation(iris1)
iris2_max, iris2_min, iris2_avg, iris2_std, iris2_var = math_operation(iris2)
iris3_max, iris3_min, iris3_avg, iris3_std, iris3_var = math_operation(iris3)

print(f"iris - Max: {iris_max}, Min: {iris_min}, Avg: {iris_avg}, Std: {iris_std}, Var: {iris_var}")
print(f"iris1 - Max: {iris1_max}, Min: {iris1_min}, Avg: {iris1_avg}, Std: {iris1_std}, Var: {iris1_var}")
print(f"iris2 - Max: {iris2_max}, Min: {iris2_min}, Avg: {iris2_avg}, Std: {iris2_std}, Var: {iris2_var}")
print(f"iris3 - Max: {iris3_max}, Min: {iris3_min}, Avg: {iris3_avg}, Std: {iris3_std}, Var: {iris3_var}")


# 3. Check the minimum value for sepal length, sepal width, petal length and petal width of the three
# species in comparison to the minimum value of sepal length, sepal width, petal length and petal width
# for the data set as a whole and fill the table below with True if the species value is greater than the
# dataset value and False otherwise.


data = """sepal.length,sepal.width,petal.length,petal.width,variety
5.1,3.5,1.4,.2,Setosa
4.9,3,1.4,.2,Setosa
4.7,3.2,1.3,.2,Setosa
4.6,3.1,1.5,.2,Setosa
5,3.6,1.4,.2,Setosa
5.4,3.9,1.7,.4,Setosa
4.6,3.4,1.4,.3,Setosa
5,3.4,1.5,.2,Setosa
4.4,2.9,1.4,.2,Setosa
4.9,3.1,1.5,.1,Setosa
5.4,3.7,1.5,.2,Setosa
4.8,3.4,1.6,.2,Setosa
4.8,3,1.4,.1,Setosa
4.3,3,1.1,.1,Setosa
5.8,4,1.2,.2,Setosa
5.7,4.4,1.5,.4,Setosa
5.4,3.9,1.3,.4,Setosa
5.1,3.5,1.4,.3,Setosa
5.7,3.8,1.7,.3,Setosa
5.1,3.8,1.5,.3,Setosa
5.4,3.4,1.7,.2,Setosa
5.1,3.7,1.5,.4,Setosa
4.6,3.6,1,.2,Setosa
5.1,3.3,1.7,.5,Setosa
4.8,3.4,1.9,.2,Setosa
5,3,1.6,.2,Setosa
5,3.4,1.6,.4,Setosa
5.2,3.5,1.5,.2,Setosa
5.2,3.4,1.4,.2,Setosa
4.7,3.2,1.6,.2,Setosa
4.8,3.1,1.6,.2,Setosa
5.4,3.4,1.5,.4,Setosa
5.2,4.1,1.5,.1,Setosa
5.5,4.2,1.4,.2,Setosa
4.9,3.1,1.5,.2,Setosa
5,3.2,1.2,.2,Setosa
5.5,3.5,1.3,.2,Setosa
4.9,3.6,1.4,.1,Setosa
4.4,3,1.3,.2,Setosa
5.1,3.4,1.5,.2,Setosa
5,3.5,1.3,.3,Setosa
4.5,2.3,1.3,.3,Setosa
4.4,3.2,1.3,.2,Setosa
5,3.5,1.6,.6,Setosa
5.1,3.8,1.9,.4,Setosa
4.8,3,1.4,.3,Setosa
5.1,3.8,1.6,.2,Setosa
4.6,3.2,1.4,.2,Setosa
5.3,3.7,1.5,.2,Setosa
5,3.3,1.4,.2,Setosa
7,3.2,4.7,1.4,Versicolor
6.4,3.2,4.5,1.5,Versicolor
6.9,3.1,4.9,1.5,Versicolor
5.5,2.3,4,1.3,Versicolor
6.5,2.8,4.6,1.5,Versicolor
5.7,2.8,4.5,1.3,Versicolor
6.3,3.3,4.7,1.6,Versicolor
4.9,2.4,3.3,1,Versicolor
6.6,2.9,4.6,1.3,Versicolor
5.2,2.7,3.9,1.4,Versicolor
5,2,3.5,1,Versicolor
5.9,3,4.2,1.5,Versicolor
6,2.2,4,1,Versicolor
6.1,2.9,4.7,1.4,Versicolor
5.6,2.9,3.6,1.3,Versicolor
6.7,3.1,4.4,1.4,Versicolor
5.6,3,4.5,1.5,Versicolor
5.8,2.7,4.1,1,Versicolor
6.2,2.2,4.5,1.5,Versicolor
5.6,2.5,3.9,1.1,Versicolor
5.9,3.2,4.8,1.8,Versicolor
6.1,2.8,4,1.3,Versicolor
6.3,2.5,4.9,1.5,Versicolor
6.1,2.8,4.7,1.2,Versicolor
6.4,2.9,4.3,1.3,Versicolor
6.6,3,4.4,1.4,Versicolor
6.8,2.8,4.8,1.4,Versicolor
6.7,3,5,1.7,Versicolor
6,2.9,4.5,1.5,Versicolor
5.7,2.6,3.5,1,Versicolor
5.5,2.4,3.8,1.1,Versicolor
5.5,2.4,3.7,1,Versicolor
5.8,2.7,3.9,1.2,Versicolor
6,2.7,5.1,1.6,Versicolor
5.4,3,4.5,1.5,Versicolor
6,3.4,4.5,1.6,Versicolor
6.7,3.1,4.7,1.5,Versicolor
6.3,2.3,4.4,1.3,Versicolor
5.6,3,4.1,1.3,Versicolor
5.5,2.5,4,1.3,Versicolor
5.5,2.6,4.4,1.2,Versicolor
6.1,3,4.6,1.4,Versicolor
5.8,2.6,4,1.2,Versicolor
5,2.3,3.3,1,Versicolor
5.6,2.7,4.2,1.3,Versicolor
5.7,3,4.2,1.2,Versicolor
5.7,2.9,4.2,1.3,Versicolor
6.2,2.9,4.3,1.3,Versicolor
5.1,2.5,3,1.1,Versicolor
5.7,2.8,4.1,1.3,Versicolor
6.3,3.3,6,2.5,Virginica
5.8,2.7,5.1,1.9,Virginica
7.1,3,5.9,2.1,Virginica
6.3,2.9,5.6,1.8,Virginica
6.5,3,5.8,2.2,Virginica
7.6,3,6.6,2.1,Virginica
4.9,2.5,4.5,1.7,Virginica
7.3,2.9,6.3,1.8,Virginica
6.7,2.5,5.8,1.8,Virginica
7.2,3.6,6.1,2.5,Virginica
6.5,3.2,5.1,2,Virginica
6.4,2.7,5.3,1.9,Virginica
6.8,3,5.5,2.1,Virginica
5.7,2.5,5,2,Virginica
5.8,2.8,5.1,2.4,Virginica
6.4,3.2,5.3,2.3,Virginica
6.5,3,5.5,1.8,Virginica
7.7,3.8,6.7,2.2,Virginica
7.7,2.6,6.9,2.3,Virginica
6,2.2,5,1.5,Virginica
6.9,3.2,5.7,2.3,Virginica
5.6,2.8,4.9,2,Virginica
7.7,2.8,6.7,2,Virginica
6.3,2.7,4.9,1.8,Virginica
6.7,3.3,5.7,2.1,Virginica
7.2,3.2,6,1.8,Virginica
6.2,2.8,4.8,1.8,Virginica
6.1,3,4.9,1.8,Virginica
6.4,2.8,5.6,2.1,Virginica
7.2,3,5.8,1.6,Virginica
7.4,2.8,6.1,1.9,Virginica
7.9,3.8,6.4,2,Virginica
6.4,2.8,5.6,2.2,Virginica
6.3,2.8,5.1,1.5,Virginica
6.1,2.6,5.6,1.4,Virginica
7.7,3,6.1,2.3,Virginica
6.3,3.4,5.6,2.4,Virginica
6.4,3.1,5.5,1.8,Virginica
6,3,4.8,1.8,Virginica
6.9,3.1,5.4,2.1,Virginica
6.7,3.1,5.6,2.4,Virginica
6.9,3.1,5.1,2.3,Virginica
5.8,2.7,5.1,1.9,Virginica
6.8,3.2,5.9,2.3,Virginica
6.7,3.3,5.7,2.5,Virginica
6.7,3,5.2,2.3,Virginica
6.3,2.5,5,1.9,Virginica
6.5,3,5.2,2,Virginica
6.2,3.4,5.4,2.3,Virginica
5.9,3,5.1,1.8,Virginica
"""

df = pd.read_csv(StringIO(data))

def min_values(df):
    return {
        'sepal_length': df['sepal.length'].min(),
        'sepal_width': df['sepal.width'].min(),
        'petal_length': df['petal.length'].min(),
        'petal_width': df['petal.width'].min()
    }

min_dataset = min_values(df)
min_setosa = min_values(df[df['variety'] == 'Setosa'])
min_versicolor = min_values(df[df['variety'] == 'Versicolor'])
min_virginica = min_values(df[df['variety'] == 'Virginica'])

comparison = {
    'Setosa': {key: min_setosa[key] > min_dataset[key] for key in min_setosa},
    'Versicolor': {key: min_versicolor[key] > min_dataset[key] for key in min_versicolor},
    'Virginica': {key: min_virginica[key] > min_dataset[key] for key in min_virginica}
}

print(comparison)
