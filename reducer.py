from user_mapper import word_count_Mapper
from collections import defaultdict


x=word_count_Mapper()
data=x.mapper()

class Reducer:
    def __init__(self):
        self.items = []

    def reduce(self, item):
        self.items.extend(item)
    


num_categories = 5  # number of categories
reducers = [Reducer() for i in range(num_categories)]  # create N reducer instances


for key,value in data.items():
    reducers[key].reduce(value)


word_count_list = []

for i, reducer in enumerate(reducers):
    hashMap = {}
    word_list = reducer.items
    word_dict = {}
    word_count = defaultdict(int)
    # convert the list of key-value pairs to a dictionary
    for key, value in word_list:
        word_dict[key] = word_dict.get(key, 0) + value
        # count the number of occurrences of each word
    for word in word_dict:
        word_count[word] += word_dict[word]
        # convert the dictionary to a list of tuples and sort by the word count
    ans = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
   # print("R" + str(i) + " " + str(ans))
    word_count_list.extend(ans)

#print(word_count_list)
