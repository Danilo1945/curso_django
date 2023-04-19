from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='account_list'),
    # path('edit/<int:move_id>', views.edit, name='account_edit'),
    # path('form/', views.form, name='account_form'),
    # path('delete/<int:move_id>', views.delete, name='account_delete'),

]
