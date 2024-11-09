# search/views.py
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from pathlib import Path

class UserSearchView(View):
    def get(self, request):
        # Get search query from request parameters
        query = request.GET.get("query", "").lower()
        
        # Load data from JSON file
        data_path = Path(__file__).resolve().parent / "data" / "data.json"
        with open(data_path, 'r') as file:
            users = json.load(file)
        
        # Filter users based on search query
        results = [
            user for user in users 
            if query in user['first_name'].lower() or query in user['last_name'].lower()
        ]
        
        # If no results, return an empty response
        if not results:
            return JsonResponse({"results": []}, status=200)
        
        # Otherwise, return filtered user data
        return JsonResponse({"results": results}, safe=False)
