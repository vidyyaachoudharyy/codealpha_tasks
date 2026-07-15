import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("IMDB Dataset.csv")

# First 5 rows
print(df.head())

# Dataset Information
print("\nDataset Shape:", df.shape)

# Sentiment Counts
sentiment_counts = df['sentiment'].value_counts()

print("\nSentiment Distribution:")
print(sentiment_counts)

# Bar Chart
plt.figure(figsize=(6,4))
sentiment_counts.plot(kind='bar')

plt.title("Positive vs Negative Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
sentiment_counts.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sentiment Distribution")
plt.ylabel("")

plt.show()

# Review Length Analysis

df['review_length'] = df['review'].apply(len)

avg_length = df.groupby('sentiment')['review_length'].mean()

print("\nAverage Review Length:")
print(avg_length)

plt.figure(figsize=(6,4))
avg_length.plot(kind='bar')

plt.title("Average Review Length by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average Length")

plt.show()