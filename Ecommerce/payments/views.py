import stripe
from decimal import Decimal
from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from order.models import Order
from user.models import Cart
from .models import Payment
from product.models import *

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
@api_view(['POST'])
def stripe_payment(request, order_id):
  try:
    data_dict = request.data
    # payment_intent = stripe.PaymentIntent.create(
    #     amount=500,            # Amount in smallest currency unit (e.g., 500 for GBP = £5.00)
    #     currency="gbp",        # Specify currency
    #     payment_method="pm_card_visa",  # Test PaymentMethod ID
    #     automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
        
    #     confirm=True           # Automatically confirms the PaymentIntent
    # )
    # print("PaymentIntent status:", payment_intent.status)

    # Print PaymentIntent details (for debugging/testing)
    # print("PaymentIntent status:", payment_intent.status)

    
    # try:
    #     token = stripe.Token.create(
    #         card = {
    #                     # "number": str(data_dict['number']),
    #                     # "exp_month": int(data_dict['expiry_month']),
    #                     # "exp_year": int(data_dict['expiry_year']),
    #                     # "cvc": str(data_dict['cvc']),
    #                     "number": str(data_dict['number']),
    #                     "exp_month": int(data_dict['expiry_month']),
    #                     "exp_year": int(data_dict['expiry_year']),
    #                     "cvc": str(data_dict['cvc']),
    #                 },
    #     )
    #     print("Token created/n", token.id)
    # except Exception as e:
    #     print("Token creation failed/n" , e)

    # card_details = {
    #             "type": "card",
    #             "card": {
    #                 "number": data_dict['number'],
    #                 "exp_month": data_dict['expiry_month'],
    #                 "exp_year": data_dict['expiry_year'],
    #                 "cvc": data_dict['cvc'],
    #             },
    #         }

    
    order = Order.objects.filter(id=order_id).first()
    print("Step 1")

    if order:

        print("Step 2")
        # tax = round(order.total_price * Decimal(settings.TAX), 2)
        # total = round(Decimal(order.total_price + tax), 2)
        stripe_total = int(order.total_price*100)


        # payment_method = stripe.PaymentMethod.create(**card_details)

        # print("Payment method created/n", payment_method)
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='inr',
            payment_method=data_dict['payment_method_id'],
            automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
            # payment_method_data={
            # "type": "card",
            # "card": {"token": token.id}
            # },
            # confirmation_method='manual',
            confirm=True
        )

        print("Payment intent created/n", payment_intent)
        
        # payment_intent_modified = stripe.PaymentIntent.modify(
        #         payment_intent['id'],
        #         payment_method=payment_method['id'],
        #     )

        # print("Payment intent modified/n", payment_intent_modified)

        
        # try:
        #         payment_confirm = stripe.PaymentIntent.confirm(
        #             payment_intent['id']
        #         )
        #         payment_intent_modified = stripe.PaymentIntent.retrieve(payment_intent['id'])
        # except:
        #         payment_intent_modified = stripe.PaymentIntent.retrieve(payment_intent['id'])
        #         payment_confirm = {
        #             "stripe_payment_error": "Failed",
        #             "code": payment_intent_modified['last_payment_error']['code'],
        #             "message": payment_intent_modified['last_payment_error']['message'],
        #             'status': "Failed"
        #         }

        payments_obj = Payment.objects.create(order=order, amount=stripe_total, payment_id=payment_intent.client_secret)
        payments_obj.save() 

        print("Payment object created/n", payments_obj)


        if payment_intent and payment_intent['status'] == 'succeeded':
            order.payment_status = True
            order.save()
            user_id = order.user.id
            cart = Cart.objects.get(user=user_id)
            cart_items = cart.cart
            
            for product_id, quantity in cart_items.items():
                review_obj = Review.objects.filter(product_id=product_id, user_id=user_id).first()
                if review_obj:
                    review_obj.verified_purchase = True
                    review_obj.save()
                product_obj = Product.objects.get(id=product_id)
                product_obj.quantity -= quantity
                product_obj.save()

            cart.delete()
            # payments_obj = Payments.objects.get(order=order)
            payments_obj.payment_status = 'success'
            payments_obj.save()

            print("Payment successful/n", payment_intent)

            return Response({
                    'success': "Card Payment Success",
                    # "card_details": card_details,
                    # "payment_intent": payment_intent,
                    # "payment_confirm": payment_confirm
                }, status=status.HTTP_200_OK)
        else:
            order.payment_status = False
            order.save()

            print("Payment unsuccessful/n", payment_intent)

            return Response({
                    'error': "Card Payment Failed",
                    # "card_details": card_details,
                    # "payment_intent": payment_intent_modified,
                    # "payment_confirm": payment_confirm
                }, status=status.HTTP_400_BAD_REQUEST)
    else:

        print("Order not found")
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    print("Exception: ", e)
    return Response({
                # 'error': "Your card number is incorrect",
                # "payment_intent": {"id": "Null"},
                # "payment_confirm": {'status': "Failed"}
                'error': "PaymentIntent not created"
            }, status=status.HTTP_400_BAD_REQUEST)