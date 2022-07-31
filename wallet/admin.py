from django.contrib import admin
from .models import Account, Card, Third_party
from .models import Customer
from .models import Wallet
from .models import Transaction
from .models import Notification
from .models import Third_party
from .models import Receipt
from .models import Loan
from .models import Reward









class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Third_party)




# Register your models here.
