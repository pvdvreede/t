from django.views.generic import *
from t.transactions.functions import run_rules
from t.transactions.models import *
from t.transactions.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect 

class BaseDeleteView(View):
    model=None
    success_url=None
    action_message="Items deleted!"
    
    def get_success_url(self):
        return self.success_url
    
    def post(self, request):
        self.model.objects.filter(user=request.user).filter(id__in=request.POST.getlist("ids")).delete()     
        messages.success(self.request, self.action_message)        
        return HttpResponseRedirect(self.get_success_url())        

class UserBaseCreateView(CreateView):  
    action_message = "Item created!"
    
    def get_context_data(self, **kwargs):
        context = super(UserBaseCreateView, self).get_context_data(**kwargs)
        context["cancel_url"] = self.success_url
        return context
    
    def form_valid(self, form):
        value = super(UserBaseCreateView, self).form_valid(form)
        messages.success(self.request, self.action_message)
        return value

    def get_form_kwargs(self):
        kwargs = super(UserBaseCreateView, self).get_form_kwargs()
        kwargs.update({ "user" : self.request.user })
        return kwargs
    
class UserBaseUpdateView(UpdateView):
    action_message = "Item updated!"

    def get_context_data(self, **kwargs):
        context = super(UserBaseUpdateView, self).get_context_data(**kwargs)
        context["cancel_url"] = self.success_url
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).filter(id=self.kwargs.get('pk', None))

    def form_valid(self, form):
        value = super(UserBaseUpdateView, self).form_valid(form)
        messages.success(self.request, self.action_message)
        return value

    def get_form_kwargs(self):
        kwargs = super(UserBaseUpdateView, self).get_form_kwargs()
        kwargs.update({ "user" : self.request.user })
        return kwargs



class TransactionActionView(View):
    def post(self, request):
	if request.POST["action"] == "delete":
	  Transaction.objects.filter(user=request.user).filter(id__in=request.POST.getlist("ids")).delete()
	  messages.success(self.request, "Items deleted!")
	elif request.POST["action"] == "category":
	  Transaction.objects.filter(user=request.user).filter(id__in=request.POST.getlist("ids")).update(category=request.POST["category"])
	  messages.success(self.request, "Items updated!")
	
	return HttpResponseRedirect("/transaction") 
      
class TransactionsListView(ListView):
    model=Transaction
    template_name="transaction_list.html" 
    paginate_by=20
     
    def get_queryset(self):
        objects = Transaction.objects.filter(user=self.request.user)
        if self.request.GET.__contains__("account"):
            objects = objects.filter(account__in=self.request.GET.getlist("account"))
        if self.request.GET.__contains__("category"):
            objects = objects.filter(category__in=self.request.GET.getlist("category"))
        objects = objects.order_by("-date")
        return objects
     
    def get_context_data(self, **kwargs):
        context = super(TransactionsListView, self).get_context_data(**kwargs)
        if self.request.GET.__contains__("account"):
            context["selected_accounts"] = self.request.GET.getlist("account")
        if self.request.GET.__contains__("category"):
            context["selected_categories"] = self.request.GET.getlist("category")
        context["accounts"] = Account.objects.filter(user=self.request.user)
        context["categories"] = Category.objects.filter(user=self.request.user)
        return context
        
class TransactionCreateView(UserBaseCreateView):
    model=Transaction
    template_name="transaction_form.html"
    form_class=TransactionForm
    success_url="/transaction"   
    
class TransactionUpdateView(UserBaseUpdateView):
    model=Transaction
    template_name="transaction_form.html"
    form_class=TransactionForm
    success_url="/transaction"

class TransactionDeleteView(BaseDeleteView):
    model=Transaction
    success_url="/transaction"



class CategoryListView(ListView):
    model=Category
    template_name="category_list.html"
    paginate_by=15
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
class CategoryCreateView(UserBaseCreateView):
    model=Category
    template_name="category_form.html"
    form_class=CategoryForm  
    success_url="/category"
    
class CategoryUpdateView(UserBaseUpdateView):
    model=Category
    template_name="category_form.html"
    form_class=CategoryForm
    success_url="/category"

class CategoryDeleteView(BaseDeleteView):
    model=Category
    success_url="/category"

class RuleRunView(RedirectView):
    url="/rule"

    def get(self, request, *args, **kwargs):
        import t.transactions.functions
        run_rules(request.user.id)
        messages.success(self.request, 'Transactions have been updated!')
        return super(RuleRunView, self).get(request, *args, **kwargs)
    
class RuleListView(ListView):
    model=Rule
    template_name="rule_list.html"
    paginate_by=15

    def get_queryset(self):
        return Rule.objects.filter(user=self.request.user)

class RuleCreateView(UserBaseCreateView):
    model=Rule
    template_name="rule_form.html"
    form_class=RuleForm
    success_url="/rule"

class RuleUpdateView(UserBaseUpdateView):
    model=Rule
    template_name="rule_form.html"
    form_class=RuleForm
    success_url="/rule"

class RuleDeleteView(BaseDeleteView):
    model=Rule
    success_url="/rule"



class AccountListView(ListView):
    model=Account
    template_name="account_list.html"
    paginate_by=15
    
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
   
class AccountCreateView(UserBaseCreateView):
    model=Account
    template_name="account_form.html"
    form_class=AccountForm
    success_url="/account"
    
class AccountUpdateView(UserBaseUpdateView):
    model=Account
    template_name="account_form.html"
    form_class=AccountForm
    success_url="/account"
    
class AccountDeleteView(BaseDeleteView):
    model=Account
    success_url="/account"