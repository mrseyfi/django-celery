from django.shortcuts import render, redirect, get_object_or_404
from .forms import NumberForm
from .models import Number
from .tasks import adding


def home(request):
	numbers = Number.objects.all()
	if request.method == 'POST':
		form = NumberForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			num = Number(x=cd['x'], y=cd['y'])
			num.save()
			result = adding.delay(cd['x'], cd['y'], num.id)
			num.task_id = result.id
			num.save()
			return redirect('home:home')
	else:
		form = NumberForm()
	return render(request, 'home/home.html', {'form':form, 'numbers':numbers})


def nums(request, num_id):
	num = get_object_or_404(Number, id=num_id)
	return render(request, 'home/nums.html', {'num':num})