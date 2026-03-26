from .utils import word_overlap, semantic, length_ratio, edit_sim, ngram_overlap, missing_word
def hybrid_score(stimulus, response):
    overlap = word_overlap(stimulus, response)
    semantic_sim = semantic(stimulus, response)
    length = length_ratio(stimulus, response)
    match = edit_sim(stimulus, response)
    bigram_score = ngram_overlap(stimulus, response, n=2)
    final = (
        0.2 * overlap +
        0.25 * semantic_sim +
        0.15 * length +
        0.2 * match +
        0.2 * bigram_score
    )
    if length < 0.6:
        final *= 0.75
    if missing_word(stimulus, response) > 0.4:
        final *= 0.75
    if semantic_sim > 0.9 and overlap > 0.85:
        return 4
    if final > 0.85:
        return 4
    elif final > 0.7:
        return 3
    elif final > 0.5:
        return 2
    elif final > 0.3:
        return 1
    else:
        return 0