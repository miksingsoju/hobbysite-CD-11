from django.shortcuts import render, get_object_or_404
from .models import Commission

# Create your views here.

def commission_list(request):         # list of comissions
    commissions = Commission.objects.all()
    return render(request, 'commissions_list.html', {'commissions': commissions})

def commission_detail(request, pk):   # gets 1 commission out of the list
    commission = get_object_or_404(Commission, pk=pk)
    return render(request, 'commissions_detail.html', {'commission': commission})
