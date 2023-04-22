from django.urls import path

from . import views

urlpatterns = [
    # path('move_list/', views.move_list, name='move_list'),
    path('move_list/', views.MoveList.as_view(), name='move_list'),
    # path('move_form/', views.move_form, name='move_form'),
    path('move_form/', views.MoveCreate.as_view(), name='move_form'),
    # path('move_edit/<int:move_id>', views.move_edit, name='move_edit'),
    path('move_edit/<int:pk>', views.MoveUpdate.as_view(), name='move_edit'),
    # path('move_delete/<int:move_id>', views.move_delete, name='move_delete'),
    path('move_delete/<int:pk>', views.MoveDelete.as_view(), name='move_delete'),

    path('movemasterdetail/', views.MoveMasterDetailView.as_view(), name='move_master_detail_form'),
    path('movemasterdetaillist/<int:pk>', views.MoveMasterDetailUpdateView.as_view(), name='move_master_detail_list'),


    # account_move_line
    #
    path('line_list/', views.move_line_list, name='move_line_list'),

]
