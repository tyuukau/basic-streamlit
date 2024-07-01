import streamlit as st

from utils import load_vocab, levenshtein_distance

# App Title
st.title("Word Correction using Levenshtein Distance")

# Load vocabulary
vocabs = load_vocab(file_path="data/vocab.txt")

# Input text
word = st.text_input("Word:")

if st.button("Compute"):

    # Compute levenshtein distance
    leven_distances = dict()
    for vocab in vocabs:
        leven_distances[vocab] = levenshtein_distance(word, vocab)

    # Sort by distance
    sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distences.keys())[0]
    st.write("Correct word: ", correct_word)

    col1, col2 = st.columns(2)
    col1.write("Vocabulary:")
    col1.write(vocabs)

    col2.write("Distances:")
    col2.write(sorted_distences)
