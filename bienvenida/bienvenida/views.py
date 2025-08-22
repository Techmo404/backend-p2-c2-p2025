from django.http import HttpResponse
def inicio(request):
    return HttpResponse("Hola mundo desde Django")
def monstrar_bienvenida(request):
    tu_nombre = "Benjamin Miranda"
    return HttpResponse(f"Bienvenido rey, {tu_nombre}")