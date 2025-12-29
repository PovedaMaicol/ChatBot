from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar dataset
dataset = load_dataset("DeepPavlov/snips")

train_df = dataset["train"].to_pandas()
test_df = dataset["test"].to_pandas()

# Separar texto y etiquetas
X_train_text = train_df["utterance"]
y_train = train_df["label"]

X_test_text = test_df["utterance"]
y_test = test_df["label"]

# Crear vectorizador TF-IDF
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000 #las 5000 palabras más importantes
)

# Aprender vocabulario y vectorizar con fit_transform
# nunca se usa fit_transform en test
X_train = vectorizer.fit_transform(X_train_text)

# Usar el mismo vocabulario para test, con transform solo vectoriza
X_test = vectorizer.transform(X_test_text)

print("Dimensión de X_train:", X_train.shape)
print("Dimensión de X_test:", X_test.shape)
