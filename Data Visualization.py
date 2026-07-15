import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Top 10 Countries
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.show()
# Movies vs TV Shows Pie Chart

type_counts = df['type'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(type_counts,
        labels=type_counts.index,
        autopct='%1.1f%%')

plt.title("Movies vs TV Shows on Netflix")

plt.show()
# Top 10 Release Years

top_years = df['release_year'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_years.plot(kind='bar')

plt.title("Top 10 Release Years on Netflix")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()

# Top 10 Genres

top_genres = df['listed_in'].value_counts().head(10)

plt.figure(figsize=(12,6))
top_genres.plot(kind='bar')

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()