import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the diamonds dataset
diamonds = sns.load_dataset('diamonds')
print(diamonds.head())

# Basic Plots
# Scatter Plot
sns.scatterplot(x='carat', y='price', data=diamonds)
plt.title('Scatter Plot of Carat vs Price')
plt.show()

sns.scatterplot(x='carat', y='depth', data=diamonds)
plt.title('Scatter Plot of Carat vs Depth')
plt.show()

sns.scatterplot(x='price', y='depth', data=diamonds)
plt.title('Scatter Plot of Price vs Depth')
plt.show()

# Line Plot
sns.lineplot(x='carat', y='price', data=diamonds)
plt.title('Line Plot of Price vs Carat')
plt.show()

sns.lineplot(x='carat', y='price', hue='cut', data=diamonds)
plt.title('Line Plot of Price vs Carat by Cut')
plt.show()

sns.lineplot(x='carat', y='price', hue='color', style='clarity', data=diamonds)
plt.title('Line Plot of Price vs Carat by Color and Clarity')
plt.show()

# Categorical plots
# Bar Plot
sns.barplot(x='cut', y='price', data=diamonds)
plt.title('Bar Plot of Price by Cut')
plt.show()

sns.barplot(x='color', y='price', hue='cut', data=diamonds)
plt.title('Bar Plot of Price by Color and Cut')
plt.show()

sns.barplot(x='clarity', y='price', hue='cut', data=diamonds)
plt.title('Bar Plot of Price by Clarity and Cut')
plt.show()

# Box Plot
sns.boxplot(x='cut', y='price', data=diamonds)
plt.title('Box Plot of Price by Cut')
plt.show()

sns.boxplot(x='color', y='price', data=diamonds)
plt.title('Box Plot of Price by Color')
plt.show()

sns.boxplot(x='clarity', y='price', hue='cut', data=diamonds)
plt.title('Box Plot of Price by Clarity and Cut')
plt.show()

# Violin Plot
sns.violinplot(x='cut', y='price', data=diamonds)
plt.title('Violin Plot of Price by Cut')
plt.show()

sns.violinplot(x='color', y='price', hue='cut', data=diamonds, split=True)
plt.title('Violin Plot of Price by Color and Cut')
plt.show()

sns.violinplot(x='clarity', y='price', hue='cut', data=diamonds, split=True)
plt.title('Violin Plot of Price by Clarity and Cut')
plt.show()

# Distribution Plots
# Histogram
sns.histplot(diamonds['price'], bins=20, kde=True)
plt.title('Histogram of Price')
plt.show()

sns.histplot(diamonds['carat'], bins=15, kde=True)
plt.title('Histogram of Carat')
plt.show()

sns.histplot(diamonds['depth'], bins=10, kde=True)
plt.title('Histogram of Depth')
plt.show()

# Kernel Density Estimate (KDE) Plot
sns.kdeplot(diamonds['price'], shade=True)
plt.title('KDE Plot of Price')
plt.show()

sns.kdeplot(diamonds['carat'], shade=True)
plt.title('KDE Plot of Carat')
plt.show()

sns.kdeplot(diamonds['depth'], shade=True)
plt.title('KDE Plot of Depth')
plt.show()

# Matrix Plots
# Heatmap
diamonds_corr = diamonds.corr()
sns.heatmap(diamonds_corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap of Diamonds Correlation Matrix')
plt.show()

# Pair Plot
sns.pairplot(diamonds)
plt.title('Pair Plot of Diamonds Dataset')
plt.show()

sns.pairplot(diamonds, hue='cut')
plt.title('Pair Plot of Diamonds Dataset by Cut')
plt.show()

sns.pairplot(diamonds, hue='color')
plt.title('Pair Plot of Diamonds Dataset by Color')
plt.show()

# FacetGrid
g = sns.FacetGrid(diamonds, col='cut', hue='color')
g.map(sns.scatterplot, 'carat', 'price')
g.add_legend()
plt.show()

g = sns.FacetGrid(diamonds, row='clarity', col='cut')
g.map(sns.histplot, 'price')
plt.show()

g = sns.FacetGrid(diamonds, col='color', hue='cut')
g.map(sns.boxplot, 'clarity', 'price')
g.add_legend()
plt.show()
