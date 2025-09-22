# authors.py

from tt_gutenberg.utils import load_gutenberg_data, clean_authors

def list_authors(by_languages=True, alias=True):
    """
    Return a list of author aliases sorted by translation count.
    Only includes valid aliases.
    """
    authors, languages, metadata, subjects = load_gutenberg_data()
    authors = clean_authors(authors)

    if by_languages and alias:
        # Merge authors with languages on gutenberg_author_id
        merged = authors.merge(languages, on="gutenberg_author_id", how="inner")

        # Count number of translations per alias
        translation_counts = merged.groupby("alias")["language"].count()

        # Sort descending and return list of aliases
        return translation_counts.sort_values(ascending=False).index.tolist()

    return []