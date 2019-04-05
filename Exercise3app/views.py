from .forms import RegistrationForm, IdolCreationForm
from .models import IdolDetail
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,  redirect, get_object_or_404
import operator


@login_required
def idoldetailview(request, pk):
	idolinfo = get_object_or_404(IdolDetail, pk=pk)
	return render(request, 'Exercise3app/idoldetailview.html', {'idolinfo' : idolinfo})

@login_required
def idolfulllist(request):
	if 'search_function' in request.GET:
		search_idol_term = request.GET.get('search_function').split(" ")
		idolwholelist = IdolDetail.objects.all()
		for term in search_idol_term:
			idolwholelist = idolwholelist.filter(
				Q(namefirst__icontains=term) | 
				Q(namelast__icontains=term) | 
				Q(namemiddle__icontains=term) | 
				Q(nickname__icontains=term))
		idolwholelist = idolwholelist.distinct()
	else:
		idolwholelist = IdolDetail.objects.order_by('namelast')
	return render(request, 'Exercise3app/idolfulllist.html', {'idolwholelist' : idolwholelist})

@login_required
def idolregister(request):
	if request.method == 'POST':
		forms = IdolCreationForm(request.POST, request.FILES)
		if forms.is_valid():
			forms.save()
			formskey = forms.save(commit=False)
			return redirect('idoldetailview', pk=formskey.pk)
	else:
		forms = IdolCreationForm()
	return render(request, 'Exercise3app/idolregister.html', {'forms' : forms})

@login_required
def idol_edit(request, pk):
	formsinfo = get_object_or_404(IdolDetail, pk=pk)
	if request.method == 'POST':
		forms = IdolCreationForm(request.POST, request.FILES, instance=formsinfo)
		if forms.is_valid():
			forms.save()
			formskey = forms.save(commit=False)
			return redirect('idoldetailview', pk=formskey.pk)
	else:
		forms = IdolCreationForm(instance = formsinfo)
	return render(request, 'Exercise3app/idolregister.html', {'forms' : forms})

def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login.html')
	else:
		form = RegistrationForm()
	return render(request, 'registration/registration.html', {'form' : form})

def welcome(request):
	idoltoplist = IdolDetail.objects.order_by('-votes')[0:4]
	return render(request, 'Exercise3app/welcome.html', {'idoltoplist' : idoltoplist})