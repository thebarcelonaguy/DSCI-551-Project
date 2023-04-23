from user_mapper import word_count_Mapper

x=word_count_Mapper()
data=x.mapper()

class Reducer:
    def __init__(self):
        self.items = []

    def reduce(self, item):
        self.items.extend(item)
    
    def get(self):
        return self.items

num_categories = 5  # number of categories
reducers = [Reducer() for i in range(num_categories)]  # create N reducer instances


for key,value in data.items():
    reducers[key].reduce(value)

for i, reducer in enumerate(reducers):
    print(f"Reducer {i+1}: {reducer.items}")