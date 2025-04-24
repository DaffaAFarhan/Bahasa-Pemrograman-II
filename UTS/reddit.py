# install dulu pip install scikit-learn

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Simulasi data subreddit
data = {
    'subreddit': ['r/learnpython', 'r/machinelearning', 'r/technology', 'r/anime', 'r/gaming'],
    'description': [
        'A place for learning Python',
        'Discussions and news about machine learning',
        'Subreddit about current and future technology',
        'Subreddit for anime lovers',
        'Everything related to gaming'
    ]
}

df = pd.DataFrame(data)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Input user
print("Contoh: AI and technology, Python, anime, gaming, dll.")
user_input = input("Masukkan topik yang kamu suka: ")

if not user_input.strip():
    print("Silakan masukkan topik yang relevan.")
    exit()

# Vectorisasi input user
user_tfidf = vectorizer.transform([user_input])

# Hitung similarity
similarity = cosine_similarity(user_tfidf, tfidf_matrix)

# Ambil hasil teratas
df['similarity'] = similarity[0]
top_result = df.sort_values(by='similarity', ascending=False)
top_result['similarity'] = top_result['similarity'].round(3)

# Tampilkan rekomendasi
print("\nRekomendasi subreddit berdasarkan minat kamu:")
print(top_result[['subreddit', 'similarity']].head())
