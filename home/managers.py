from django.contrib.auth.base_user import BaseUserManager

class BaseManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_field):
        user = self.model(username=username, email=email, **extra_field)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_field):
        user = self.create_user(username=username, email=email, password=password, **extra_field)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_varified = True
        user.save(using = self._db)
        return user