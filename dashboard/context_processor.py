from home.models import Team_Setting_Config

def website_setting(request):
    website_settings = Team_Setting_Config.objects.get(setting_no=1)
    return {'website_settings': website_settings}

