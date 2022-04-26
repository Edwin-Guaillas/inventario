from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SistemaConfig(AppConfig):
    name = 'sistema'



class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'