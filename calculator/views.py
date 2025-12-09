from django.shortcuts import render

def index(request):
    result = None
    error = None
    a = ''
    b = ''
    op = ''

    if request.method == 'POST':
        a = request.POST.get('a', '').strip()
        b = request.POST.get('b', '').strip()
        op = request.POST.get('operation', '')

        try:
            x = float(a)
            y = float(b)

            if op == 'add':
                result = x + y
            elif op == 'sub':
                result = x - y
            elif op == 'mul':
                result = x * y
            elif op == 'div':
                if y == 0:
                    error = 'Деление на ноль невозможно.'
                else:
                    result = x / y
            else:
                error = 'Неизвестная операция.'

        except ValueError:
            error = 'Пожалуйста, вводите числа (например: 2 или 3.5).'

    context = {
        'result': result,
        'error': error,
        'a': a,
        'b': b,
        'op': op,
    }
    return render(request, 'calculator/index.html', context)
