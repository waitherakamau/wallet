# from locale import currency
from unicodedata import name
from django.urls import path

from wallet.models import Customer
from .views import customer_profile, edit_customer, list_currencys, list_customers, register_account, register_card, register_currency, register_customer, register_loan, register_loan, register_notification, register_receipt, register_reward, register_third_party, register_transaction, register_wallet
from .import views
# import wallet
urlpatterns=[
path("register/",register_customer,name="registration"),
path("currency/",register_currency,name="registration"),
path("wallet/",register_wallet,name="registration"),
path("account/",register_account,name="registration"),

path("transaction/",register_transaction,name="registration"),
path("card/",register_card,name="registration"),
path("third_party/",register_third_party,name="registration"),
path("notification/",register_notification,name="registration"),
path("receipt/",register_receipt,name="registration"),
path("loan/",register_loan,name="registration"),
path("reward/",register_reward,name="registration"),

path("customers/",views.list_customers,name="customers_list"),
path("currencys/",views.list_currencys,name="currencys_list"),
path("wallets/",views.list_wallet,name="wallets_list"),
path("transactions/",views.list_transaction,name="transactions_list"),
path("cards/",views.list_cards,name="cards_list"),
path("third_partys/",views.list_third_party,name="third_partys_list"),
path("notifications/",views.list_notifications,name="notofications_list"),
path("receipts/",views.list_receipts,name="receipts_list"),
path("loans/",views.loans_list,name="loans_list"),
path("rewards/",views.reward_list,name="rewards_list"),
path("accounts/",views.accounts_list,name="accounts_list")


path("customers/<int::id>/",customer_profile,name="customer_profile")
path(customers/edit/<int::id/",edit_customer,name="edit_customer">)













]