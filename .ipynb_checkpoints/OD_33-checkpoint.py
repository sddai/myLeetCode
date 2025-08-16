def word_encode(sentence):
    stop_set = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    words = sentence.split(" ")
    new_sentence = []
    for i, word in enumerate(words):
        has_stop = False
        new_word = []
        for j, s in enumerate(word):
            if s not in stop_set:
                new_word.append(s)
            elif s in stop_set:
                has_stop = True
                # words[i][j] = "*"
                new_word.append("*")
        if not has_stop:
            # words[i][0], words[i][-1] = words[i][-1], words[i][0]
            new_word[0], new_word[-1] = new_word[-1], new_word[0]
        new_sentence.append("".join(c for c in new_word))
    return " ".join([w for w in new_sentence])

print(word_encode("Hello world"))
print(word_encode("cry happy dry"))