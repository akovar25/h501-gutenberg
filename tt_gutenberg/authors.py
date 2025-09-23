from .utils import load_data, count_translations_by_author

def list_authors(by_languages=True, alias=True):
    """
    Function to list author aliases ordered by translation count.

    Parameters:
    by_languages: bool -> currently must be True (translation count)
    alias: bool -> use alias column instead of author name

    Returns:
    A list of author aliases
    """
    # Load data
    authors, metadata, languages = load_data()
    
    # Get counts and return list
    if by_languages:
        counts = count_translations_by_author(authors, metadata, languages, alias=alias)
        return counts["alias" if alias else "name"].tolist()
    else:
        raise NotImplementedError("Only by_languages=True is supported right now.")