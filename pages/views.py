from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.forms import UserForm
from pages.models import Employer, Neighborhood, Transaction

# Create your views here.
class IndexView(TemplateView):
  template_name = 'pages/index.html'
  
class AboutView(TemplateView):
  template_name = 'pages/about.html'
  
# SELECT
  
class NeighborhoodsList(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  model = Neighborhood
  template_name = 'pages/neighborhoods.html'
  paginate_by = 10
  
  def get_queryset(self):
    txt_name = self.request.GET.get('nome')
    
    if txt_name:
      neighborhoods = Neighborhood.objects.filter(nome__icontains=txt_name)
    else: 
      neighborhoods = Neighborhood.objects.all()
      
    return neighborhoods
  
class EmployersList(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  model = Employer
  template_name = 'pages/employers.html'
  paginate_by = 10
  
  def get_queryset(self):
    txt_name = self.request.GET.get('nome')
    
    if txt_name:
      employers = Employer.objects.filter(nome__icontains=txt_name)
    else: 
      employers = Employer.objects.all()
      
    return employers
  
class TransactionsList(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  model = Transaction
  template_name = 'pages/transactions.html'
  paginate_by = 10  
  
  def get_queryset(self):
    txt_description = self.request.GET.get('descricao')
    
    if txt_description:
      transactions = Transaction.objects.filter(descricao__icontains=txt_description)
    else: 
      transactions = Transaction.objects.all()
      
    return transactions
  
# CREATE

class UserCreate(CreateView):
  form_class = UserForm
  template_name = 'pages/form.html'
  success_url = reverse_lazy('login')
  
class NeighborhoodsCreate(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('login')
  model = Neighborhood
  fields =  ['nome', 'populacao']
  template_name = 'pages/form.html'
  success_url = reverse_lazy('neighborhoods')
  
class EmployersCreate(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('login')
  model = Employer
  fields =  ['cpf', 'nome', 'sobrenome', 'data_nascimento', 'uf', 'cargo', 'salario']
  template_name = 'pages/form.html'
  success_url = reverse_lazy('employers')
  
class TransactionsCreate(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('login')
  model = Transaction
  fields =  ['descricao', 'valor', 'tipo', 'usuario', 'comprovante']
  template_name = 'pages/form-upload.html'
  success_url = reverse_lazy('transactions')
  
# EDIT
  
class NeighborhoodsUpdate(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('login')
  model = Neighborhood
  fields =  ['nome', 'populacao']
  template_name = 'pages/form.html'
  success_url = reverse_lazy('neighborhoods')
  
class EmployersUpdate(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('login')
  model = Employer
  fields =  ['cpf', 'nome', 'sobrenome', 'data_nascimento', 'uf', 'cargo', 'salario']
  template_name = 'pages/form.html'
  success_url = reverse_lazy('employers')
  
class TransactionsUpdate(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('login')
  model = Transaction
  fields =  ['descricao', 'valor', 'tipo', 'usuario', 'comprovante']
  template_name = 'pages/form-upload.html'
  success_url = reverse_lazy('transactions')
  
# DELETE
  
class NeighborhoodsDelete(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('login')
  model = Neighborhood
  template_name = 'pages/form-delete.html'
  success_url = reverse_lazy('neighborhoods')
  
class EmployersDelete(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('login')
  model = Employer
  template_name = 'pages/form-delete.html'
  success_url = reverse_lazy('employers')
    
class TransactionsDelete(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('login')
  model = Transaction
  template_name = 'pages/form-delete.html'
  success_url = reverse_lazy('transactions')