def tri_frequency(s):
    s = s.split(" ")
    print(s)
    hash = {}
    for i in range(0, len(s), 1):
        sentence = ' '.join(s[i:i+3])
        print(s[i:i+3])
        print(len(s[1:1+3]))
        if sentence in hash:
            hash[sentence] += 1
        else:
            hash[sentence] = 1
    print(max(hash, key=hash.get).lower())


corpus = "I came from the moon. He went to the other room. She went to the drawing room."
tri_frequency(corpus)
