class UnificationError(Exception):
    pass

def unify_var(var, x, theta):
    """
    Helper function to handle variable unification.
    """
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):
    """
    Main unification function.
    """
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.isalpha():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.isalpha():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        raise UnificationError("Unification failed")

# Example usage:
if __name__ == "__main__":
    try:
        theta = unify(['P', 'x', 'y'], ['P', 'A', 'B'], {})
        print("Unification successful. Substitution:", theta)
    except UnificationError as e:
        print("Unification failed:", str(e))

