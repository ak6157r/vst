from django.shortcuts import render
from . models import MainDb
from django.db.models import Q
import re

# Create your views here.

def index(request):
    return render(request, 'index.html')

def main_search(request):
    search = request.POST['search']
    results = []
    if search:
        results = MainDb.objects.filter(Q(iccid1__exact=search)|Q(imsi1__exact=search)|Q(msisdn1__exact=search)|Q(iccid2__exact=search)|Q(imsi2__exact=search)|Q(msisdn2__exact=search)|Q(imei__exact=search)|Q(serial__exact=search)|Q(activation__exact=search))
        for result in results:
            result.highlighted_iccid1 = highlight_text(result.iccid1, search)
            result.highlighted_imsi1 = highlight_text(result.imsi1, search)
            result.highlighted_msisdn1 = highlight_text(result.msisdn1, search)
            result.highlighted_iccid2 = highlight_text(result.iccid2, search)
            result.highlighted_imsi2 = highlight_text(result.imsi2, search)
            result.highlighted_msisdn2 = highlight_text(result.msisdn2, search)
            result.highlighted_imei = highlight_text(result.imei, search)
            result.highlighted_serial = highlight_text(result.serial, search)
            result.highlighted_activation = highlight_text(result.activation, search)
    return render(request, 'search_main.html', {'results': results, 'search': search})
            
            
def highlight_text(text, search):
    if not search:
        return text
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    highlighted = pattern.sub(lambda m: f'<mark>{m.group()}</mark>', text)
    return highlighted        