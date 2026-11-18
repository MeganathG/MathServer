from django.shortcuts import render
0
def churn_rate(request):

    P = float(request.POST.get('Initialcustomer', '0'))
    T = float(request.POST.get('Customerlost', '0'))

    churnrate = (T / P) * 100 if request.method == 'POST' and P != 0 else 0

    print("Initialcustomer =", P)
    print("Customerlost =", T)
    print("Churn rate =", churnrate)

    return render(request, 'kishoreapp/math.html', {
        'P': P,
        'T': T,
        'churnrate': churnrate
    })