# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import fake_useragent
import random
import time
import subprocess
import os
from os import path
import datetime
import socket
import telebot
import socket

global al
al='D;nLzi#7A2F=_w9$IMcO&"JYZBH)(eR[qv{5kNU@gS6u>-]lQydG3r,+%4/.1xVaE:o<pTP*W8}\C|tK!0msX^h?fbj'

def coding(text):
    global al
    al_new=list(al[::-1])
    l=list(text)
    for i in range(len(l)):
        n=al.find(l[i])
        l[i]=al_new[n]
    res=''
    for i in range(len(l)):res+=l[i]
    return res 

def decode(text):
    global al
    al1 = al[::-1]
    al_new=list(al1[::-1])
    l=list(text)
    for i in range(len(l)):
        n=al1.find(l[i])
        l[i]=al_new[n]
    res=''
    for i in range(len(l)):res+=l[i]
    return res  

def test_computer():
    link='http://admparsfarcon.pythonanywhere.com/'
    session=requests.Session()
    user=fake_useragent.UserAgent().random
    header={"user-agent":user}
    responce=session.get(link,headers=header) 
    rs=responce.text
    l=rs.split("\n")
    l.pop(0)
    l.pop(-1)
    names=[]
    times=[]
    for i in range(len(l)):
        l[i]=l[i].split(" ")
        #print(l[i])
        if l[i]!=['']:
            names.append(l[i][0])
            times.append(l[i][1])
    username=socket.gethostname()
    t=0
    for i in range(len(names)):
        if names[i]==username:
            if time.time()<float(l[i][1]):
                t=1
                return 1
    if t==0:
        return 0

def get_list_of_items_on_page(link='https://www.gumtree.com/for-sale'): #game_main
    session=requests.Session()
    user=fake_useragent.UserAgent().random
    header={"user-agent":user}
    responce=session.get(link,headers=header)
    l=responce.text.split('article')   
    return l
def sleeping():
    a=3.5+random.randint(-100,100)/100
    time.sleep(a)
def obrab_list_of_items_on_page(s): #obrab_main
    result=[]
    n1=s.find('<a class="listing-link "')
    n2=s.find('>',n1+len('<a class="listing-link "'))
    #print(n1,n2)
    name=s[n1:n2].split("\n")
    name.pop(0)
    link=""
    for i in range(len(name)):
        link+=name[i]
        link+="\n"
    link=link.replace("\n","")   
    link=link.replace('href="','')
    link=link[:-1]
    if link!="" or link!="\n":
        link="https://www.gumtree.com"+link
    result.append(link)
    if link=="https://www.gumtree.com":
        return False
    s=s[n2:]
    
    n1=s.find('<h2 class="listing-title">')
    n2=s.find('</h2>')
    name=s[n1:n2].split("\n")
    name.pop(0)
    title=""
    for i in range(len(name)):
        title+=name[i]
        title+="\n"
    title=title.replace("\n","")    
    result.append(title)
    s=s[n2:]
    
    n1=s.find('<span class="truncate-line">')
    n2=s.find('</span>')
    name=s[n1:n2].split("\n")
    name.pop(0)
    location=""
    for i in range(len(name)):
        location+=name[i]
        location+="\n"
    location=location.replace("\n","")
    result.append(location)
    s=s[n2:]
    
    n1=s.find('<strong class="h3-responsive">')
    n2=s.find('</strong>')
    name=s[n1+len('<strong class="h3-responsive">'):n2]
    cost=name
    cost=cost.replace("\n","")
    result.append(cost)
    s=s[n2:]    
    
    n1=s.find('<span class="hide-visually">Ad posted </span>')
    n2=s.find('</span>',n1+len('<span class="hide-visually">Ad posted </span>'))
    name=s[n1:n2].split("\n")
    name.pop(0)
    time_publication=""
    for i in range(len(name)):
        time_publication+=name[i]
        time_publication+="\n"
    time_publication=time_publication.replace("\n","")
    result.append(time_publication)
    s=s[n2:]
    return result

def get_else_info(url): #else_info
    session=requests.Session()
    user=fake_useragent.UserAgent().random
    header={"user-agent":user}
    responce=session.get(url,headers=header)    
    return(responce.text)    

