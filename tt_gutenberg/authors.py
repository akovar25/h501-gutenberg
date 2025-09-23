from .utils import count_translations_by_author

def list_authors(by_languages=True, alias=True):
    df = count_translations_by_author()

    if by_languages:
        df = df.sort_values("translation_count", ascending=False)

    if alias:
        df = df[df["alias"].notna()]
        return df["alias"].tolist()

    return df["author"].dropna().tolist()