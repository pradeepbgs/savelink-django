from django.http import JsonResponse
from link.models import Link
from django.views.decorators.csrf import csrf_exempt 
import json
from django.core.paginator import Paginator
from decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required
@csrf_exempt
def create_link(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        
        title = data.get('title')
        link = data.get('link')
        tags = data.get('tags')

        if not link:
            return JsonResponse({'success': False, 'error':'pls provide link'},status=400)
        
        post = Link(
            link=link,
            user=request.user,
            title=title,
            tags=tags
        )

        post.save()
        
        return JsonResponse({'success': True, 'message': 'Link created successfully','link':link}, status=201)


    else:
        return JsonResponse({'success': False, 'error':'method is not allowed'},status=405)

@login_required
@csrf_exempt
def get_user_links(request):
    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        query = request.GET.get('query')
        links_per_page = 10
     
        user_links = Link.objects.filter(user=request.user).order_by('-created_at')

        if query:
            user_links = user_links.filter(
               Q(title__icontains=query) | Q(tags__icontains=query)
            )
            
        paginator = Paginator(user_links, links_per_page)

        try:
            page = paginator.page(page_number)
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Invalid page number'}, status=400)
     
        links_data = [
            {
                'id': link.id, 
                'title': link.title, 
                'link': link.link, 
                'tags': link.tags,
                'created_at':link.created_at
            } 
            for link in page
        ]
     
        return JsonResponse({
            'success': True,
            'data': links_data,
            'page': page.number,
            'total_pages': paginator.num_pages
        })

    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)


@login_required
@csrf_exempt
def delete_link(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        link_id = data.get('link_id')  # Retrieve link_id from URL parameters

        if not link_id:
            return JsonResponse({'success': False,'error': 'Link ID not provided'}, status=400)

        if not link_id:
            return JsonResponse({'success': False, 'error': 'Link ID not provided'}, status=400)

        link = Link.objects.filter(user=request.user, id=link_id)

        if not link.exists():
            return JsonResponse({'success': False, 'error': 'Link not found'}, status=404)

        link.delete()

        return JsonResponse({'success': True, 'message': 'Link deleted successfully'}, status=200)

    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

@csrf_exempt
def health(request):
    if request.method == 'GET':
        return JsonResponse({'success': True, 'msg':"everything is ok"})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
