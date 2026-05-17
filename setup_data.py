import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskAssign.settings')
django.setup()

from main.models import User, Task

def setup_data():
    # Create or update admin user
    admin_user, created = User.objects.get_or_create(username='admin')
    admin_user.set_password('adminpassword123')
    admin_user.is_superuser = True
    admin_user.is_staff = True
    admin_user.is_active = True
    admin_user.save()
    print("Admin user created/updated.")

    # Create or get user bharat
    bharat, _ = User.objects.get_or_create(username='bharat')
    bharat.set_password('password123')
    bharat.is_active = True
    bharat.save()
    print("User 'bharat' created/updated.")

    # Create or get user likhith
    likhith, _ = User.objects.get_or_create(username='likhith')
    likhith.set_password('password123')
    likhith.is_active = True
    likhith.save()
    print("User 'likhith' created/updated.")

    # Create task 1
    task1, _ = Task.objects.get_or_create(title='task 1', defaults={'description': 'Task 1 description'})
    task1.assignees.set([bharat])
    task1.save()
    print("Task 'task 1' created and assigned to bharat.")

    # Create task 2
    task2, _ = Task.objects.get_or_create(title='task 2', defaults={'description': 'Task 2 description'})
    task2.assignees.set([bharat, likhith])
    task2.save()
    print("Task 'task 2' created and assigned to bharat and likhith.")

if __name__ == '__main__':
    setup_data()
