from bs4 import BeautifulSoup
import requests
import pandas as pd

#creating a dictionary of {"NAME of product" : number of pages }
#to loop in

all_kale_products = {"yogurt": 4 , 
                     "icecream" : 9,
                     "dessert" : 4,
                     "milk":4,
                     "sauce":3,
                     "cream":2,
                     "beverage":4,
                     "healthy-food":1,
                     "butter":1,
                     "kashk":1,
                     "sports-supplement":1}
titles=[]
url ="https://kalleh.com/product-category/"
for pName,pageNumbers in all_kale_products.items(): # 2 for loops to preparing the url ready
    url_temp =url + pName
    for i in range(1,pageNumbers+1):
        url_finall= url_temp + "/page/" + str(i)
        page= requests.get(url_finall)
        soup= BeautifulSoup(page.text,"html.parser")
        title=soup.select("h2.woocommerce-loop-product__title") # selecting the "h2" tag to reach content
        for t in title:
            name=t.text
            titles.append(name) #this for takes all h2 tags and append the text instide the list
    
product = {"title": titles}
data=pd.DataFrame.from_dict(product,orient="index")# making a dataframe to write easier in file 
data= data.transpose() # for visualizing
writer = pd.ExcelWriter('product.xlsx')
data.to_excel(writer)
writer.save()
        
    
    