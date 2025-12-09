import nltk

# ✅ Cegah error "punkt_tab not found"
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Case folding
    text = text.lower()

    # Hapus tanda baca
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenizing
    tokens = word_tokenize(text)

    # Stopword removal (gunakan stopword bahasa Indonesia)
    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    return " ".join(filtered_tokens)

def preprocess_dataframe(df):
    df["clean_comment"] = df["comment"].apply(preprocess_text)
    return df
