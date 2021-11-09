from z3 import Int, Implies

# the set of initial subterms of a set of monoid terms
def initial_subterms(terms):
    subterms = set()
    for t in terms:
        for i in range(len(t) + 1):
            subterms.add(t[:i])
    return subterms

# the set of implications u <= v ==> ux <= vx
# for ux != vx in terms.
# because there is no patterm matching,
# we do slicing, and what is `u` in the instructions
# is now `u[:-1]`, and what is `ux` is now `u`
def sigma(terms):
    sig = set()
    # would use `pairwise`, but this is 3.10
    # for u, v in pairwise(terms):
    for u in terms:
        for v in terms:
            if u == '' or v == '' or u == v:
                pass
            elif u[-1] == v[-1]:
                sig.add(Implies(Int(u[:-1]) <= Int(v[:-1]), 
                                   Int(u) <= Int(v)))
    return sig

# the set of inequations s > t for
# s in terms1 and t in terms2.
# if this is satisfiable together with sigma,
# then the equation Meet(terms1) <= Join(terms2)
# is not valid.
def fail(terms1, terms2)
    fail = set()
    for s in terms1:
        for t in terms2:
            fail.add(Int(s) > Int(t))
    return fail

