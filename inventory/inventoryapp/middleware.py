from django.shortcuts import redirect
from django.http import HttpResponse

class SpecificUserAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
                
            user_profile = request.user.userprofile
            is_supplier = user_profile.is_supplier
            path = request.path

            if path.startswith('/media/'):
                return self.get_response(request)

            if is_supplier:
                if not (path.startswith("/products_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/products_list/")

        return self.get_response(request)
