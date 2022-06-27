from django.shortcuts import render,redirect
from . models import Items, Branch1, Branch2, Branch3
from . forms import ItemsForm,Branch1Form,Branch2Form,Branch3Form
from django.contrib import messages
import csv, io
from django.db.models import Q
from django.http import HttpResponse
from itertools import chain
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    items = Items.objects.all()
    p = Paginator(Items.objects.all(), 10)
    page = request.GET.get('page')
    item_list = p.get_page(page)
    nums = "a" * item_list.paginator.num_pages
    context = {'items':items, 'item_list':item_list, 'nums':nums}
    return render(request,'home.html', context)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if request.method == "POST":
            itemz = Items.objects.filter(Q(ICCID1__contains=searched)|Q(IMSI1__contains=searched)|Q(MSISDN1__contains=searched)|Q(ICCID2__contains=searched)|Q(IMSI2__contains=searched)|Q(MSISDN2__contains=searched)|Q(IMEI__contains=searched)|Q(STATUS__contains=searched))
            return render(request,'search.html',{'searched':searched,'itemz':itemz})
    return render(request,'search.html')

def add(request):
    form = ItemsForm()
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item added successfully...")
            return redirect('home')
    return render(request,'add.html',{'form':form})

def update(request,item_id):
    item = Items.objects.get(id=item_id)
    form = ItemsForm(instance=item)
    if request.method == "POST":
        form = ItemsForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been updated successfully!")
            return redirect('home')
    return render(request,'update.html',{'form':form})

def delete(request,item_id):
    Items.objects.get(id=item_id).delete()
    messages.success(request,"Item deleted successfully!")
    return redirect('home')

