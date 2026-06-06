import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = pd.read_csv("match_data.csv")

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

# Remove rows that are completely empty
df = df.dropna(how="all")

documents = []

for _, row in df.iterrows():

    values = [str(v) for v in row.values if pd.notna(v)]

    text = " | ".join(values)

    if len(text.strip()) > 10:
        documents.append(text)

print(f"\nDocuments Created: {len(documents)}")

if len(documents) == 0:
    print("No valid records found in match_data.csv")
    exit()

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

while True:

    query = input("\nEnter your query (or type exit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = np.argsort(similarities)[-3:][::-1]

    print("\nTop Matches:\n")

    for idx in top_indices:
        print(documents[idx])
        print("-" * 60)