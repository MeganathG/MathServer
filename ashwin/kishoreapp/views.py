
from django.shortcuts import render

def churn_rate(request):
    churnrate = 0
    P = 0
    T = 0

    if request.method == 'POST':
        P = float(request.POST.get('Initialcustomer', 0))
        T = float(request.POST.get('Customerlost', 0))

        if P > 0:
            churnrate = (T / P) * 100
        else:
            churnrate = 0

        print("Initialcustomer =", P)
        print("Customerlost =", T)
        print("Churn rate =", churnrate)

    return render(request, 'kishoreapp/math.html', {
        'P': P,
        'T': T,
        'churnrate': round(churnrate, 2)
    })
