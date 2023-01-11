import secrets

def private_key(p):
    # secrets.randbelow(N) returns a random integer between 0 and N exclusive.
    return secrets.randbelow(p - 2) + 2


def public_key(p, g, private):
    # pow -> (g ** private) % p
    return pow(g, private, p)


def secret(p, public, private):
    # pow -> (public ** private) % p
    return pow(public, private, p)
