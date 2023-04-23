import hashlib

from mapper_reducer import Mapper


class word_count_Mapper(Mapper):
    def mapper(self):
        with open('output.txt','r') as file:
            file_contents=file.read()
        results = []
        y=[]
        x=file_contents.split("\n")
        for i in x:
            z=i.split(',')
            y.append(z[1:])
        flattened_list = [item for sublist in y for item in sublist]

        
        for line in flattened_list:
            words = line.split()
            for word in words:
                results.append((word, 1))
            
        categories = {}
        num_categories = 5  
        for item in results:
            key = item[0]
            category_num = hash(key) % num_categories  
            if category_num not in categories:
                categories[category_num] = []

            categories[category_num].append(item)


        return categories


riten= word_count_Mapper()
riten.mapper()



                



 