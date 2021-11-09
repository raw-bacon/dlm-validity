# the set of initial subterms of a set of monoid terms
def initial_subterms(terms):
    subterms = set()
    for t in terms:
        for i in range(len(t) + 1):
            subterms.add(t[:i])
    return subterms


