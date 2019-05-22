from bs4 import BeautifulSoup
import database,imp,search


class demo:
    
    def find(self):
        #SEARCH

        #Getting data from database

        page=database.getPages()
        keys=database.getKeys()
        density=database.getDense() #keys and density are nested lists

        print('Welcome user,')
        print()

        #Keyword input

        inp=input("Enter a keyword: ")


        match=[]    #List of URLs in which keywords match
        freq=[]     #List of frequency of the keyword in each URL

        length=len(page)

        for x in range(0,length):
            page_keys=keys[x].split(',')
            page_freq=density[x].split(',')
            word_len=len(page_keys)
            for y in range(0,word_len):
                if page_keys[y].casefold()==inp.casefold():
                    match.append(page[x])
                    freq.append(page_freq[y])


        '''========================================================================'''

        #SORTING IN DESCENDING ORDER

        for x in range(0,len(freq)):
            for y in range(x+1,len(freq)):
                if freq[x]<freq[y]:
                    temp=freq[x]
                    temp1=match[x]
                    freq[x]=freq[y]
                    match[x]=match[y]
                    freq[y]=temp
                    match[y]=temp1

        print()
        print()
        print("*************************************************************************")
        print()

        if match==[]:
            print("No result found")
        else:
            print(str(len(match))+' Results found:')
            print()
            for x in match:
                print(x)

        d=demo()
        d.yesno()




    def yesno(self):
        print()
        print()
        opt=input("New Search? (yes/no):  ")
        if opt.casefold()=='yes'.casefold():
            print()
            d=demo()
            d.find()
        else:
            print()
            print("Thank you!!")
            exit()


d=demo()
d.find()
