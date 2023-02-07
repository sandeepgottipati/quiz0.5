from flask import Flask,render_template,url_for,request
import pandas as pd
import csv
app=Flask(__name__)
storagelist=[]
def csv_to_list():
    global storagelist
    with open("data-1.csv","r") as f:
        reader=csv.DictReader(f)
        for row in reader:
            storagelist.append(row)
    return storagelist
storagelist=csv_to_list()  
print(storagelist)
@app.route('/')
def home():
    return render_template('home.html',picture="pictures/m.jpg",name="Sai Sandeep Gottipati")


## for elven a 
@app.route('/listall')
def list_all_names_comments_income():
    user_list=[]
    income_list=[]
    comment_list=[]
    for i in range(0,len(storagelist)):
        user_list.append(storagelist[i]['name'])
        income_list.append(storagelist[i]['income'])
        comment_list.append(storagelist[i]['comments'])

    return render_template('listall.html',user_list=user_list,income_list=income_list,comment_list=comment_list,zip=zip)
## for eleven b
@app.route('/listpictures')
def list_pictures_by_name():
    pictures_list=[]
    user_list=[]
    for i in range(0,len(storagelist)):
       
        if(storagelist[i]['picture']!=" " and storagelist[i]['picture']!=''):
            pictures_list.append("/static/pictures/"+storagelist[i]['picture'])
            user_list.append(storagelist[i]['name'])
        
    return render_template('listpictures.html',pictures_list=pictures_list,user_list=user_list,zip=zip)
if __name__=="__main__":
    app.run(debug=True)