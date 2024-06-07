from django.urls import path
from resumes.views import resumes
from payments.views import paypal_view, paypal_cancel, paypal_return

app_name = 'payments'

urlpatterns = [
    # paypal 
    path('paypal/<int:client_id>/<int:template_id>/', paypal_view, name='paypal_view'),
    path('paypal-return/<int:client_id>/<int:template_id>/', paypal_return, name='paypal-return'),
    path('paypal-cancel', paypal_cancel, name="paypal-cancel"),
] 