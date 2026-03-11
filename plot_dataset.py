import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'Music Dataset Lyrics and Metadata from 1950 to 2019\tcc_ceds_music.csv') 

df['year'] = pd.to_numeric(df['release_date'].astype(str).str[:4], errors='coerce')
df = df.dropna(subset=['year', 'loudness', 'lyrics'])
df['year'] = df['year'].astype(int)

df['artist_name'] = df['artist_name'].astype(str).str.lower().str.strip()
df['track_name'] = df['track_name'].astype(str).str.lower().str.strip()
df = df.drop_duplicates(subset=['artist_name', 'track_name'], keep='first')

df['word_count'] = df['lyrics'].astype(str).str.split().str.len()
df = df[(df['word_count'] >= 15) & (df['word_count'] <= 2000)]
df = df[(df['year'] >= 1960) & (df['year'] <= 2019)]

yearly_avg = df.groupby('year').agg({
    'loudness': 'mean',
    'word_count': 'mean',
    'sadness': 'mean',
    'obscene': 'mean'
}).reset_index()

yearly_avg['loudness_smooth'] = yearly_avg['loudness'].rolling(window=3, min_periods=1).mean()
yearly_avg['word_count_smooth'] = yearly_avg['word_count'].rolling(window=3, min_periods=1).mean()

sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 5))
plt.plot(yearly_avg['year'], yearly_avg['loudness_smooth'], color='red', linewidth=3)
plt.fill_between(yearly_avg['year'], yearly_avg['loudness_smooth'], color='red', alpha=0.1)
plt.title('Evolution of Audio Loudness (1960-2019)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Loudness (dB)', fontsize=12)
plt.tight_layout()
plt.savefig('trend_loudness.png')
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(yearly_avg['year'], yearly_avg['word_count_smooth'], color='blue', linewidth=3)
plt.fill_between(yearly_avg['year'], yearly_avg['word_count_smooth'], color='blue', alpha=0.1)
plt.title('Average Word Count Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Number of Words', fontsize=12)
plt.tight_layout()
plt.savefig('trend_length.png')
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(yearly_avg['year'], yearly_avg['sadness'].rolling(3).mean(), color='purple', linewidth=2, label='Sadness')
plt.plot(yearly_avg['year'], yearly_avg['obscene'].rolling(3).mean(), color='orange', linewidth=2, label='Obscene')
plt.title('Lyrical Topic Intensity (1960 - 2019)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Topic Intensity', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('trend_topics.png')
plt.show()
