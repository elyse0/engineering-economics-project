from django.urls import path
from home.views import *

urlpatterns = [

    path('', HomeView.as_view()),
    path('valor-futuro-cantidad-presente', ValorFuturoCantidadPresenteView.as_view()),
    path('valor-presente-cantidad-futura', ValorPresenteCantidadFuturaView.as_view()),
    path('serie-uniforme-equivalente-presente', SerieUniformeEquivalentePresenteView.as_view()),
    path('valor-presente-serie-uniforme', ValorPresenteSerieUniformeView.as_view()),
    path('serie-uniforme-equivalente-futuro', SerieUniformeEquivalenteFuturoView.as_view()),
    path('valor-futuro-serie-uniforme', ValorFuturoSerieUniformeView.as_view()),
    path('valor-presente-equivalente-gradiente', ValorPresenteEquivalenteGradienteView.as_view()),
    path('valor-presente-equivalente-total-gradiente', ValorPresenteEquivalenteTotalGradienteView.as_view()),
    path('serie-anual-equivalente-gradiente', SerieAnualEquivalenteGradienteView.as_view()),
    path('serie-uniforme-equivalente-total-gradiente', SerieUniformeEquivalenteTotalGradienteView.as_view()),
]