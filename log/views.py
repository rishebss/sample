from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm  

def service(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  
        else:
            
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    else:
        form = AppointmentForm()

    return render(request, 'service.html', {'form': form})

