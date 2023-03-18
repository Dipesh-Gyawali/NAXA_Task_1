import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project

@csrf_exempt
def upload_projects(request):
    if request.method == 'POST':
        # Read the file from the request
        file = request.FILES['file']
        
        # Parse the data from the file
        data = pd.read_excel(file)
        
        # Validate the data
        # Here, you can add your own validation logic to ensure that the data conforms to your expected format
        
        # Connect to the database
        # Assuming that you have already set up your database settings in the settings.py file
        # and that you have already created a Project model in models.py
        # You can use Django's built-in ORM to insert the data into the database
        for i, row in data.iterrows():
            project = Project.objects.create(
                name=row['name'],
                description=row['description'],
                start_date=row['start_date'],
                end_date=row['end_date']
                # Add more fields as necessary
            )
            project.save()
        
        # Return a success response
        return JsonResponse({'message': 'Projects uploaded successfully.'})
    else:
        # Return a bad request response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
