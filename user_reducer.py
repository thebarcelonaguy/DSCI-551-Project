from reducer import Reducer


class UserReducer(Reducer):
    def reducer(self):
        x=Reducer.get(self)
        print(x)



x=UserReducer()
x.reducer()