from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
from django.db.models import Q


class SearchProductView(ListView):
    template_name="search/view.html"

    def get_context_data(self, *args, **kwargs):
        context=super(SearchProductView,self).get_context_data(*args,**kwargs)
        query=self.request.GET.get('q')
        context['query']=query
        #SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self,*args,**kwargs):
        request=self.request
        method_dict=request.GET
        query=method_dict.get('q',None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()


# def SearchProductView(request,*args,**kwargs):
#     method_dict=request.GET
#     query=method_dict.get('q',None)
#     print(query)
#     if query is not None:
#         return Product.objects.filter(title__icontains=query)
#     return Product.objects.all()
#     context={
#         'get_queryset':get_queryset
#     }
#
#     return render(request,"search/view.html", context)
