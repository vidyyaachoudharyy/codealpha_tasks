import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Dataset Information
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# Movies vs TV Shows
print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.show()

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Top Countries
print("\nTop 10 Countries:")
top_countries = df['country'].value_counts().head(10)
print(top_countries)

top_countries.plot(kind='bar')
plt.title("Top 10 Countries on Netflix")
plt.show()

# Top Release Years
print("\nTop Release Years:")
top_years = df['release_year'].value_counts().head(10)
print(top_years)

top_years.plot(kind='bar')
plt.title("Top Release Years on Netflix")
plt.show()

# Top Genres
print("\nTop Genres:")
top_genres = df['listed_in'].value_counts().head(10)
print(top_genres)

top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.show()


