# lấy danh sách stopwords từ từ điển:
stopwords = []
with open("vietnamese-stopwords.txt", 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        stopwords.append(line)

# print(stopwords)


# lọc ra stopwords từ các words đầu vào
def filter_stopwords(input_arr):
    results = []
    for word in input_arr:
        if word in stopwords:
            results.append(word)

    return results
