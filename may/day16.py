def get_longest_chain(dominoes):
    def dfs(chain, remaining):
        best = chain[:]
        last = chain[-1][1]

        for i, domino in enumerate(remaining):
            a, b = domino
            next_remaining = remaining[:i] + remaining[i+1:]

            # try normal orientation
            if a == last:
                result = dfs(chain + [[a, b]], next_remaining)
                if len(result) > len(best):
                    best = result

            # try flipped orientation
            if b == last and b != a:
                result = dfs(chain + [[b, a]], next_remaining)
                if len(result) > len(best):
                    best = result

        return best

    if not dominoes:
        return []

    best_chain = []

    for i, domino in enumerate(dominoes):
        remaining = dominoes[:i] + dominoes[i+1:]
        a, b = domino

        # start with normal orientation
        result = dfs([domino], remaining)
        if len(result) > len(best_chain):
            best_chain = result

        # start with flipped orientation
        if a != b:
            result = dfs([[b, a]], remaining)
            if len(result) > len(best_chain):
                best_chain = result

    return best_chain
