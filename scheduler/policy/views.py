from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view(['GET'])
def privacy_policy(request):
    '''
    render privacy policy page
    '''
    return render(request, 'privacy_policy.html')

@api_view(['GET'])
def data_deletion(request):
    '''
    render data deletion policy page
    '''
    return render(request, 'data_deletion.html')

@api_view(['GET'])
def terms_service(request):
    '''
    render term of service page
    '''
    return render(request, 'terms_service.html')

