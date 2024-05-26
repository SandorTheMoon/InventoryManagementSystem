from django.shortcuts import redirect
from django.http import HttpResponse

class SpecificUserAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            path = request.path

            if username == 'meat':
                if not (path.startswith("/meats_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/meats_list/")
            elif username == 'baked':
                if not (path.startswith("/baked_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/baked_list/")
            elif username == 'dairy':
                if not (path.startswith("/dairy_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/dairy_list/")
            elif username == 'plants':
                if not (path.startswith("/plants_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/plants_list/")
            elif username == 'condiments':
                if not (path.startswith("/condiments_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/condiments_list/")
            elif username == 'beverages':
                if not (path.startswith("/beverages_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/beverages_list/")
            elif username == 'dry':
                if not (path.startswith("/dry_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/dry_list/")
            elif username == 'packaging':
                if not (path.startswith("/packaging_list/") or
                        path.startswith("/generate_po/") or
                        path.startswith("/my_generated_po/") or
                        path.startswith("/my_generated_po_details/") or
                        path.startswith("/logout/")):
                    return redirect("/packaging_list/")
            else:
                # If the user does not match any specific username
                restricted_paths = [
                    "/meats_list/", "/baked_list/", "/dairy_list/",
                    "/plants_list/", "/condiments_list/", "/beverages_list/",
                    "/dry_list/", "/packaging_list/", "/generate_po/",
                    "/my_generated_po/", "/my_generated_po_details/"
                ]
                if any(path.startswith(p) for p in restricted_paths):
                    return HttpResponse("Forbidden Access")

        return self.get_response(request)
