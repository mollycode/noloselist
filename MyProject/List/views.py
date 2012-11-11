# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import ItemForm, Item

def List(request):

	if request.method == 'POST':
		form = ItemForm(request.POST) 
		if form.is_valid():
			newItem = form.save()
			return HttpResponseRedirect('')
		else:
			listitems = Item.objects.filter(active="true").order_by("due")
			return render_to_response('list.html',
			{'form':form, 'listitems': listitems},
			context_instance=RequestContext(request))

	else:
		form = ItemForm()
		listitems = Item.objects.order_by("due")

	return render_to_response('list.html',
		{'form':form, 'listitems': listitems},
		context_instance=RequestContext(request))