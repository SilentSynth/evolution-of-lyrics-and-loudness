<h1 align="center">Evolution of Lyrics and Loudness (1960–2019)</h1>

<p align="center">
  An exploratory data analysis of musical evolution from 1960 to 2019 using a dataset of 28,000+ songs.
</p>


An exploratory data analysis of musical evolution from 1960 to 2019 using a dataset with more than 28k songs. This project investigates the Loudness War, shifts in lyrical density (word count), and the longitudinal progression of thematic sentiments like sadness and obscenity.

Data Source
The dataset used in this project is the Music Dataset: Lyrics and Metadata from 1950 to 2019.

Due to file size constraints, the raw CSV file is not hosted in this repository. To run the analysis, download the dataset from Mendeley Data and place it in the project root directory.

Source: Mendeley Data - Music Dataset

Citation: Moura, L., Fontelles, E., Sampaio, V., & França, M. (2020). Music Dataset: Lyrics and Metadata from 1950 to 2019. Mendeley Data, V3.

Technical Implementation
The analysis is performed using Python and the following libraries:

Pandas: Data manipulation, cleaning, and time-series aggregation.

Matplotlib/Seaborn: Data visualization and trend identification.

Processing Pipeline
Data Cleaning: Standardization of artist and track naming conventions to ensure accurate deduplication.

Feature Engineering: Calculation of word counts from raw lyrics and the extraction of release years.

Trend Smoothing: Implementation of 3-year rolling averages to reduce annual volatility and highlight macro-level trends.

Filtering: Focused analysis on the period between 1960 and 2019, removing instrumental tracks and statistical outliers.

Analysis and Visualizations

1. The Loudness War

<img width="1200" height="500" alt="image" src="https://github.com/user-attachments/assets/d09b1319-8732-431f-8895-976c7cb6a8ab" />
This visualization tracks the average decibel levels of music over time, illustrating the industry-wide trend of increasing audio compression and volume.

2. Lyrical Density

<img width="1200" height="500" alt="image" src="https://github.com/user-attachments/assets/f01e1274-074e-444d-ae3b-16d98aa1102b" />
An analysis of the average number of words per song, showing how the complexity and length of lyrics have shifted across different eras of music.

3. Thematic Shifts

<img width="1200" height="500" alt="image" src="https://github.com/user-attachments/assets/05b71913-2170-4c2e-ad63-40c19a0bf556" />
A comparison of sentiment intensities, specifically tracking the prevalence of "Sadness" and "Obscene" topics in lyrics across the 60-year period.

Installation and Usage
Clone the repository:

Bash
git clone https://github.com/your-username/evolution-of-lyrics-and-loudness.git
Install dependencies:

Bash
pip install pandas matplotlib seaborn
Place tcc_ceds_music.csv in the project folder.

Run the analysis script:

Bash
python analysis_script.py
