from django.http import JsonResponse
from django.utils.decorators import method_decorator
from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