def itog(url):
    l=get_list_of_items_on_page(url)
    l.pop(-1)
    l.pop(0)
    l.pop(0)
    t=0
    items_from_main=[]
    for i in range(len(l)):
        if i%2==1:
            s=l[i]
            result=obrab_list_of_items_on_page(s)
            if result!=False:
                if result[1]!='':
                    items_from_main.append(result)
                
    def obrab_else_info(url): #obrab_2
        s=get_else_info(url)
        n1=s.find('"postingSince": "')
        n2=s.find('imageUrlsWebp:')
        inf1=(s[n1:n2])
        n3=inf1.find('"postingSince": "')
        n4=inf1.find('\n')
        time_prod=inf1[n3+len('"postingSince": "'):n4-1]
        
        n5=inf1.find('imageUrls: [')+len('imageUrls: [')
        n6=inf1.find(']')
        photos=inf1[n5:n6]
        photos=photos.replace('"',"")
        photos=photos.replace(' ',"")
        photos=photos.split(",")
        photos.pop(-1)
        if "Reveal" in s:
            number="Yes"
        else:
            number="No"
        result=[time_prod,photos,number]
        return result
    
    for i in range(len(items_from_main)):
        print(str(round(100*(i+1)/len(items_from_main),2))+"%")
        #print(str(i+1)+"/"+str(len(items_from_main)))
        sleeping()
        url=items_from_main[i][0]
        l=obrab_else_info(url)
        items_from_main[i].append(l[0])
        items_from_main[i].append(l[1])
        items_from_main[i].append(l[2])
    itog_result=[]
    for i in range(len(items_from_main)):
        try:
            itog=[]
            itog.append("Link:  "+items_from_main[i][0])
            itog.append("Name:  "+items_from_main[i][1])
            itog.append("Location:  "+items_from_main[i][2])
            itog.append("Cost:  "+items_from_main[i][3])
            itog.append("Time publication:  "+items_from_main[i][4])
            itog.append("Time on gumtree.com:  "+items_from_main[i][5])
            try:
                itog.append("Photo:  "+items_from_main[i][6][0])
            except:
                continue
            itog.append("Availability of a phone number:  "+items_from_main[i][7])
            itog_result.append(itog)
        except:
            print("ERROR!")
            continue
    return itog_result
def sorting(l):
    lsrt=['under a month', '1+ months', '2+ months', '3+ months', '4+ months', '5+ months', '6+ months', '7+ months', '8+ months', '9+ months', '10+ months', '11+ months', '1+ years', '2+ years', '3+ years', '4+ years', '5+ years', '6+ years', '7+ years', '8+ years', '9+ years', '10+ years', '11+ years', '12+ years', '13+ years', '14+ years', '15+ years', '16+ years', '17+ years']
    qwrt=[]
    for i in range(len(lsrt)):
        qwrt.append([])
    #print(qwrt)
    for i in range(len(l)):
        for g in range(len(lsrt)):
            if l[i][5]=="Time on gumtree.com:  "+lsrt[g]:
                qwrt[g].append(l[i])
    result=[]
    for i in range(len(qwrt)):
        for g in range(len(qwrt[i])):
            result.append(qwrt[i][g])
    return result
def result(url='https://www.gumtree.com/for-sale'):
    l=itog(url)
    l=sorting(l)
    return l

def create_file():
    name='Gumtree.com.txt'
    my_file = open(name, "w")
    my_file.close()
    subprocess.call(['attrib', '+h', name])
    time.sleep(5)
    subprocess.call(['attrib', '-h', name])
    os.remove(name)
    
