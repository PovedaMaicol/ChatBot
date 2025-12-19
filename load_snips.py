from datasets import load_dataset

# Load the SNIPS dataset
dataset = load_dataset("DeepPavlov/snips")
print(dataset)

# Convert to pandas DataFrame
train_df = dataset["train"].to_pandas()
test_df = dataset["test"].to_pandas()


print("First 5 rows of the training set:")
print(train_df.head())

print("\nInformación general:")
print(train_df.info())

print("\nEjemplo de etiquetas únicas:")
print(train_df["label"].unique())