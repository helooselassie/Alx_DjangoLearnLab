from django.contrib.auth import get_user_model  # Use get_user_model()

def list_users(request):
    User = get_user_model()  # Get the custom user model dynamically
    users = User.objects.all()  # Update this line to use User variable
    return render(request, 'users.html', {'users': users})