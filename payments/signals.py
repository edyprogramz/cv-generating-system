from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from client.models import Client

@receiver(valid_ipn_received)
def handle_paypal_ipn(sender, **kwargs):
    ipn_obj = sender

    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Payment was successful
        invoice = ipn_obj.invoice
        try:
            client = Client.objects.get(invoice=invoice)
            # Mark the client as paid and activate subscription
            client.activate_subscription()
        except Client.DoesNotExist:
            pass  # Handle the case where the client does not exist


