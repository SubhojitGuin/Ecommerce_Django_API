from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentsAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'amount', 'payment_status')
  list_filter = ('payment_status', 'created_at')
  search_fields = ('id', 'user__email')
  readonly_fields = ('id', 'user', 'amount', 'payment_status')
  list_per_page = 20

  def user(self, obj):
    return obj.order.user.first_name + ' ' + obj.order.user.last_name
  user.short_description = 'User'

  def has_delete_permission(self, request, obj=None):
    return False

  # def has_view_permission(self, request, obj=None):
  #   return False

  def has_change_permission(self, request, obj=None):
    return False
  
  def has_add_permission(self, request):
    return False

admin.site.register(Payment, PaymentsAdmin)