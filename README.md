# LLM from Scratch

This project demonstrates how to create a Large Language Model (LLM) from scratch using Python. It includes steps to set up the environment, preprocess data, train the model, and run a chatbot.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Training](#training)
- [Chatbot](#chatbot)
- [License](#license)

## Installation

1. **Create a virtual environment:**

    ```sh
    python -m venv envname
    ```

2. **Activate the virtual environment:**

    - On Windows:
      ```sh
      envname\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source envname/bin/activate
      ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Dataset

We are using the OpenWebText dataset. You can find the dataset on Hugging Face:

[OpenWebText Dataset](https://huggingface.co/datasets/Skylion007/openwebtext)

1. **Save the data locally:**
    Follow the instructions on the Hugging Face page to download and save the dataset to your local machine.

## Preprocessing

1. **Run the preprocessing script:**

    After downloading the dataset, update the dataset path in `preprocessing.py`. 

    ```python
    loaded_dataset = load_from_disk("your/local/dataset/directory")
    ```

2. **Execute the preprocessing script:**

    ```sh
    python preprocessing.py
    ```

    This will generate three output files:
    - `output_train.txt`
    - `output_val.txt`
    - `vocab.txt`

## Training

1. **Run the training script:**

    ```sh
    python training.py
    ```

    Upon completion, this will produce a model file named `model-01.pkl`.

## Chatbot

1. **Run the chatbot script:**

    ```sh
    python chatbot.py -batch_size 32
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests.

Happy coding!
