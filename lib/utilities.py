import nltk.corpus
import nltk.tokenize.punkt
import string

def LevenshteinDistance(s, len_s, t, len_t):
    print(s, len_s, t, len_t)
    cost = 0
    if len_s == 0:
        return len_s
    if len_t == 0:
        return len_t
    if s[len_s-1] == t[len_t-1]:
        cost = 0
    else:
        cost = 1
    return min(LevenshteinDistance(s, len_s-1, t, len_t-1) + 1,
               LevenshteinDistance(s, len_s, t, len_t - 1) + 1,
               LevenshteinDistance(s, len_s-1, t, len_t-1) + cost)


def matcher(a, b):
    def is_ci_token_stopword_match(a, b):
        """Check if a and b are matches."""
        tokens_a = [token.lower().strip(string.punctuation) for token in
                    tokenizer.tokenize(a) if token.lower().strip(
                string.punctuation) not in stopwords]
        tokens_b = [token.lower().strip(string.punctuation) for token in
                    tokenizer.tokenize(b) if token.lower().strip(
                string.punctuation) not in stopwords]

        return len(set(tokens_a) & set(tokens_b))
    # ## IPython Notebook for [Bommarito Consulting](http://bommaritollc.com/)
    # Fuzzy sentence matching in Python
    # http://bommaritollc.com/2014/06/fuzzy-match-sentences-in-python
    # **Author**: [Michael J. Bommarito II]
    # (https://www.linkedin.com/in/bommarito/)
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(string.punctuation)
    stopwords.append('\n')

    # Create tokenizer
    tokenizer = nltk.tokenize.TreebankWordTokenizer()
    return is_ci_token_stopword_match(a, b)

