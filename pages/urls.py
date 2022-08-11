from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AboutView, EmployersCreate, EmployersDelete, EmployersList, EmployersUpdate, IndexView, NeighborhoodsCreate, NeighborhoodsDelete, NeighborhoodsList, NeighborhoodsUpdate, TransactionsCreate, TransactionsDelete, TransactionsList, TransactionsUpdate, UserCreate

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('about/', AboutView.as_view(), name='about'),
  path('login/', auth_views.LoginView.as_view(template_name='pages/form-login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('register/', UserCreate.as_view(), name='register'),
  path('neighborhoods/', NeighborhoodsList.as_view(), name='neighborhoods'),
  path('neighborhoods/create/', NeighborhoodsCreate.as_view(), name='create-neighborhood'),
  path('neighborhoods/update/<int:pk>', NeighborhoodsUpdate.as_view(), name='update-neighborhood'),
  path('neighborhoods/delete/<int:pk>', NeighborhoodsDelete.as_view(), name='delete-neighborhood'),
  path('employers/', EmployersList.as_view(), name='employers'),
  path('employers/create/', EmployersCreate.as_view(), name='create-employer'),
  path('employers/update/<int:pk>', EmployersUpdate.as_view(), name='update-employer'),
  path('employers/delete/<int:pk>', EmployersDelete.as_view(), name='delete-employer'),
  path('transactions/', TransactionsList.as_view(), name='transactions'),
  path('transactions/create/', TransactionsCreate.as_view(), name='create-transaction'),
  path('transactions/update/<int:pk>', TransactionsUpdate.as_view(), name='update-transaction'),
  path('transactions/delete/<int:pk>', TransactionsDelete.as_view(), name='delete-transaction'),
]
