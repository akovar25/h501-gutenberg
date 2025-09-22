# utils.py

import pandas as pd

# URLs for TidyTuesday Gutenberg dataset (2025-06-03)
AUTHORS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
LANGUAGES_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
METADATA_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
SUBJECTS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv"

def load_gutenberg_data():
    """Load all four Gutenberg datasets from TidyTuesday GitHub."""
    authors = pd.read_csv(AUTHORS_URL)
    languages = pd.read_csv(LANGUAGES_URL)
    metadata = pd.read_csv(METADATA_URL)
    subjects = pd.read_csv(SUBJECTS_URL)
    return authors, languages, metadata, subjects

def clean_authors(df):
    """Filter out rows with missing or non-string aliases."""
    return df[df["alias"].notnull() & df["alias"].apply(lambda x: isinstance(x, str))]