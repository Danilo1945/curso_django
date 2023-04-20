from django.urls import path

from . import views

urlpatterns = [
    path('move_list/', views.move_list, name='move_list'),
    path('line_list/', views.move_line_list, name='move_line_list'),
    # path('edit/<int:move_id>', views.edit, name='account_edit'),
    # path('form/', views.form, name='account_form'),
    # path('delete/<int:move_id>', views.delete, name='account_delete'),

]
