from django.shortcuts import render
import random
from .models import merchantModel,ProductModel
from django.views.generic import View
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import MerchantForm,ProductForm
from django.core.serializers import serialize

# Create your views here.
def showlogin(request):
    return render(request,"login.html")

def showindex(request):
    n1 = request.POST.get("uname")
    n2 = request.POST.get("upass")
    if n1 == "admin" and n2 == "admin":
         return render(request,"index.html")
    else:
         return render(request,"login.html",{"message":"Username/Password is Invalid"})



def randamid_pass(request):
    id = random.randrange(11,99)
    upass = random.randint(1,101)
    return render(request,"merchant.html",{"mid":id,"mpass":upass})


def savemerchant(request):
    try:
        vid = request.POST['m1']
        vna = request.POST['m2']
        vcont = request.POST['m3']
        vmail = request.POST['m4']
        vpass = request.POST['m5']
        merchantModel(id=vid,name=vna,contact=vcont,email=vmail,password=vpass).save()
        return render(request,"index.html",{"message1":"data saved"})
    except:
        return render(request,"index.html",{"message2":"Contact/Email-Id is Already Exists"})


def viewmerchant(request):
    return render(request,"viewmerchant.html",{"details":merchantModel.objects.all()})


def deletemerchant(request):
    deleteid = request.GET.get("del_no")
    merchantModel.objects.filter(id=deleteid).delete()
    return render(request,"index.html",{"message3":"Succssfully Deleted"})


class checkuser(View):
    def get(self,request,username,password):
        try:
            res = merchantModel.objects.get(email=username,password=password)
        except:
            data = json.dumps({"message":"invalid"})
            return HttpResponse(data,content_type='application/json',status=400)
        else:
            messa  = json.dumps({"message":"valied"})
            return HttpResponse(messa,content_type='application/json',status=200)

@method_decorator(csrf_exempt,name='dispatch')
class resertpassword(View):
    def put(self,request,gmailusername):
        d1 = request.body
        newpassword = json.loads(d1)
        try:
            res = merchantModel.objects.get(email=gmailusername)
            olddata = {"idno":res.id,
                       "name":res.name,
                       "contact":res.contact,
                       "username":res.email,
                       "password":res.password}
        except:
            mess = json.dumps({"mess":"Invalid"})
            return HttpResponse(mess, content_type="application/json", status=400)

        else:
            olddata.update(newpassword)
            merchantupdate = MerchantForm(olddata,instance=res)
            if merchantupdate.is_valid():
                merchantupdate.save()
            data = json.dumps({"mess":"Valid"})
            return HttpResponse(data,content_type="application/json",status=200)

@method_decorator(csrf_exempt ,name='dispatch')
class changepassword(View):
    def put(self,request,email,password):
        d2 = request.body
        newpasswordchange = json.loads(d2)
        try:
            res1 = merchantModel.objects.get(email=email,password=password)
            olddata = {"idno":res1.id,
                       "name":res1.name,
                       "contact":res1.contact,
                       "username":res1.email,
                       "password":res1.password}

        except:
            message = json.dumps({"mess":"Invalid"})
            return HttpResponse(message,content_type="application/json",status=400)

        else:
            olddata.update(newpasswordchange)
            merchantchange = MerchantForm(olddata,instance=res1)
            if merchantchange.is_valid():
                merchantchange.save()
            data1 = json.dumps({'messa':"Valid"})
            return HttpResponse(data1,content_type="application/json",status=200)

@method_decorator(csrf_exempt,name="dispatch")
class showsavedata(View):
    def post(self,request):
        data = request.body
        d1 = json.loads(data)
        ef = ProductForm(d1)
        if ef.is_valid():
            ef.save()
            js = json.dumps({"message":"Valied"})
        else:
            js = json.dumps({"mess":"Invalid"})
        if ef.errors:
            js = json.dumps(ef.errors)
        return HttpResponse(js,content_type="application/json")


class showproduct(View):
    def get(self,request):
        qs = ProductModel.objects.all()
        json_data = serialize('json',qs)
        return HttpResponse(json_data,content_type="application/json")


class showproviderdelete(View):
    def delete(self,request,id):
        res = ProductModel.objects.all(p_no=id)
        if res == [0]:
            res1 = json.dumps({"delmessage1":"Merchant Deleted"})
            return HttpResponse(res1,content_type="application/json")
        else:
            res2 = json.dumps({"delmessage2":"Not Deleted"})
            return HttpResponse(res2,content_type="application/json")

