from django.shortcuts import render, redirect
from .forms import CalculatorForm
from datetime import datetime
import math

history = []

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data.get('b')
            op = form.cleaned_data['operation']

            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                result = a / b
            elif op == 'pow':
                result = a ** b
            elif op == 'sqrt':
                result = math.sqrt(a)

            history.append({
                'a': a,
                'b': b,
                'operation': dict(form.fields['operation'].choices)[op],
                'result': result,
                'timestamp': datetime.now()
            })
            if len(history) > 10:
                history.pop(0)
    else:
        form = CalculatorForm()

    return render(request, 'calculator/calculator.html', {'form': form, 'result': result})

def history_view(request):
    if request.method == 'POST' and request.POST.get('clear') == 'true':
        history.clear()
        return redirect('calculator:history')
    return render(request, 'calculator/history.html', {'history': history})
