
'''
   author : teja
   date : 24/8/2018
'''
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    str1 = ''
    for i in text:
        for j in i:
            if 'a' <= j <= 'z' or j == ' ':
                str1 += j
    list1 = str1.split()
    extra = load_stopwords("stopwords.txt")
    list2 = list1[:]
    for i in list2:
        if i in extra:
            list1.remove(i)
    return list1
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    # clean up doc and tokenize to words list
    # add or update the words of the doc to the search index
    # return search index
    import collections
    len_docs = len(docs)
    searchindex = {}
    for i in range(len_docs):
        docs[i] = word_list(docs[i])
        docs[i] = collections.Counter(docs[i])
    for i in range(len_docs):
        for j in docs[i]:
            if j in searchindex:
                searchindex[j].append((i, docs[i][j]))
            else:
                searchindex[j] = [(i, docs[i][j])]
    return searchindex
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input().lower())
        i = i+1
    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
