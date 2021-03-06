from django.contrib.auth.models import User
from django.db.models import Q

class CaseInsensitiveAuth:
    
    def authenticate(self, username=None, password=None):
    
        users = User.objects.filter(Q(username__iexact=username) |
                                    Q(email__iexact=username))
        if not users:
            return None
            
        user = users[0]
        if user.check_password(password):
            return user
        return None
        
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None