def upload(request):
    templates = 'upload.html'
    prompt = {
        'order':'Order of the csv must be: ICCID1, IMSI1, MSISDN1, ICCID2, IMSI2, MSISDN2, IMEI, STATUS'
    }
    if request.method == "GET":
        return render(request,templates,prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _,created = Items.objects.update_or_create(
            ICCID1=column[0],
            IMSI1= column[1],
            MSISDN1=column[2],
            ICCID2=column[3],
            IMSI2=column[4],
            MSISDN2=column[5],
            IMEI=column[6],
            STATUS=column[7],
        )
    context = {}
    messages.success(request,"Items have been uploaded successfully!")
    return render(request, templates, context)

def branch2(request):
    branch1 = Branch1.objects.all()
    pagination = Paginator(Branch1.objects.all(), 10)
    pages = request.GET.get('page')
    br = pagination.get_page(pages)
    numbers = "z" * br.paginator.num_pages
    context = {'branch1':branch1, 'br':br, 'numbers':numbers}
    return render(request,'branch1.html',context)

def add2branch2(request):
    form = Branch1Form()
    if request.method == "POST":
        form = Branch1Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item added successfully")
            return redirect('branch2')
    return render(request,'add2branch2.html',{'form':form})

def update2branch2(request, branch2_id):
    branch2 = Branch1.objects.get(id=branch2_id)
    form = Branch1Form(instance=branch2)
    if request.method == "POST":
        form = Branch1Form(request.POST,instance=branch2)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been updated successfully")
            return redirect('branch2')
    return render(request,'update2branch2.html',{'form':form})

def delete2branch2(request, branch2_id):
    Branch1.objects.get(id=branch2_id).delete()
    return redirect('branch2')

def upload2branch2(request):
    templates = 'upload2branch2.html'
    prompt = {
        'order':'Order of the csv must be: ICCID1, MSISDN1, STATUS'
    }
    if request.method == "GET":
        return render(request,templates,prompt)
    csv_file = request.FILES['file2']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _,created = Branch1.objects.update_or_create(
            iccid1=column[0],
            msisdn1=column[1],
            status=column[2],
        )
    context = {}
    messages.success(request,"Item has been uploaded successfully!")
    return render(request, templates, context)

def search_branch3(request):
    if request.method == "POST":
        search = request.POST['search']
        if request.method == "POST":
            item = Items.objects.filter(Q(ICCID1__contains=search)|Q(MSISDN1__contains=search)|Q(STATUS__contains=search))
            itemzz = Branch1.objects.filter(Q(iccid1__contains=search)|Q(msisdn1__contains=search)|Q(status__contains=search))
            qs = chain(item, itemzz)
            return render(request,'search_branch2.html',{'search':search, 'qs':qs})
    return render(request,'search_branch2.html')
    
def branch3(request):
    branch3 = Branch2.objects.all()
    pg = Paginator(Branch2.objects.all(), 10)
    pagez = request.GET.get('page')
    br3 = pg.get_page(pagez)
    numb = "c" * br3.paginator.num_pages
    context = {
        'branch3':branch3,
        'br3':br3,
        'numb':numb
    }
    return render(request,'branch3.html',context)

def search_branch4(request):
    if request.method == "POST":
        searches = request.POST['searches']
        if request.method == "POST":
            item = Items.objects.filter(Q(ICCID2__contains=searches)|Q(MSISDN2__contains=searches)|Q(STATUS__contains=searches))
            group = Branch2.objects.filter(Q(iccid2__contains=searches)|Q(msisdn2__contains=searches)|Q(status__contains=searches))
            qz = chain(item, group)
            return render(request,'search_branch4.html',{'searches':searches,'qz':qz})
    return render(request,'search_branch4.html')

def add2branch3(request):
    form = Branch2Form()
    if request.method == "POST":
        form = Branch2Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item added successfully!")
            return redirect('branch3')
    return render(request,'add2branch3.html',{'form':form})

def update2branch3(request, branch3_id):
    branch3 = Branch2.objects.get(id=branch3_id)
    form = Branch2Form(instance=branch3)
    if request.method == "POST":
        form = Branch2Form(request.POST,instance=branch3)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been updated successfully!")
            return redirect('branch3')
    return render(request,'update2branch3.html',{'form':form})

def delete2branch3(request, branch3_id):
    branch3.objects.get(id=branch3_id).delete()
    messages.success(request,"item has been deleted successfully!")
    return redirect('branch3')

def upload2branch3(request):
    templates = 'upload2branch3.html'
    prompt = {
        'order':'Order of the csv must be: ICCID2, MSISDN2, STATUS'
    }
    if request.method == "GET":
        return render(request, templates, prompt)
    csv_file = request.FILES['filess']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _,created = Branch2.objects.update_or_create(
            iccid2 = column[0],
            msisdn2 = column[1],
            status = column[2],
        )
    context = {}
    messages.success(request,"Item has been uploaded successfully!")
    return render(request, templates, context)

def branch4(request):
    branch4 = Branch3.objects.all()
    pgs = Paginator(Branch3.objects.all(), 10)
    pags = request.GET.get('page')
    br4 = pgs.get_page(pags)
    number = "n" * br4.paginator.num_pages
    context = {
        'branch4':branch4,
        'br4':br4,
        'number':number,
    }
    return render(request,'branch4.html',context)

def add2branch4(request):
    form = Branch3Form()
    if request.method == "POST":
        form = Branch3Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been added successfully!")
            return redirect('branch4')
    return render(request,'add2branch4.html',{'form':form})

def update2branch4(request, branch4_id):
    branch4 = Branch3.objects.get(id=branch4_id)
    form = Branch3Form(instance=branch4)
    if request.method == "POST":
        form = Branch3Form(request.POST,instance=branch4)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been updated successfully!")
            return redirect('branch4')
    return render(request,'update2branch4.html',{'form':form})

def delete2branch4(request, branch4_id):
    Branch3.objects.get(id=branch4_id).delete()
    messages.success(request,"Item has been deleted successfully!")
    return redirect('branch4')

def upload2branch4(request):
    templates = 'upload2branch4.html'
    prompt = {
        'order':'Order of the csv must be: ICCID1, IMEI, SERIAL, STATUS'
    }
    if request.method == "GET":
        return render(request, templates, prompt)
    csv_file = request.FILES['filez']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _,created = Branch3.objects.update_or_create(
            iccid1 = column[0],
            imei = column[1],
            serial = column[2],
            status = column[3],
        )
    context = {}
    messages.success(request,"Item has been uploaded successfully!")
    return render(request, templates, context)

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vstiot.csv'
    
    writer = csv.writer(response)
    
    items = Items.objects.all()
    
    writer.writerow(['ICCID1','IMSI1','MSISDN1','ICCID2','IMSI2','MSISDN2','IMEI','STATUS'])
    
    for item in items:
        writer.writerow([item.ICCID1, item.IMSI1, item.MSISDN1, item.ICCID2, item.IMSI2, item.MSISDN2, item.IMEI, item.STATUS])
    
    return response

def export_csv_branch2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= vstb2.csv'
    
    writer = csv.writer(response)
    
    branch1 = Branch1.objects.all()
    
    writer.writerow(['ICCID1', 'MSISDN1', 'STATUS'])
    
    for branch in branch1:
        writer.writerow([branch.iccid1, branch.msisdn1, branch.status])
    
    return response

def export_csv_branch3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vstb3.csv'
    
    writer = csv.writer(response)
    
    branch2 = Branch2.objects.all()
    
    writer.writerow(['ICCID2', 'MSISDN2', 'STATUS'])
    
    for branch in branch2:
        writer.writerow([branch.iccid2, branch.msisdn2, branch.status])
    
    return response

def export_csv_branch4(response):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vstb4.csv'
    
    writer = csv.writer(response)
    
    branch3 = Branch3.objects.all()
    
    writer.writerow(['ICCID1', 'IMEI', 'SERIAL', 'STATUS'])
    
    for branch in branch3:
        writer.writerow([branch.iccid1, branch.imei, branch.serial, branch.status])
        
    return response

def search_branch5(request):
    if request.method == "POST":
        searchz = request.POST['searchz']
        if request.method == "POST":
            itemm = Items.objects.filter(Q(ICCID1__contains=searchz)|Q(STATUS__contains=searchz))
            groups = Branch3.objects.filter(Q(iccid1__contains=searchz)|Q(imei__contains=searchz)|Q(serial__contains=searchz)|Q(status__contains=searchz))
            ig = chain(itemm,groups)
            return render(request,'search_branch5.html',{'searchz':searchz, 'ig':ig})
    return render(request,'search_branch5.html')

    
    