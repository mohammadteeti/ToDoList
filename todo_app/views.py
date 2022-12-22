from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from todo_app.models import ToDoItem,ToDoList
from .forms import DeleteForm
# Create your views here.

class ListListView(ListView):
    model=ToDoList
    template_name="todo/index.html"
    
    # #redundant context
    # #get_context_data merges the context of all parent classes
    # #with the context of the current class 
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "To Do List!"
    #     return context
    
    
    
class ItemListView(ListView):
    
    #no need to specify the model here as it's 
    #specified in the get_queryset() method  below
    #if we don't override get_query_set 
    #then we must add model=... as the default query set 
    #deependes on it in retreiving all objects from database
    model=ToDoItem
    
    #we can  either abandon this or add a specific tamplate name
    #if abandoned ,the default template name should be of the form
    #modelname_list.html ,where modelname is lowercase
    template_name="todo/todo_list.html"
    
    
    #override queryset so that it retrieves only the items 
    #related to the List with list_id 
    #list_id is extracted from url args as a kwarg of key "list_id"
    #list_id was passed to the request through url <int:list_id>
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    
    #after setting the queryset above we should append 
    #the corrosponding List id to the new template that 
    #views all it's related items , we do taht 
    #by overriding the context data and add new key,value 
    #pair to the context (we didi the same as in queryset in
    # retrieving the list_id from the url kwargs)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #below line means : get the List of id = List_id got from url <int:list_id>
        #and appedn to the context as todo_list
        context["todo_list"]=ToDoList.objects.get(id=self.kwargs["list_id"])
        return context #know the context contais values from 
                     #parent class (listview) which are things like pagination,pages, object_list
                     #as well as values add (todo_list)
        
        #note that we can leave the context as is without overriding 
        #but we did so because the logic of the app requires to know
        #what list those items follow
        
        #get_context_data merges all contexts from all parents 
        #along with the current class contexts



#a class to create new List
class ListCreate(CreateView):
    model=ToDoList
    #success_url=reverse_lazy("list",args=[id])
    fields=["title",]
    template_name="todo/todolist_form.html"


#a class to create new Item 
class ItemCreate(CreateView):
    model=ToDoItem
    fields=[
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    
    template_name="todo/item_form.html"
    
    def get_initial(self):
        initial_data=super().get_initial()
        #we must use "get" instead of "filter" as filter returns a group 
        #while get returns a single element 
        #even if the group contains one element it still a group
        #and won't initialize todo_list field 
        # see https://stackoverflow.com/questions/42899919/django-queryset-and-filter-vs-get
        initial_data["todo_list"]=ToDoList.objects.get(id=self.kwargs["list_id"])
        return initial_data
    
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        #always watch for get ,use get not filter for single objects 
        #very important to remember that filter returns a queryset 
        #while "get" returns one object
        context["todo_list"]=ToDoList.objects.get(id=self.kwargs["list_id"])
        context["title"]="Item Create"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list",args=[self.kwargs["list_id"]])



class ItemUpdate(UpdateView):
    model=ToDoItem
    fields=[
         "todo_list",
         "title",
         "description",
         "due_date",
    ]
     
    template_name="todo/item_form.html"
     

    
    def get_context_data(self, **kwargs):
         context=super(ItemUpdate,self).get_context_data(**kwargs)
         #always watch for get ,use get not filter for single objects 
         #very important to remember that filter returns a queryset 
         #while "get" returns one object
         context["todo_list"]=ToDoList.objects.get(id=self.kwargs["list_id"])
         context["title"]="Item Update"
         return context
    def get_success_url(self) -> str:
         return reverse("list",args=[self.kwargs["list_id"]])
     
     
     
def ItemDelete(request,list_id,pk):
    
    item=ToDoItem.objects.get(id=pk)
    
    if request.method=="POST":
        data=request.POST["delete"]
        if data =="Yes":
            item.delete()
        
        return redirect(reverse("list",args=[list_id]))
        
    return render(request,"todo/item-delete.html",{"item":item})


    
        
    