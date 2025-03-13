from django.shortcuts import render, get_object_or_404
from .models import Commission

def commission_list(request):      
    commissions = Commission.objects.all()
    return render(request, 'commissions_list.html', {'commissions': commissions})

def commission_detail(request, num = 1):   
    commission = get_object_or_404(Commission, pk = num)
    comments = commission.comments.all()  
    commissions = Commission.objects.all()
    context = { 'commission' : commission, 'comments' : comments, 'commissions' : commissions}  
    return render(request, 'commissions_detail.html', context)
