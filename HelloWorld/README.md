# Hello world

- Add the module

    ```python
    from django.http import HttpResponse
    ```

- Define in urls.py in urlpatterns

    ```python
    path('hello-world/', hello_world)
    ```

- Define the function hello_world in urls.py (only for this example)

    ```python
    def hello_world(request):
    	return HttpResponse('Hello world!')
    ```
