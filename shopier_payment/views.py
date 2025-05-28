import hashlib
import hmac
import base64
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def generate_signature(data, secret):
    message = ''.join(str(data[k]) for k in sorted(data.keys()))
    signature = base64.b64encode(hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest())
    return signature.decode()

def payment_view(request):
    data = {
        'api_key': settings.SHOPIER_API_KEY,
        'website_index': '1',
        'platform_order_id': '123456',
        'product_name': 'Ürün Adı',
        'total_order_value': '99.99',
        'currency': 'TRY',
        'user_email': 'ali@example.com',
        'user_name': 'Ali',
        'user_surname': 'Veli',
        'user_address': 'İstanbul, Türkiye',
        'user_phone': '05000000000',
        'billing_address': 'İstanbul, Türkiye',
        'shipping_address': 'İstanbul, Türkiye',
        'buyer_account_age': '1',
        'client_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
        'is_in_frame': '0',
        'status_email': '1',
        'redirect_url': 'https://yourdomain.com/payment-success/',
        'cancel_url': 'https://yourdomain.com/payment-cancel/',
        'module': 'Django',
    }
    data['signature'] = generate_signature(data, settings.SHOPIER_API_SECRET)
    return render(request, 'shopier_form.html', {'data': data})



@csrf_exempt
def shopier_callback(request):
    if request.method == 'POST':
        print("🔁 Shopier Callback Geldi:", request.POST)
        return HttpResponse("OK")
    return HttpResponse("Invalid Request", status=400)


def payment_success(request):
    return HttpResponse("<h1>✅ Ödeme Başarılı!</h1>")


def payment_cancel(request):
    return HttpResponse("<h1>❌ Ödeme İptal Edildi.</h1>")
