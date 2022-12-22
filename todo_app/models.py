from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

#to use functions in the same module classes we define 
#functions on top of the class 
def on_week_hence():
    return timezone.now() +timezone.timedelta(days=7) 



class ToDoList (models.Model):
    title =models.CharField(("Title"), max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    
    


    
class ToDoItem (models.Model):
    title = models.CharField(("Title"), max_length=100)
    description = models.TextField(("Description"))
    create_date= models.DateTimeField(("Created At"), auto_now_add=True)
    due_date = models.DateField(("Due Date"),default=on_week_hence)
    todo_list= models.ForeignKey("ToDoList",related_name="items" ,verbose_name=("Item's List"), on_delete=models.CASCADE)
    
    class Meta:
        ordering=["due_date"]
    
    def __str__(self) -> str:
        return f"{self.title} : due {self.due_date}"
    
    #here we pass two args because the item is shown on item-update view
    # which has a url as list/<int:list_id>/item/<int:item_id>
    #so we have two arguments list_id ,and item_id
    def get_absolute_url(self):       
        return reverse("item-update", args=[str(self.todo_list.id),str(self.id)])

    


    

