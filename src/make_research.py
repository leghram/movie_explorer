'''
 title, gender, rating, tag, release_date
 los problemas son tag y rating

 Regex: '.*'


'''

def get_data():
    dict_data = [
        [{'moveId' : 1}, {'title' : 'title1 (1996)'}, {'genres' : 'Drama|Comedia|'},
         {'tags' : ['funny','tag2','tag3']}, {'release_date' : '1996'}, {'ratings' : [{'rating' : 'value rating 1'},
                    {'rating' : 'value ratings 2'}]}],

        [{'moveId': 2}, {'title': 'title2 (2006)'}, {'genres': 'Horror|Suspense'},
         {'tags': ['family', 'tag4', 'tag5']}, {'ratings': [{'rating': 'value rating 3'},
                    {'release_date' : '2006'}, {'rating': 'value ratings 4'}]}]
    ]
    return dict_data

def filter_data_with_input_args(data_csv, input_args):
    filtered_data = []
    print(len(data_csv))
    for a in range(len(data_csv)):
        for b in range(len(data_csv[a])):
            print(data_csv[a][b]['moveId'])



        #filtered_data = [print((key,value)) for (key,value) in data_csv[i].items()]
    #print(filtered_data)



def research(input_args):
    data_csv = get_data()
    filtered_data = filter_data_with_input_args(data_csv=data_csv, input_args=input_args)





if __name__ == '__main__':
    research({'title': 'Toy Story', 'genres': '.*', 'rating': '.*', 'tag': '.*', 'release_date': '.*', 'order': '.*', 'by': '.*'})