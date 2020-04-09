import re

def regex_alpha_k(string):
    alphabet = re.findall("[a-k-A-K-0-5]", string)
    return len(string) == len(alphabet)
