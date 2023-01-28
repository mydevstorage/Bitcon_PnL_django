from django.shortcuts import redirect
from .models import *
from .services import *
from datetime import datetime
from django.views.generic import FormView
from django.views.generic.list import ListView
from .forms import IndexForm


class IndexView(FormView, ListView):
    '''Контроллер обработки основной страницы'''
    model = PnlIndex
    template_name = "pnl_index/index.html"
    context_object_name = 'index_data'
    form_class = IndexForm

    def get_queryset(self): 
        '''Получение последней записи'''
        queryset = super().get_queryset()
        return queryset.last()

    def get_context_data(self, **kwargs):
        '''Добавление дополнительных данных в шаблон'''
        object_end = PnlIndex.objects.last()
        object_start = PnlIndex.objects.first()
        context = super().get_context_data(**kwargs)
        context['profit_in_percent'] = period_profit_in_percent(object_start,
                                                                object_end)
        context['period'] = (f'{object_start.created.strftime("%d.%m.%Y [%H:%M]")}'
                             f' - {datetime.now().strftime("%d.%m.%Y [%H:%M]")}')
        return context


    def form_valid(self, form):
        '''Получение, обработка данных из формы'''
        CustomPeriod.create_custom_record(form.cleaned_data)
        return redirect('pnl_index:custom')



class CustomPeriodView(FormView, ListView):
    '''Дополнительный контроллер для обработки запроса кастомного периода'''
    model = CustomPeriod
    template_name = "pnl_index/index.html"
    context_object_name = 'index_data'
    form_class = IndexForm

    def get_queryset(self): 
        queryset = super().get_queryset()
        return queryset.last()

    