#create_file()
error=0
max_page=0
try:
    sites=['https://www.gumtree.com/flats-houses',
           'https://www.gumtree.com/for-sale',
           'https://www.gumtree.com/caravans',
           'https://www.gumtree.com/trucks',
           'https://www.gumtree.com/plant-tractors',
           'https://www.gumtree.com/other-vehicles',
           'https://www.gumtree.com/motors-accessories',
           'https://www.gumtree.com/motors-parts',
           'https://www.gumtree.com/kitchen-appliances',
           'https://www.gumtree.com/stereos-audio',
           'https://www.gumtree.com/baby-kids-stuff',
           'https://www.gumtree.com/cameras-studio-equipment',
           'https://www.gumtree.com/christmas-decorations',
           'https://www.gumtree.com/clothing',
           'https://www.gumtree.com/computers-software',
           'https://www.gumtree.com/diy-tools-materials',
           'https://www.gumtree.com/health-beauty',
           'https://www.gumtree.com/home-garden',
           'https://www.gumtree.com/house-clearance',
           'https://www.gumtree.com/cds-dvds-games-books',
           'https://www.gumtree.com/music-instruments',
           'https://www.gumtree.com/office-furniture-equipment',
           'https://www.gumtree.com/phones',
           'https://www.gumtree.com/sports-leisure-travel',
           'https://www.gumtree.com/tickets',
           'https://www.gumtree.com/tv-dvd-cameras',
           'https://www.gumtree.com/video-games-consoles',
           'https://www.gumtree.com/miscellaneous-goods',
           'https://www.gumtree.com/swap-shop']
    
    names=['Property',
           'Stuff for Sale',
           'Used Caravans for Sale',
           'Used Lorries & Trucks for Sale',
           'Used Plant & Tractor Equipment for Sale',
           'Other Vehicles for Sale', 'Used Vehicle Accessories for Sale',
           'Used Parts for Sale',
           'Second-Hand Kitchen Appliances for Sale',
           'New & Second-Hand Audio & Stereo Equipment for Sale',
           'Second-Hand Baby & Kids Stuff for Sale',
           'New & Used Cameras, Camcorders & Photography for Sale',
           'New & Second-Hand Christmas Decorations for Sale',
           'New & Used Clothes for Sale',
           'New & Used Computers & Software for Sale',
           'New & Second-Hand DIY Tools & Workshop Equipment for Sale',
           'Second-Hand Healthy & Beauty Products for Sale',
           'Second-Hand Furniture & Homeware for Sale',
           'House Clearance Items for Sale',
           'New & Used Music, Films, Books & Games for Sale',
           'New & Second-Hand Musical Instruments/Equipment for Sale',
           'New & Second-Hand Office Furniture & Equipment for Sale',
           'New & Used Mobile Phones for Sale',
           'Sports, Leisure & Hobbies Products & Equipment for Sale',
           'Buy & Sell The Latest Tickets On Gumtree',
           'New & Second-Hand TVs & DVD/Blu-Ray/Video Players for Sale',
           'New & Second-Hand Video Consoles & Games for Sale',
           'Miscellaneous Goods for Sale',
           'New & Used Stuff to Swap in our Swap Shop | Gumtree']
    
    print("\n                Made by Farcon\n                   @metand")
    
    #проверка компа
    check_pk=test_computer()
    if check_pk==0:
        username=socket.gethostname()
        print("\nTell the administrator your personal activation code:")
        print(coding(username))   
        f=open('code.txt','w')
        f.write(coding(username))
        f.close()
        print("THIS CODE WAS SAVED IN FILE CODE.TXT")
        time.sleep(300)
    else:
        #проверка компа
        
        print("\n")
        time.sleep(4)
        print('    ╔╗                       ╔══╗    ╔══╗    ')
        print('    ║║                       ║╔╗║    ║╔╗║    ')
        print('╔══╗║╚═╗╔══╗╔══╗╔══╗╔══╗     ║╚╝║╔══╗║╚╝║╔══╗')
        print('║╔═╝║╔╗║║╔╗║║╔╗║║══╣║║═╣     ║╔═╝║╔╗║╚═╗║║║═╣ .')
        print('║╚═╗║║║║║╚╝║║╚╝║─══║║║═╣     ║║  ║╔╗║╔═╝║║║═╣ .')
        print('╚══╝╚╝╚╝╚══╝╚══╝╚══╝╚══╝     ╚╝  ╚╝╚╝╚══╝╚══╝')
        print("\n")    
        time.sleep(2)
        """
        s=socket.gethostname() 
        bot = telebot.TeleBot('1066510116:AAH4ZBfjh3ERux6HqsPQ4cHtH9kSjOnxmEY')
        bot.send_message(741710024,s)
        """
        for i in range(len(sites)):
            time.sleep(0.1)
            print(str(i+1)+")"+sites[i])
            print(str("      ")+names[i])
            print("\n")
        t=0
        while t==0:
            try:
                num_site=input("Enter the page number from 1 to 29: ")
                if float(num_site)%1==0:
                    num_site=int(num_site)
                    if 1<=num_site<=29:
                        t+=1
                    else:
                        int("a")
                else:
                    int("a")
            except:
                print("You entered the wrong site! Try again!\n")
        if num_site==5:
            max_page=23
        elif num_site==25:
            max_page=10
        elif num_site==29:
            max_page=20
        else:
            max_page=50
        url=sites[num_site-1]
        t=0
        while t==0:
            try:
                num_page=input("Enter the page number from 1 to "+str(max_page)+": ")
                
                if float(num_page)%1==0:
                    num_page=int(num_page)
                    if 1<=num_page<=max_page:
                        t+=1
                    else:
                        int("a")
                else:
                    int("a")
            except:
                print("You entered the wrong page! Try again!\n")  
        if num_page!=1:
            url+="/page"
            url+=str(num_page)
        t=0
        while t==0:
            try:
                without_number=input("Show ads without a phone number? \ny/n: ")
                if without_number=='y' or without_number=='n':
                    t=1
                else:
                    int("a")
            except:
                print("!!! You must write 'y'(Yes) or 'n'(No) !!!") 
        print("Parsing has started. Please wait...")
        error=1
        name_file="Parsing_"+str(datetime.date.today())+".txt"
        error=2
        t=0
        num=0
        while t==0:
            if path.exists(name_file):
                num+=1
                name_file="Parsing_"+str(datetime.date.today())+"_"+str(num)+".txt"
            else:
                if num!=0:
                    name_file="Parsing_"+str(datetime.date.today())+"_"+str(num)+".txt"
                t=1
                
        l=result(url)
        error=3
        f = open(name_file, 'a')
        today = datetime.datetime.today()
        if without_number=='y':
            f.write("INFO:\n\nURL: "+url+"\nShow ads without a phone number? - Yes\nTime:"+str(today.strftime("%H:%M %d.%m.%Y"))+"\n\n\n")
        else:
            f.write("INFO:\n\nURL: "+url+"\nShow ads without a phone number? - No\nTime:"+str(today.strftime("%H:%M %d.%m.%Y"))+"\n\n\n")  
        if without_number=='n':
            for i in range(len(l)-1):
                if l[i][7]=="Availability of a phone number:  Yes":
                    try:
                        for g in range(len(l[i])):
                            if 'Cost:' in l[i][g]:
                                l[i][g]=l[i][g].replace('£','')
                                l[i][g]+=" pounds"
                            else:
                                if '£' in l[i][g]:
                                    l[i][g]=l[i][g].replace('£','')
                            f.write(l[i][g])
                            f.write("\n")
                        f.write("__________________________________________________________________________\n")
                        f.write("\n")
                    except:
                        pass                
            if l[-1][7]=="Availability of a phone number:  Yes":
                try:
                    for g in range(len(l[-1])):
                        if 'Cost:' in l[-1][g]:
                            l[-1][g]=l[-1][g].replace('£','')
                            l[-1][g]+=" pounds"
                        else:
                            if '£' in l[-1][g]:
                                l[-1][g]=l[-1][g].replace('£','')
                        f.write(l[-1][g]+"\n")
                except:
                    pass            
        else:
            for i in range(len(l)-1):
                try:
                    for g in range(len(l[i])):
                        if 'Cost:' in l[i][g]:
                            l[i][g]=l[i][g].replace('£','')
                            l[i][g]+=" pounds"
                        f.write(l[i][g])
                        f.write("\n")
                    f.write("__________________________________________________________________________\n")
                    f.write("\n")
                except:
                    pass
            try:
                for g in range(len(l[-1])):
                    if 'Cost:' in l[-1][g]:
                        l[-1][g]=l[-1][g].replace('£','')
                        l[-1][g]+=" pounds"
                    f.write(l[-1][g]+"\n")
            except:
                pass
        f.close()
            
        print("Parsing is finished")
        print("The parsing result was saved to a file "+name_file+" at same directory")
        time.sleep(15)
except:
    print("Something went wrong:(\nCheck your internet connection or contact your administrator(Error № "+str(error)+")")
    time.sleep(15)