def get_count(sentence, count = 0):
    for i in sentence:
        if i in "aeiou":
            count += 1
    return count

get_count("sentence")
