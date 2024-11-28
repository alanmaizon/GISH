from orders.models import User

# Create a new staff user
staff_user = User.objects.create_user(
    username="staff_user",
    email="staff@example.com",
    password="securepassword123"
)
staff_user.is_staff = True  # Grant staff privileges
staff_user.save()

print(f"Staff user {staff_user.username} created successfully.")
