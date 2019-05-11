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

    getTemplate = 'ecuacion.3.get.html'
    postTemplate = 'ecuacion.3.post.html'

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


class ValorPresenteSerieUniformeView (TemplateView):

    getTemplate = 'ecuacion.4.get.html'
    postTemplate = 'ecuacion.4.post.html'

    def get(self, request):
        valorSerie = ValorSerieForm()
        interes = InteresForm()
        numeroPeriodos = NumeroPeriodosForm()
        tipoPeriodos = TipoPeriodosForm()
        return render(request, self.getTemplate,
                      {'interes': interes, 'valorSerie': valorSerie,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos})

    def post(self, request):

        valorSerie = ValorSerieForm(request.POST)
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
                      {'interes': interes, 'valorSerie': valorSerie,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos,
                       'stringTipoPeriodos': tipoPeriodos['tipoPeriodos'].value(),
                       'stringNumeroPeriodos': numeroPeriodos['numeroPeriodos'].value(),
                       'stringValorSerie': valorSerie['valorSerie'].value(),
                       'stringValorInteres': interes['interes'].value()})


class SerieUniformeEquivalenteFuturoView (TemplateView):

    getTemplate = 'ecuacion.5.get.html'
    postTemplate = 'ecuacion.5.post.html'

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



class ValorFuturoSerieUniformeView (TemplateView):

    getTemplate = 'ecuacion.6.get.html'
    postTemplate = 'ecuacion.6.post.html'

    def get(self, request):
        valorSerie = ValorSerieForm()
        interes = InteresForm()
        numeroPeriodos = NumeroPeriodosForm()
        tipoPeriodos = TipoPeriodosForm()
        return render(request, self.getTemplate,
                      {'interes': interes, 'valorSerie': valorSerie,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos})

    def post(self, request):

        valorSerie = ValorSerieForm(request.POST)
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
                      {'interes': interes, 'valorSerie': valorSerie,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos,
                       'stringTipoPeriodos': tipoPeriodos['tipoPeriodos'].value(),
                       'stringNumeroPeriodos': numeroPeriodos['numeroPeriodos'].value(),
                       'stringValorSerie': valorSerie['valorSerie'].value(),
                       'stringValorInteres': interes['interes'].value()})


class ValorPresenteEquivalenteGradienteView (TemplateView):

    getTemplate = 'ecuacion.7.get.html'
    postTemplate = 'ecuacion.7.post.html'

    def get(self, request):
        valorInicial = ValorInicialForm()
        valorGradiente = ValorGradienteForm()
        interes = InteresForm()
        numeroPeriodos = NumeroPeriodosForm()
        tipoPeriodos = TipoPeriodosForm()
        return render(request, self.getTemplate,
                      {'interes': interes, 'valorGradiente': valorGradiente, 'valorInicial': valorInicial,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos})

    def post(self, request):

        valorInicial = ValorInicialForm(request.POST)
        valorGradiente = ValorGradienteForm(request.POST)
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
                      {'interes': interes, 'valorGradiente': valorGradiente, 'valorInicial': valorInicial,
                       'numeroPeriodos': numeroPeriodos, 'tipoPeriodos': tipoPeriodos,
                       'stringTipoPeriodos': tipoPeriodos['tipoPeriodos'].value(),
                       'stringNumeroPeriodos': numeroPeriodos['numeroPeriodos'].value(),
                       'stringValorInicial': valorInicial['valorInicial'].value(),
                       'stringValorGradiente': valorGradiente['valorGradiente'].value(),
                       'stringValorInteres': interes['interes'].value()})


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