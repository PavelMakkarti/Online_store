from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Product
from .filters import ProductFilter


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'
        paginate_by = 2

        # Переопределяем функцию получения списка товаров
        def get_queryset(self):
            # Получаем обычный запрос
            queryset = super().get_queryset()
            # Используем наш класс фильтрации.
            # self.request.GET содержит объект QueryDict, который мы рассматривали
            # в этом юните ранее.
            # Сохраняем нашу фильтрацию в объекте класса,
            # чтобы потом добавить в контекст и использовать в шаблоне.
            self.filterset = ProductFilter(self.request.GET, queryset)
            # Возвращаем из функции отфильтрованный список товаров
            return self.filterset.qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # Добавляем в контекст объект фильтрации.
            context['filterset'] = self.filterset
            return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'

