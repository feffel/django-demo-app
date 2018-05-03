from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from apps.leads.models import Lead
from apps.leads.forms import LeadForm


@require_http_methods(['GET'])
def LeadsListView(request):
    leads = Lead.objects.all()
    return render(request, 'leads/list.html', {'leads': leads})


@require_http_methods(['GET', 'POST'])
def LeadsAddView(request):
    if request.method == "POST":
        action = request.POST.get('action')
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            if action == "redirect":
                return render(
                    request, 'leads/list.html', {'leads': Lead.objects.all()})
            else:
                form = LeadForm()
    else:
        form = LeadForm()
    return render(request, 'leads/add.html', {'form': form})
