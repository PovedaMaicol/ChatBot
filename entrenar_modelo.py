from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# la regresión logistica es un modelo lineal para clasificación, predice la probabilidad de un resultado (SI/NO)
#funciona bien para texto 

# CONCEPTO CLAVE:
'''Variable Dependiente (Y): La variable que se quiere predecir (ej: gasto futuro).
Variable Independiente (X): La variable conocida que se usa para predecir (ej: ingreso futuro).'''

# 1. Load dataset
dataset = load_dataset("DeepPavlov/snips")

#  Convert to pandas DataFrame
train_df = dataset["train"].to_pandas()
test_df = dataset["test"].to_pandas()

#  Separate text and labels
x_train_text = train_df["utterance"]
y_train = train_df["label"]

x_test_text = test_df["utterance"]
y_test = test_df["label"]

# 2. Vectorization 
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000 # top 5000 important words
)

X_train = vectorizer.fit_transform(x_train_text)
X_test = vectorizer.transform(x_test_text)

# 3 Model
model = LogisticRegression(max_iter=1000)

# 4. Training
model.fit(X_train, y_train)

# 5. Evaluation
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6. Guardar modelo y vectorizador
# joblib.dump(model, "modelo_intenciones.pkl")
# joblib.dump(vectorizer, "vectorizer.pkl")