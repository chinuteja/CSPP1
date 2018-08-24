'''
    Author : teja
    Date : 24/8/2018
'''
def search(search_index, query):
    '''
        function to search through the search index and return the results
        split the query into lowercase words
        check if the word is in the search_index
        collect all the values for the words that are in the search_index
        make a set of doc_id and return
    '''
    list1 = set()
    query = query.lower()
    query = query.split()
    for i in query:
        if i in search_index:
            list2 = list(search_index.get(i))
            for j in list2:
                list1.add(j[0])
    return list1
def process_queries(search_index, queries):
    '''
        function to process the search queries
        iterate through all the queries and call the search function
        print the results returned by search function
    '''
    for i in queries:
        print(search(search_index, i))
def main():
    '''
        main function
    '''
    # This line loads the search index
    search_index = eval(input())
    # read the number of search queries
    lines = int(input())
    # read the search queries into a list
    queries = []
    for i in range(lines):
        queries.append(input())
        i = i+1
    #print(queries)
    # call process queries
    process_queries(search_index, queries)
if __name__ == '__main__':
    main()
