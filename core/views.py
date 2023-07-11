from django.shortcuts import render, redirect

def home_page(request):
    return render(request, 'core/index.html')

def search_results_view(request):
    trip_type = request.GET['trip_type']
    origin = request.GET['origin']
    destination = request.GET['destination']
    date_outbound = request.GET['date_outbound']
    date_return = request.GET['date_return']
    context = {
        'trip_type':trip_type,
        'origin':origin,
        'destination':destination,
        'date_outbound':date_outbound,
        'date_return':date_return
    }
    return render(request, 'core/search-results.html', context)