from django.template.defaulttags import url
from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ticket Support API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('endpoints/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('create-ticket/', CreateTicket.as_view()),
    path('tickets/', TicketsList.as_view(), name='tickets'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket'),
    path('tickets/<str:status>/', TicketsStatusList.as_view(), name='status_tickets'),
    path('ticket-change-status/<int:pk>/', TicketChange.as_view(), name='ticket-change-status'),
    path('ticket-replies/<int:pk>/', TicketReply.as_view(), name='create_reply'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
