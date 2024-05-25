from datasets import load_from_disk, Dataset
from sklearn.model_selection import train_test_split
import tqdm

# Load the dataset from the saved directory
loaded_dataset = load_from_disk("D:\\myllm\\fcc-gpt-course\\data")

# Split the dataset into training and validation sets (90% training, 10% validation)
train_indices, val_indices = train_test_split(range(len(loaded_dataset['train'])), test_size=0.1, random_state=42)
train_dataset = loaded_dataset['train'].select(train_indices)
val_dataset = loaded_dataset['train'].select(val_indices)

# File paths
output_file_train = "output_train.txt"
output_file_val = "output_val.txt"
vocab_file = "vocab.txt"

# Function to write dataset to a file and collect vocabulary in batches
def write_data_and_collect_vocab(dataset, output_file, batch_size=1000):
    vocab = set()
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in tqdm.tqdm(range(0, len(dataset), batch_size), desc=f"Writing {output_file}"):
            batch = dataset.select(range(i, min(i + batch_size, len(dataset))))
            for example in batch:
                text = example['text']
                f.write(text + '\n')
                vocab.update(text)
    return vocab

# Write training and validation data to their respective files
vocab_train = write_data_and_collect_vocab(train_dataset, output_file_train)
vocab_val = write_data_and_collect_vocab(val_dataset, output_file_val)

# Combine vocabularies from training and validation sets
vocab = vocab_train.union(vocab_val)

# Write the vocabulary to vocab.txt
with open(vocab_file, 'w', encoding='utf-8') as f:
    for char in sorted(vocab):
        f.write(char + '\n')

print("Data processing completed.")
