# Ex.04 Design a Website for Server Side Processing
## Date 16.03.2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
math.html

<html>
    <head>
        <tittle></tittle>
    </head>
    <style>
          body
          {
            background:linear-gradient(45deg,rgb(30, 0, 255),rgb(239, 18, 110));
            margin: 10;
          }  
          .head
          {
            gap:40;
            position: fixed;
            bottom:10%;
            left:35%;
            border: dashed 4px rgb(9, 225, 38);
            border-radius: 20px;
            background: rgb(138, 7, 231);
            padding:100;
          }
          input
         {
            margin-top: 10px;
            padding: 8px;
            border-radius: 20px;
         }
         .form
         {
            border-radius: 10px;
            width:10px;
         }
         .submit
         {
            color:rgb(238, 4, 255);
            background-color: white;
         }
          
    </style>
    <body>
        <center>
            <div class="head">
                <h1>Price Calculator</h1>
                <h2>RAJAVEL MURUGAN  (25012404)</h2>
                <form method="POST">
                    {% csrf_token %}
                <label>PRICE:</label>
                <input type="text" name="price" value="{{Price}}">
                <br>
                <br>
                <label>GST:</label>
                <input type="text" name="GST" value="{{GST}}">
                <br>
                <br>
                <input type="submit" value="Calculate">
                <br>
                <br>
                <label>TOTAL:</label>
                <input type="text" value="{{Total}}">
                </form>
                </div>
            </center>
        </body>
</html>

    ]
views.py
from django.shortcuts import render
def Calculate_bill(request):
	price=float(request.POST.get('price','0'))
	gst=float(request.POST.get('GST','0'))
	total = price+(price*gst/100) if request.method=='POST' else 0
	print("Price=",price)
	print("GST=",gst)
	print("Total=",total)
	return render(request,"mathapp/math.html",{'Price':price,'GST':gst,'Total':total})
urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.Calculate_bill, name='Calculate_bill')
    ]



```


## OUTPUT - SERVER SIDE:


## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-03-16 114610.png>)



## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
