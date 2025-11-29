from django.shortcuts import render
from django.db.models import Sum
from .models import Donation

def dashboard_view(request):
    total_donations = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0
    num_donors = Donation.objects.values('donor_name').distinct().count()

    donations_by_date = (
        Donation.objects.values('date')
        .annotate(total=Sum('amount'))
        .order_by('date')
    )

    labels = [item['date'].strftime('%Y-%m-%d') for item in donations_by_date]
    data = [float(item['total']) for item in donations_by_date]

    donations = Donation.objects.order_by('-date', '-id')

    return render(request, 'dashboard/dashboard.html', {
        'total_donations': total_donations,
        'num_donors': num_donors,
        'labels': labels,
        'data': data,
        'donations': donations,
    })
from django.shortcuts import render
from django.db.models import Sum
from .models import Donation

def dashboard_view(request):
    total_donations = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0
    num_donors = Donation.objects.values('donor_name').distinct().count()

    donations_by_date = (
        Donation.objects.values('date')
        .annotate(total=Sum('amount'))
        .order_by('date')
    )

    labels = [item['date'].strftime('%Y-%m-%d') for item in donations_by_date]
    data = [float(item['total']) for item in donations_by_date]

    donations = Donation.objects.order_by('-date', '-id')

    return render(request, 'dashboard/dashboard.html', {
        'total_donations': total_donations,
        'num_donors': num_donors,
        'labels': labels,
        'data': data,
        'donations': donations,
    })
