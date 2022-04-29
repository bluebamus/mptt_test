from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Category

class CategoryView(View):
    template_name = 'mptt_test2.html'
    def get(self, request):
        context = {'categories': Category.objects.all()}

        return render(request, self.template_name, context)