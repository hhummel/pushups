def lcs(s1, s2):
    if not (s1 and s2):
        return ""
    elif s1[-1] == s2[-1]:
        last = s1[-1]
        return lcs(s1[:-1], s2[:-1]) + last
    else:
        v1 = lcs(s1, s2[:-1])
        v2 = lcs(s1[:-1], s2)
        if len(v1) > len(v2):
            return v1
        else:
            return v2

if __name__ == "__main__":
    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    result = lcs(s1, s2)
    print result

