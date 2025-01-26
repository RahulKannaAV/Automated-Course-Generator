import yake


def get_important_keywords(text):
    extractor = yake.KeywordExtractor()
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 15
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)

    filtered_keywords = []

    for kw in keywords:
        filtered_keywords.append(kw[0])

    return filtered_keywords

