
import os
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_core.tools import tool


QUERY_FOLDER = r"C:\Users\Karan PC\LangGraph\AgenticRequestRetriever_fine _donechanges_withGraph_Text_JSON_FastSearching_P - Copy\data"

SUPPORTED_EXTENSIONS = (".txt", ".sql", ".json")


# Load files and create TF-IDF index only once
@st.cache_resource(show_spinner="Loading request files...")
def load_search_index(folder):

    files = []
    documents = []

    if not os.path.isdir(folder):
        return None

    for root, _, filenames in os.walk(folder):

        for filename in filenames:

            if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
                continue

            file_path = os.path.join(root, filename)

            try:
                with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
                    content = f.read()

                if content.strip():

                    files.append({
                        "file_name": filename,
                        "file_path": file_path,
                        "file_content": content
                    })

                    documents.append(
                        filename.replace("_", " ") + " " + content
                    )

            except OSError:
                continue

    if not files:
        return None

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    document_vectors = vectorizer.fit_transform(documents)

    return files, vectorizer, document_vectors


# Search tool
@tool
def search_query_files(query: str) -> dict:
    """
    Search TXT, SQL and JSON files using cached TF-IDF index.
    Returns top 5 matching files.
    """

    index = load_search_index(QUERY_FOLDER)

    if index is None:
        return {
            "error": "No readable TXT, SQL or JSON files found.",
            "results": []
        }

    files, vectorizer, document_vectors = index

    try:

        query_vector = vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            document_vectors
        ).flatten()

        top_indices = scores.argsort()[::-1][:5]

        results = [
            {
                **files[i],
                "similarity_score": round(float(scores[i]), 4)
            }
            for i in top_indices
            if scores[i] > 0
        ]

        if not results:
            return {
                "error": "No matching files found.",
                "results": []
            }

        return {
            "error": None,
            "total_files_searched": len(files),
            "results": results
        }

    except ValueError as e:

        return {
            "error": str(e),
            "results": []
        }


# Clear cached index when request files are updated
def refresh_search_index():
    load_search_index.clear()

