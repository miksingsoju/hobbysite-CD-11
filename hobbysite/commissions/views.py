from django.shortcuts import render, get_object_or_404
from .models import Commission

# this will be called when the url is commissions/list and will take the template from the commissions_list.html file
def commission_list(request):      
    commissions = Commission.objects.all()
    return render(request, 'commissions_list.html', {'commissions': commissions})

# this will be called when the url is commissions/details/number and will take the template from the commissions_details.html file
def commission_detail(request, num = 1):   
    commission = get_object_or_404(Commission, pk = num)
    comments = commission.comments.all()            # gets all comments from the commission
    commissions = Commission.objects.all()          # for the mini commissions list sidebar
    context = { 'commission' : commission, 'comments' : comments, 'commissions' : commissions}    
    return render(request, 'commissions_detail.html', context)
