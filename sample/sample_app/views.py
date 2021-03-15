from django.shortcuts import render,redirect

# Create your views here.


from .models import shop_details,category_details,product_details

def index(request):
    return render(request,'sample_app/index.html')

def add_shop_details(request):
    data = shop_details.objects.all()
    return render(request,'sample_app/add_shop_details.html',{'data':data})

def add_shop_details_action(request):
    if request.method == "POST":
        shop_name = request.POST.get("shop_name")
        shop_location = request.POST.get("shop_location")
        shop_details_save = shop_details(shop_name=shop_name,shop_location=shop_location)
        shop_details_save.save()
        return redirect("index")


def add_category_details(request):
    data = category_details.objects.all()
    return render(request,'sample_app/add_category_details.html',{'data':data})

def add_category_details_action(request):
    if request.method == "POST":
        category = request.POST.get("category")

        data_category_details = category_details(category=category)
        data_category_details.save()
        return redirect("index")


def add_product_details(request):
    data_shop = shop_details.objects.all()
    data_category = category_details.objects.all()
    data = product_details.objects.all()
    return render(request,'sample_app/add_product_details.html',{'data_shop':data_shop,'data_category':data_category,'data':data})



def add_product_action(request):

    if request.method == "POST":
        pic = request.FILES['pic']
        shop_name= request.POST.get("shop_name")
        category= request.POST.get("category")
        name = request.POST.get("name")
        data_cat_id = category_details.objects.get(id=category)

        data_shop_id = shop_details.objects.get(id=shop_name)
        data_product_details = product_details(shop_id=data_shop_id,cat_id=data_cat_id,name=name,product_image=pic)
        data_product_details.save()
        return redirect("index")

import json
from django.http import JsonResponse

def product_api(request):

    shop_id = request.GET.get("shop_id")
    print("shhhhh::",str(shop_id))

    data = product_details.objects.filter(shop_id=shop_id)

    

    data1 = data.values()
    return JsonResponse(list(data1),safe=False)


def delete_shop_details(request):
    id = request.GET.get("id")

    delete_shop_details = shop_details.objects.get(id=id).delete()
    return redirect("add_shop_details")


def delete_category(request):

    id = request.POST.get("id")

    dlel = category_details.objects.get(id=id).delete()
    return redirect("add_category_details")

def delete_product(request):
    id = request.GET.get("id")
    del1 = product_details.objects.get(id=id).delete()
    return redirect("add_product_details")



