from django.shortcuts import render, get_object_or_404
from .models import Commission

def commission_list(request):      
    commissions = Commission.objects.all()
    return render(request, 'commissions_list.html', {'commissions': commissions})

def commission_detail(request, num = 1):   
    commission = get_object_or_404(Commission, pk = num)
    comments = commission.comments.all()           # comments is the related_name of the foreign key
    context = { 'commission' : commission, 'comments' : comments}
    return render(request, 'commissions_detail.html', context)
