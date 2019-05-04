from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from home.forms import *

# Create your views here.

class HomeView (TemplateView):

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class ValorFuturoCantidadPresenteView (TemplateView):

    getTemplate = 'ecuacion.1.get.html'
    postTemplate = 'ecuacion.1.post.html'

    def get(self, request):

        valorPresente = ValorPresenteForm()
        interes = InteresForm()
        numeroPeriodos = NumeroPeriodosForm()
        tipoPeriodos = TipoPeriodosForm()
        return render(request, self.getTemplate,
                      {'interes': interes, 'valorPresente': valorPresente,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos})

    def post(self, request):

        valorPresente = ValorPresenteForm(request.POST)
        interes = InteresForm(request.POST)
        numeroPeriodos = NumeroPeriodosForm(request.POST)
        tipoPeriodos = TipoPeriodosForm(request.POST)
        periodos = []

        for x in range(int(numeroPeriodos['numeroPeriodos'].value()) + 1):
            periodos.append(str(x))

        for x in periodos:
            print(periodos)
            print(x)

        return render(request, self.postTemplate,
                      {'interes': interes, 'valorPresente': valorPresente,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos,
                       'stringTipoPeriodos': tipoPeriodos['tipoPeriodos'].value(),
                       'stringNumeroPeriodos': numeroPeriodos['numeroPeriodos'].value(),
                       'stringValorPresente': valorPresente['valorPresente'].value(),
                       'stringValorInteres': interes['interes'].value()})


class ValorPresenteCantidadFuturaView (TemplateView):

    getTemplate = 'ecuacion.2.get.html'
    postTemplate = 'ecuacion.2.post.html'

    def get(self, request):

        valorFuturo = ValorFuturoForm()
        interes = InteresForm()
        numeroPeriodos = NumeroPeriodosForm()
        tipoPeriodos = TipoPeriodosForm()
        return render(request, self.getTemplate,
                      {'interes': interes, 'valorFuturo': valorFuturo,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos})

    def post(self, request):

        valorFuturo = ValorFuturoForm(request.POST)
        interes = InteresForm(request.POST)
        numeroPeriodos = NumeroPeriodosForm(request.POST)
        tipoPeriodos = TipoPeriodosForm(request.POST)
        periodos = []

        for x in range(int(numeroPeriodos['numeroPeriodos'].value()) + 1):
            periodos.append(str(x))

        for x in periodos:
            print(periodos)
            print(x)

        return render(request, self.postTemplate,
                      {'interes': interes, 'valorFuturo': valorFuturo,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos,
                       'stringTipoPeriodos': tipoPeriodos['tipoPeriodos'].value(),
                       'stringNumeroPeriodos': numeroPeriodos['numeroPeriodos'].value(),
                       'stringValorFuturo': valorFuturo['valorFuturo'].value(),
                       'stringValorInteres': interes['interes'].value()})

class SerieUniformeEquivalentePresenteView (TemplateView):

    template_name = 'ecuacion.3.get.html'

    def get(self, request):
        return render(request, self.template_name)


class ValorPresenteSerieUniformeView (TemplateView):

    template_name = 'ecuacion.4.get.html'

    def get(self, request):
        return render(request, self.template_name)


class SerieUniformeEquivalenteFuturoView (TemplateView):

    template_name = 'ecuacion.5.get.html'

    def get(self, request):
        return render(request, self.template_name)


class ValorFuturoSerieUniformeView (TemplateView):

    template_name = 'ecuacion.6.get.html'

    def get(self, request):
        return render(request, self.template_name)


class ValorPresenteEquivalenteGradienteView (TemplateView):

    template_name = 'ecuacion.7.get.html'

    def get(self, request):
        return render(request, self.template_name)


class ValorPresenteEquivalenteTotalGradienteView (TemplateView):

    template_name = 'ecuacion.8.get.html'

    def get(self, request):
        return render(request, self.template_name)


class SerieAnualEquivalenteGradienteView (TemplateView):

    template_name = 'ecuacion.9.get.html'

    def get(self, request):
        return render(request, self.template_name)


class SerieUniformeEquivalenteTotalGradienteView (TemplateView):

    template_name = 'ecuacion.10.get.html'

    def get(self, request):
        return render(request, self.template_name)