from django.shortcuts import render
from .forms import UserInputForm

def input_form(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = UserInputForm()
    return render(request, 'input_form.html', {'form': form})
