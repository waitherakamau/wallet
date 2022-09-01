from django.shortcuts import render

# from wallet.models import Currency
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, Third_partyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def register_currency(request):
    form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})


def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})


def register_account(request):
    form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})

def register_transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})


def register_card(request):
    form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})

def register_third_party(request):
    form=Third_partyRegistrationForm()
    return render(request,"wallet/register_third_party.html",{"form":form})

def register_notification(request):
    form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form})


def register_receipt(request):
    form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})


def register_loan(request):
    form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})

def register_reward(request):
    form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})







# Create your views here.


