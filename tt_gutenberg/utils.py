import pandas as pd
from .data import load_authors, load_languages, load_metadata

def count_translations_by_author():
    authors = load_authors()
    languages = load_languages()
    metadata = load_metadata()

    # Merge metadata -> languages (by gutenberg_id)
    merged = metadata.merge(languages, on="gutenberg_id", how="inner")

    # Count distinct languages per author_id
    lang_counts = (
        merged.groupby("author_id")["language"]
        .nunique()
        .reset_index(name="translation_count")
    )

    # Merge back to authors
    authors_counts = authors.merge(lang_counts, on="author_id", how="inner")

    return authors_counts