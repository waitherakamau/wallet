from django.contrib import admin
from .models import Account, Card
from .models import Customer
from .models import Wallet
from .models import Transaction
from .models import Notification
from .models import Third_party
from .models import Receipt
from .models import Loan
from .models import Reward
from .models import Currency









class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)

class AccountAdmin(admin.ModelAdmin):
      list_display=('account_number','account_type','account_balance','account_name',)
      search_fields=('account_number','account_type','account_balance','account_name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_ref','wallet','receipt',)
    search_fields=('transaction_ref','wallet','receipt',)

class CardAdmin(admin.ModelAdmin):
      list_display=('card_number','card_type','card_name',)
      search_fields=('card_number','card_type','card_name',)


class Third_partyAdmin(admin.ModelAdmin):
    list_display=('currency','location','name',)
    search_fields=('currency','location','name',)

class NotificationAdmin(admin.ModelAdmin):
      list_display=('name','transaction_Id','date_time',)
      search_fields=('name','transaction_Id','date_time',)

class LoanAdmin(admin.ModelAdmin):
    list_display=('payment_due_date','guarantor','loan_term',)
    search_fields=('payment_due_date','guarantor','loan_term',)

class RewardAdmin(admin.ModelAdmin):
      list_display=('points','gender','date_time',)
      search_fields=('points','gender','date_time',)


class CurrencyAdmin(admin.ModelAdmin):
      list_display=('origin','amount',)
      search_fields=('origin','amount',)

class WalletAdmin(admin.ModelAdmin):
      list_display=('balance','customer','time',)
      search_fields=('balance','customer','time',)



class ReceiptAdmin(admin.ModelAdmin):
      list_display=('receipt_type','bill_number','date',)
      search_fields=('receipt_type','bill_number','date',)

 

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Third_party,Third_partyAdmin)
admin.site.register(Currency,CurrencyAdmin)




# Register your models here.
