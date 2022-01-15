from django.shortcuts import render

def homeView(request):
    return render(request,"index.html")

def eligibility_view(request):
    return render(request, "eligibility.html")

def feeCharges_view(request):
    return render(request, "fees_charges.html")