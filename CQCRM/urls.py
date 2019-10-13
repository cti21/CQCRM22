"""CQCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from backend.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'invoice_dict',viewset=invoice_dictViewSet,base_name='invoice_dict')
router.register(r'jinjizheng',viewset=jinjizhengViewSet,base_name='jinjizheng')
router.register(r'profit_distri_dict',viewset=profit_distri_dictViewSet,base_name='profit_distri_dict')
router.register(r'invoice_set',viewset=invoice_setViewSet,base_name='invoice_set')
router.register(r'coo_hospital',viewset=coo_hospitalViewSet,base_name='coo_hospital')
router.register(r'dept_dict',viewset=dept_dictViewSet,base_name='dept_dict')
router.register(r'post_dict',viewset=post_dictViewSet,base_name='post_dict')
router.register(r'project_dict',viewset=project_dictViewSet,base_name='project_dict')
router.register(r'project_dict_child',viewset=project_dictChildViewSet,base_name='project_dict_child')
router.register(r'project_dict_individual',viewset=project_dict_individualViewSet,base_name='project_dict_individual')
router.register(r'dept',viewset=deptViewSet,base_name='dept')
router.register(r'tuition_fee',viewset=tuitionFeeViewSet,base_name='tuition_fee')
router.register(r'tuitionfee_detail',viewset=tuitionFee_detailViewSet,base_name='tuitionfee_detail')
router.register(r'huiyuan_set',viewset=huiyuan_setViewSet,base_name='huiyuan_set')
router.register(r'project',viewset=projectViewSet,base_name='project')
router.register(r'project_child',viewset=project_ChildViewSet,base_name='project_child')
router.register(r'project_individual',viewset=project_individualViewSet,base_name='project_individual')
router.register(r'dept_post',viewset=dept_postViewSet,base_name='dept_post')
router.register(r'project_jinjizheng',viewset=project_jinjizhengViewSet,base_name='project_jinjizheng')
router.register(r'performance_dict',viewset=performance_dictViewSet,base_name='performance_dict')
router.register(r'benefit_dict',viewset=benefit_dictViewSet,base_name='benefit_dict')
router.register(r'finance_month',viewset=finance_monthViewSet,base_name='finance_month')
router.register(r'performance',viewset=performanceViewSet,base_name='performance')
router.register(r'benefit',viewset=benefitViewSet,base_name='benefit')
router.register(r'Company',viewset=HrmCompanyViewSet,base_name='Company')
router.register(r'subComSelect',viewset=subCompanyViewSet,base_name='subComSelect')
router.register(r'SubCompany',viewset=HrmSubCompanyViewSet,base_name='SubCompany')
router.register(r'subCompanyField',viewset=subCompanyFieldViewSet,base_name='subCompanyField')
router.register(r'department',viewset=HrmDepartmentViewSet,base_name='department')
router.register(r'userProfile',viewset=userProfileViewSet,base_name='userProfile')
router.register(r'client',viewset=clientViewSet,base_name='client')
router.register(r'dept_client_type',viewset=dept_client_typeViewSet,base_name='dept_client_type')
router.register(r'client_register',viewset=client_registerViewSet,base_name='client_register')
router.register(r'order',viewset=orderViewSet,base_name='order')
router.register(r'treat',viewset=treatViewSet,base_name='treat')
router.register(r'treat_history',viewset=treat_historyViewSet,base_name='treat_history')
router.register(r'treat_detail',viewset=treat_detailViewSet,base_name='treat_detail')
router.register(r'callback',viewset=callbackViewSet,base_name='callback')
router.register(r'survey',viewset=surveyViewSet,base_name='survey')
router.register(r'survey_title',viewset=survey_titleViewSet,base_name='survey_title')
router.register(r'treat_survey',viewset=treat_surveyViewSet,base_name='treat_survey')

# API_V1=[]
# API_V1.extend(router.urls)
# API_VERSIONS = [url(r'^v1/', include(API_V1))]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(API_VERSIONS)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('backend.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'docs/', include_docs_urls(title='我的API', authentication_classes=[], permission_classes=[])),
    # 创建排班基础数据
    # url(r'^api/createschedule/', ScheduleOddViewSet.as_view({'get': 'createschedule'})),
    # url(r'^api/createdayschedule/', ScheduleOddViewSet.as_view({'get': 'createdayschedule'})),
    # url(r'^patient_txtype/', patient_txtype, name='patient_txtype'),
    # url(r'^upload/', FileUploadView.as_view()),
    # url(r'^silk/',include('silk.urls', namespace='silk')),
]
