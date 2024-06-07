from django.shortcuts import render, get_object_or_404, redirect
from client.models import Client, ProfessionalSummary, Education, Experience, Skill, Hobby, Reference, Language, Certification

#paypal
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings 
import uuid
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def paypal_view(request, client_id, template_id):
    # client = get_object_or_404(Client, id=client_id)
    host = request.get_host()
    protocol = 'https' if request.is_secure() else 'http'
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '3.00',
        'item_name': 'Resume PDF Subscription',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'{protocol}://{host}{reverse("paypal-ipn")}',
        'return_url': f'{protocol}://{host}{reverse("payments:paypal-return", args=[client_id, template_id])}',
        'cancel_return': f'{protocol}://{host}{reverse("payments:paypal-cancel")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypaltest.html', {
        'form':form,
    })

def paypal_return(request, client_id, template_id):
    client = get_object_or_404(Client, id=client_id)
    client.activate_subscription()
    # messages.success(request, "You've successfully made a payment")
    return redirect('builder:generate_pdf', client_id=client_id, template_id=template_id)

def paypal_cancel(request):
    # messages.success(request, "You've cancelled the payment")
    return redirect('resumes:index')