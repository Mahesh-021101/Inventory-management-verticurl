from django.contrib.admin.decorators import register
from django.urls import path
from . import views

urlpatterns = [
path('', views.Login, name='Login'),
    path('Login/',views.Login,name='Login'),
    path('Admin_Dashboard/',views.Admin_Dashboard,name='Admin_Dashboard'),
    path('newEmployee/',views.newEmployee,name='newEmployee'),
    path('editEmployee/<str:pk>/',views.editEmployee,name='editEmployee'),
    path('newSupplier/',views.newSupplier,name='newSupplier'),
    path('editSupplier/<str:pk>/',views.editSupplier,name='editSupplier'),
    path('newStock/', views.newStock, name='newStock'),
    path('editAsset/<str:pk>/', views.editAsset, name='editAsset'),
    path('editConsumable/<str:pk>/', views.editConsumable, name='editConsumable'),
    path('newScrap/', views.newScrap, name='newScrap'),
    path('editScrap/<str:pk>/', views.editScrap, name='editScrap'),
    path('newService/', views.newService, name='newService'),
    path('newWarranty/', views.newWarranty, name='newWarranty'),
    path('allocationApproval/', views.allocationApproval, name='allocationApproval'),
    path('depreciationApproval/', views.depreciationApproval, name='depreciationApproval'),
    path('editDepreciation/<str:pk>/', views.editDepreciation, name='editDepreciation'),
    path('loader/<str:pk>/<str:dp>', views.loader, name='loader'),
    path('a_no/<str:pk>/', views.a_no, name='a_no'),
    path('a_allow/<str:pk>/', views.a_allow, name='a_allow'),
    path('req/<str:pk>/', views.req, name='req'),
    path('rap/<str:pk>/', views.rap, name='rap'),
    path('newAllocator/', views.newAllocator, name='newAllocator'),
    path('stock/', views.stock, name='stock'),
    path('viewStock/<str:pk>/', views.viewStock, name='viewStock'),
    path('employee/', views.employee, name='employee'),
    path('viewEmployee/<str:pk>/', views.viewEmployee, name='viewEmployee'),
    path('supplier/', views.supplier, name='supplier'),
    path('viewSupplier/<str:pk>/', views.viewSupplier, name='viewSupplier'),
    path('allocate/', views.allocate, name='allocate'),
    path('deallocate/', views.deallocate, name='deallocate'),
    path('addStock/', views.addStock, name='addStock'),
    path('viewConsumable/<str:pk>/', views.viewConsumable, name='viewConsumable'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('allocator_dashboard/', views.allocator_dashboard, name='allocator_dashboard'),
    path('allocation_history/', views.allocation_history, name='allocation_history'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('request/', views.request, name='request'),
    path('change_password/', views.change_password, name='change_password'),    path('a_allocate/', views.a_allocate, name='a_allocate'),
    path('a_deallocate/', views.a_deallocate, name='a_deallocate'),
    path('a_view_stock/', views.a_view_stock, name='a_view_stock'),
    path('chart_allocation/', views.chart_allocation, name='chart_allocation'),
    path('chart_overall/', views.chart_overall, name='chart_overall'),
    path('overallInventory/', views.overallInventory, name='overallInventory'),
    path('rasset/', views.rasset, name='rasset'),
    path('rscrap/', views.rscrap, name='rscrap'),
    path('rconsumable/', views.rconsumable, name='rconsumable'),
    path('bulk/', views.bulk, name='bulk'),
    path('logout/', views.logoutview, name='logout'),

]

