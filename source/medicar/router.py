from rest_framework import routers
from agenda.views import AgendaViewSet
from especialidade.views import EspecialidadeViewSet 
from medico.views import MedicoViewSet 
from consulta.views import ConsultaViewSet


router = routers.DefaultRouter()
router.register(r'agenda', AgendaViewSet)
router.register(r'especialidade', EspecialidadeViewSet)
router.register(r'medico', MedicoViewSet)
router.register(r'consulta', ConsultaViewSet)