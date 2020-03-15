from rest_framework import routers
from agenda.views import AgendaViewSet
from especialidade.views import EspecialidadeViewSet 
from medico.views import MedicoViewSet 
from consulta.views import ConsultaViewSet


router = routers.DefaultRouter()
router.register(r'agendas', AgendaViewSet)
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultas', ConsultaViewSet)