from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.views import View


def get_external_post(request, post_id):
    # The external URL you want to fetch data from
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    # 1. Make the GET request to the external API
    response = requests.get(url)

    # 2. Check if the request was successful
    if response.status_code == 200:
        # Transform the raw text response into a Python dictionary
        data = response.json()

        # 3. Return the data from your own Django endpoint
        return JsonResponse(data, status=200)

    # Handle failure if the external server drops or errors out
    return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)


class ExternalPostView(View):
    # This method automatically handles HTTP GET requests
    def get(self, request, post_id):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        print("Here is the response object:", response)

        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, status=200)

        return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)


class ExternalPostCommentsView(View):

    def get(self, request, post_id):

        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, status=200, safe=False)

        return JsonResponse(data={"error": "Failed to fetch data"}, status=response.status_code)



