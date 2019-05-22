from  bs4 import BeautifulSoup
from urllib.request import urlopen
import xlsxwriter
import re,os


# .txt FILE TO STORE ALL THE URLs

file=open("pages.txt","w")
sites=["https://pinegrow.com/","https://www.goindigo.in/",
       "https://www.apollohospitals.com/","https://uspoloassn.nnnow.com/",
       "https://www.swiggy.com/","https://www.jabong.com/"
       ,"http://www.fortishealthcare.com/",
       "http://neetabus.in/","https://www.croma.com/"]
for x in sites:
    file.write(x+'\n')
file.close()

#Get path

path=os.getcwd()   #Gives the path of the current directory    
li=path.split("\\")
path_xls='\\\\'.join(li)


'''======================================================================='''

#FETCHNIG DATA FROM EACH URL AND STORING THE REQUIRED DETAILS IN SPREADSHEETS 

file=open("pages.txt","r")
f=file.read()
pages=f.split('\n')
pages.remove('')
allTags=[]
allDensity=[]
i=0
for y in pages:
    try:            #For checking online websites
        url=urlopen(y)
        page=url.read()

    
    except:         #For checking offline HTMLs
        url=open(y,"r")
        page=url.read()

    finally:    
        soup=BeautifulSoup(page,"html.parser")
        i+=1
        title=("S"+str(i))
        tags=[]
        #Getting all the keywords from meta data
        for keys in soup.find_all('meta'):          
            if keys.get('name')=='keywords':
                string=keys.get('content')
                temp=string.split(',')
            else:
                continue

        for x in temp:
            tags.append(x.strip())

        #Gets the body of the URL
        body=soup.get_text().casefold()     

        #Get Title
        tag_count=[]
        m=title.find(' ')
        if m==-1:
            m=len(title)

        #Storing data from each website in a spreadsheet
        try:
            workbook=xlsxwriter.Workbook(path_xls+"\\Spreadsheets\\"+title[0:m]+".xlsx")

        except:
            pass

        finally:
            worksheet=workbook.add_worksheet()
            for x in range(0,len(tags)):
                no=str(x+1)
                col='A'+no
                worksheet.write(col,tags[x])
                key_search=tags[x].casefold()
                exp="\W"+tags[x]+"\W"
                regex=re.compile(exp)
                all=regex.findall(body)
                count=len(all)
                tag_count.append(count)
                no=str(x+1)
                col1='B'+no
                worksheet.write(col1,count)

            #Creating a chart for Keyword v/s Density
            chart=workbook.add_chart({'type':'column'})
            chart.add_series({'values': '=Sheet1!$B$1:$B$'+str(len(tags))})
            chart.set_y_axis({'name': 'Frequency'})
            chart.set_x_axis({'name': 'Keyword No.'})
            chart.set_title({'name': 'Keyword Frequency Chart'})
            chart.set_legend({'none':'true'})
            worksheet.insert_chart('D1',chart)
    
            workbook.close()

        #Storing the tags and their frequency in a list
        db_tags=','.join(tags)
        num=[]
        for x in tag_count:
            num.append(str(x))
        density=','.join(num)
        allTags.append(db_tags)
        allDensity.append(density)



'''======================================================================='''

#For referencing in database.py
        
def getData():
     return pages,allTags,allDensity
        
