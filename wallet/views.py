from django.shortcuts import redirect, render

import wallet
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

from wallet.models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, Third_partyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm


def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, "wallet/register_customer.html", {"form": form})


def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "wallet/customers_list.html", {"customers": customers})


def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, "wallet/register_currency.html", {"form": form})


def list_currencys(request):
    currencys = Currency.objects.all()
    return render(request, "wallet/currencys_list.html", {"currencys": currencys})


def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = WalletRegistrationForm()
    return render(request, "wallet/register_list.html", {"form": form})


def list_wallet(request):
    wallets = Wallet.objects.all()
    return render(request, "wallet/wallet_list.html", {"wallets": wallets})


def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CardRegistrationForm()
    return render(request, "wallet/register_card.html", {"form": form})


def list_cards(request):
    cards = Card.objects.all()
    return render(request, "wallet/cards_list.html", {"cards": cards})


def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html", {"form": form})


def list_transaction(request):
    Transactions = Transaction.objects.all()
    return render(request, "wallet/transaction_list.html", {"transactions": Transactions})


def register_third_party(request):
    if request.method == "POST":
        form = Third_partyRegistrationForm(request.Post)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_third_party.html", {"form": form})


def list_third_party(request):
    third_partys = Third_party.objects.all()
    return render(request, "wallet/third_party_list.html", {"third_partys": third_partys})


def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_notification.html", {"form": form})


def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, "wallet/notifications_list.html", {"notifications": notifications})


def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()
    return render(request, "wallet/register_receipt.html", {"form": form})


def list_receipts(request):
    receipts = Receipt.objects.all()
    return render(request, "wallet/receipts_list.html", {"receipts": receipts})


def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()

    return render(request, "wallet/register_loan.html", {"form": form})


def loans_list(request):
    loan = Loan.objects.all()
    return render(request, "wallet/loans_list.html", {"loans": loan})


def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RewardRegistrationForm()
    return render(request, "wallet/register_reward.html", {"form": form})


def reward_list(request):
    rewards = Reward.objects.all()
    return render(request, "wallet/rewards_list.html", {"rewards": rewards})


def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form.save()
        else:
            form = AccountRegistrationForm()
            return render(request, "wallet/register_account.html", {"form": form})


def accounts_list(request):
    accounts = Account.objects.all()
    return render(request, "wallet/accounts_list.html", {"accounts": accounts})


def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html", {"customer": customer})


def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.metod == "Post":
        form = CustomerRegistrationForm(request.post, instance=customer)
        if form is valid():
            form.save()
            return redirect("customer_profile", id=customer_id')

            else:
                form = CustomerRegistrationForm(
                    "instance-profile", id=customer.id)

                def customers_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'wallet/customers_profile.html', {"customer": customer})

def customers_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,'wallet/customers_profile.html',{"customer":customer})

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

    else:
        form = CustomerRegistrationForm(instance=customer)
    return render(request,"wallet/edit_customer.html",{"form":form})   


# Create your views here.
