import pandas as pd

def load_data():
    """
    Function that loads all the variations of the Gutenberg data from the GitHub repository.
    
    Arguments:
    None

    Returns:
    A three different DataFrames containing authors, metadata, language data.
    """
    
    # Load Author data from GitHub repository
    
    authors = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    )
    # Load Metadata data from GitHub repository

    metadata = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )
    
    # Load Language data from GitHub repository

    languages = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    )
    return authors, metadata, languages

def count_translations_by_author(authors, metadata, languages, alias=True):
    """
    Function to count the number of translations per author.

    Arguments:
    authors: dataframe
    metadata: dataframe
    languages: dataframe
    
    Parameters:
    alias: bool -> use author alias column if True, else use author name

    Returns:
    A DataFrame that displays the author and translation count.
    """
    # Merge metadata and languages dataframes
    meta_lang = metadata.merge(languages, on="gutenberg_id", how="left")

    # Count number of unique languages per book
    lang_counts = (
        meta_lang.groupby("gutenberg_id")["language_y"]
        .nunique()
        .reset_index(name="num_languages")
    )

    # Attach to authors
    merged = metadata.merge(authors, left_on="gutenberg_author_id", right_on="gutenberg_author_id", how="left") \
                 .merge(lang_counts, on="gutenberg_id", how="left")

    # Translations = languages - 1 (ignore original)
    merged["translations"] = merged["num_languages"].fillna(1) - 1

    group_col = "alias" if alias else "name"
    out = (
        merged.groupby(group_col)["translations"]
        .sum()
        .reset_index()
        .sort_values("translations", ascending=False)
    )

    return out