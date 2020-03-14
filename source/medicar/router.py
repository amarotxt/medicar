from rest_framework import routers
from source.agenda.views import AgendaViewSet
from source.especialidade.views import EspecialidadeViewSet 
from source.medico.views import MedicoViewSet 

router = routers.DefaultRouter()
router.register(r'agenda', AgendaViewSet)
router.register(r'especialidade', EspecialidadeViewSet)
router.register(r'medico', MedicoViewSet)