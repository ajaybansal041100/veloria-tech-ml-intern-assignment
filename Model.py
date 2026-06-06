import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# Load data
df = pd.read_csv("match_data.csv")

print("Original Data Shape:", df.shape)

# Remove empty rows
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only useful columns
df = df[["Series", "Match", "Venue", "Winner"]]

# Encode categorical columns
encoders = {}

for col in ["Series", "Match", "Venue", "Winner"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Features and target
X = df[["Series", "Match", "Venue"]]
y = df["Winner"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")
cm = confusion_matrix(y_test, y_pred)

print("\n===== RESULTS =====")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("F1 Score:", round(f1, 4))

print("\nConfusion Matrix:")
print(cm)