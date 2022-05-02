from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Category

class CategoryView(View):
    template_name = 'tracer/category.html'
    def get(self, request, slug):
        context = {'categories': Category.objects.all()}
        # print('context : ',context.values())
        # dict=context.values()
        # for i in dict :
        #     print('i : ',i.values())
        return render(request, self.template_name, context)