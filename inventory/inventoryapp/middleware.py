from django.shortcuts import redirect
from django.http import HttpResponse

class SpecificUserAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            if request.user.username != 'meat' and request.path.startswith("/meats_list/"):
                return HttpResponse("Forbidden Access")
            
            if request.user.username == 'meat' and not request.path.startswith("/meats_list/") and not request.path.startswith("/logout/"):
                return redirect("/meats_list/")
                
        return self.get_response(request)
