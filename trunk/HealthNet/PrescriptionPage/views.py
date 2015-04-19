from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def main_page(request):
    return render_to_response("prescriptions.html")

def stock(request):
    return render_to_response("prescription_stock.html")
