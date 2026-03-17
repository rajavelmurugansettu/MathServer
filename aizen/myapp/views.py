from django.shortcuts import render
def Total_bill(request):
	p=int(request.POST.get('price'=0))
	G=int(request.POST.get('GSt'=0))
	Total_bill = p + (p*G/100) if request.method==POST else 0
	print("price=",p)
	print("GST=",G)
	print("Total_bill=",Total_bill)
	return render(request,'myapp/sukuna.html',{'p':p,'G':G,'Total_bill':Total_bill})


