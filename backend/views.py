from django.shortcuts import render
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework import viewsets
from rest_framework.decorators import list_route,detail_route
from backend.models import *
from rest_framework.response import Response
from backend.serializers import *
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters
# from backend.filters import ProductFilter,Tx_planFilter,Tx_drugFilter,RegisterFilter,Yz_touxiFilter
from rest_framework.pagination import PageNumberPagination
from django.utils.timezone import now,timedelta,datetime
import datetime
import decimal,json
from django.db import connection
from django.http import JsonResponse,HttpResponse
from django.db.models import F,Q
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from pyexcel_xlsx import  get_data
from rest_framework import status

# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    去除 CSRF 检查
    """
    def enforce_csrf(self, request):
        return

class CommentPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10

class GeneralPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 8

class LargePagination(PageNumberPagination):
    page_size = 10000
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10000

class expensePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10

class invoice_dictViewSet(viewsets.ModelViewSet):
    """
    发票字典
    """
    queryset = invoice_dict.objects.all()
    serializer_class = invoice_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

class profit_distri_dictViewSet(viewsets.ModelViewSet):
    """
    发票字典
    """
    queryset = profit_distri_dict.objects.all()
    serializer_class = profit_distri_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

class jinjizhengViewSet(viewsets.ModelViewSet):
    """
    禁忌症字典
    """
    queryset = jinjizheng.objects.all()
    serializer_class = jinjizhengSerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)

class coo_hospitalViewSet(viewsets.ModelViewSet):
    """
    合作医院
    """
    queryset = coo_hospital.objects.all()
    serializer_class = coo_hospitalSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return coo_hospitalDetailSerializer
        else:
            return coo_hospitalSerializer

    def get_queryset(self):
        queryset = coo_hospital.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name__contains=name)
            return queryset
        else:
            return queryset

class invoice_setViewSet(viewsets.ModelViewSet):
    """
    开票设置
    """
    serializer_class = invoice_setSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = invoice_set.objects.all()
        if self.action == 'list':
            hospitalid = self.request.query_params.get('hospital_id')
            if hospitalid:
                queryset = queryset.filter(hospital_id__exact=hospitalid)
            return queryset.order_by('-begindate')
        else:
            return queryset

class HrmCompanyViewSet(viewsets.ModelViewSet):
    """
    公司
    """
    queryset = HrmCompany.objects.all()
    serializer_class = HrmCompanySerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

class dept_dictViewSet(viewsets.ModelViewSet):
    """
    公司科室字典
    """
    serializer_class = dept_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = dept_dict.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name__contains=name)
            return queryset
        else:
            return queryset

class post_dictViewSet(viewsets.ModelViewSet):
    """
    公司岗位字典
    """
    serializer_class = post_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = post_dict.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name__contains=name)
            return queryset
        else:
            return queryset

class project_dictViewSet(viewsets.ModelViewSet):
    """
    公司项目字典(包括单项及套餐)
    """
    serializer_class = project_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if self.action == 'list':
            queryset = project_dict.objects.filter(parent__isnull=True)
            name = self.request.query_params.get('name')
            isindependent = self.request.query_params.get('isindependent')
            if name:
                queryset = queryset.filter(name__contains=name)
            if isindependent:
                queryset = queryset.filter(isindependent=1)
            return queryset
        else:
            queryset = project_dict.objects.all()
            return queryset

class project_dictChildViewSet(viewsets.ModelViewSet):
    """
    套餐子项目字典
    """
    serializer_class = project_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = project_dict.objects.all()
        if self.action == 'list':
            parentid = self.request.query_params.get('parentid')
            queryset = queryset.filter(parent_id__exact=parentid)
            return queryset
        else:
            return queryset

class project_dict_individualViewSet(viewsets.ModelViewSet):
    """
    项目字典中之不能开单的单项
    """
    serializer_class = project_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = project_dict.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(parent__isnull=True,type__exact=0,isindependent=0)
            return queryset
        else:
            return queryset

class performance_dictViewSet(viewsets.ModelViewSet):
    """
    公司绩效字典
    """
    serializer_class = performance_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = performance_dict.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name__contains=name)
            return queryset
        else:
            return queryset

class benefit_dictViewSet(viewsets.ModelViewSet):
    """
    公司工资福利字典
    """
    serializer_class = benefit_dictSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = benefit_dict.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name__contains=name)
            return queryset
        else:
            return queryset

class dept_postViewSet(viewsets.ModelViewSet):
    """
    科室岗位
    """
    serializer_class = dept_postSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = dept_post.objects.all()
        if self.action == 'list':
            deptdict_id = self.request.query_params.get('name')
            if deptdict_id:
                queryset = queryset.filter(deptdict_id__exact=deptdict_id)
            return queryset
        else:
            return queryset

class project_jinjizhengViewSet(viewsets.ModelViewSet):
    """
    项目禁忌症
    """
    serializer_class = project_jinjizhengSerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = project_jinjizheng.objects.all()
        if self.action == 'list':
            projectdict_id = self.request.query_params.get('projectdict_id')
            if projectdict_id:
                queryset = queryset.filter(projectdict_id__exact=projectdict_id)
            return queryset
        else:
            return queryset

class deptViewSet(viewsets.ModelViewSet):
    """
    中心科室
    """
    serializer_class = deptSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = dept.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            return queryset

class tuitionFeeViewSet(viewsets.ModelViewSet):
    """
    中心带教费
    """
    serializer_class = tuitionFeeSerializer
    pagination_class = CommentPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = tuitionFee.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            return queryset

class tuitionFee_detailViewSet(viewsets.ModelViewSet):
    """
    中心带教费详细
    """
    serializer_class = tuitionFee_detailSerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = tuitionFee_detail.objects.all()
        if self.action == 'list':
            tuitionfee_id = self.request.query_params.get('name')
            queryset = queryset.filter(tuitionfee_id__exact=tuitionfee_id)
            return queryset
        else:
            return queryset

class projectViewSet(viewsets.ModelViewSet):
    """
    中心项目
    """
    serializer_class = projectSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if self.action == 'list':
            queryset = project.objects.filter(parent__isnull=True)
            hrmdepartment_id = self.request.query_params.get('name')
            register_id = self.request.query_params.get('register_id')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            queryset = project.objects.all()
            return queryset

class project_ChildViewSet(viewsets.ModelViewSet):
    """
    中心套餐子项目
    """
    serializer_class = projectSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        hrmdepartment_id = self.request.query_params.get('hrmdepartment_id')
        queryset = project.objects.all()
        if self.action == 'list':
            parentid = self.request.query_params.get('parentid')
            queryset = queryset.filter(hrmdepartment_id=hrmdepartment_id)
            queryset = queryset.filter(parent_id__exact=parentid)
            return queryset
        else:
            return queryset

class project_individualViewSet(viewsets.ModelViewSet):
    """
    中心项目中之项目(包括单项及套餐，不含中心自定义套餐)
    """
    serializer_class = projectSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = project.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            queryset = queryset.filter(hrmdepartment_id=hrmdepartment_id,parent__isnull=True)
            return queryset
        else:
            return queryset

class finance_monthViewSet(viewsets.ModelViewSet):
    """
    财务月
    """
    serializer_class = finance_monthSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = finance_month.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            return queryset

class performanceViewSet(viewsets.ModelViewSet):
    """
    中心绩效
    """
    serializer_class = performanceSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = performance.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            return queryset

class benefitViewSet(viewsets.ModelViewSet):
    """
    中心工资福利
    """
    serializer_class = benefitSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = benefit.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('name')
            if hrmdepartment_id:
                queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            return queryset
        else:
            return queryset

class huiyuan_setViewSet(viewsets.ModelViewSet):
    """
    回院设置
    """
    queryset = huiyuan_set.objects.all()
    serializer_class = huiyuan_setSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = huiyuan_set.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(projectdict__name__contains=name)
            return queryset
        else:
            return queryset


class subCompanyViewSet(viewsets.ModelViewSet):
    """
    公司分部select
    """
    queryset = HrmSubCompany.objects.all()
    serializer_class = HrmSubCompanySerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)


class HrmSubCompanyViewSet(viewsets.ModelViewSet):
    """
    公司分部
    """
    serializer_class = HrmSubCompanySerializer
    pagination_class = CommentPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = HrmSubCompany.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            code = self.request.query_params.get('code')
            kind = self.request.query_params.get('kind')
            if name:
                queryset = queryset.filter(name__contains=name)
            if kind == 'info':
                queryset = queryset.filter(code__exact=code)
            else:
                queryset = queryset.filter(code__startswith=code).filter(~Q(code=code))
            return queryset.order_by('showorder')
        else:
            return queryset

class subCompanyFieldViewSet(viewsets.ModelViewSet):
    """
    公司分部自定义
    """
    queryset = subCompanyField.objects.all()
    serializer_class = subCompanyFieldSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

class HrmDepartmentViewSet(viewsets.ModelViewSet):
    """
    公司部门
    """
    serializer_class = HrmDepartmentSerializer
    pagination_class = CommentPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = HrmDepartment.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            code = self.request.query_params.get('code')
            kind = self.request.query_params.get('kind')
            if name:
                queryset = queryset.filter(name__contains=name)
            if code:
                if kind == 'sub':
                    queryset = queryset.filter(code__startswith=code).filter(~Q(code=code))
                elif kind == 'dep':
                    queryset = queryset.filter(code__startswith=code)
                else:
                    queryset = queryset.filter(code__exact=code)
            return queryset.order_by('showorder')
        else:
            return queryset

class userProfileViewSet(viewsets.ModelViewSet):
    """
    员工档案
    """
    serializer_class = userProfileSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = userProfile.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('hrmdepartment_id')
            name = self.request.query_params.get('name')
            queryset = queryset.filter(hrmdepartment_id__exact=hrmdepartment_id)
            if name:
                queryset = queryset.filter(Q(name__contains=name) | Q(phone1__contains=name)
                                           | Q(phone2__contains=name))
            return queryset
        else:
            return queryset


    def create(self, request, *args, **kwargs):

        employeeData = request.data
        userobj = User.objects.order_by('-id').first()
        username = 'st' + str(userobj.id).zfill(4)
        email = username + '@126.com'

        user = User.objects.create_user(
            # username=employeeData['username'],
            # email='toma@126.com',
            username=username,
            email=email,
            first_name=employeeData['name'],
            last_name=employeeData['name']
        )
        user.set_password('123qweasd')
        obj = user.save()
        employeeData['user'] = user.id
        serializer = self.get_serializer(data=employeeData)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class clientViewSet(viewsets.ModelViewSet):
    """
    客户档案
    """
    serializer_class = clientSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = client.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            clientid = self.request.query_params.get('clientid')
            if name:
                queryset = queryset.filter(name__contains=name)
            if clientid:
                queryset = queryset.filter(pk=clientid)
            return queryset
        else:
            return queryset

class client_registerViewSet(viewsets.ModelViewSet):
    """
    客户登记
    """
    serializer_class = client_registerSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = client_register.objects.all()
        if self.action == 'list':
            clientid = self.request.query_params.get('clientid')
            name = self.request.query_params.get('name')
            clienttype = self.request.query_params.get('clienttype')
            indate = self.request.query_params.get('indate')

            if clientid:
                queryset = queryset.filter(client_id__exact=clientid)

            if name:
                queryset = queryset.filter(Q(client__name__contains=name) |
                                           Q(client__phone1__contains=name) |
                                           Q(client__phone2__contains=name))
            if clienttype:
                queryset = queryset.filter(client_type=clienttype)

            if indate:
                registerDate = datetime.datetime.strptime(indate, '%Y-%m-%d')
                queryset = queryset.filter(registerdate__year=registerDate.year,registerdate__month=registerDate.month,
                                           registerdate__day=registerDate.day)

            return queryset.order_by('-registerdate')
        else:
            return queryset

class dept_client_typeViewSet(viewsets.ModelViewSet):
    """
    科室对应的客户类型
    """
    serializer_class = dept_client_typeSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = dept_client_type.objects.all()
        if self.action == 'list':
            dept_id = self.request.query_params.get('dept_id')
            dept_obj = dept.objects.filter(id=dept_id).first()
            queryset = queryset.filter(deptdict=dept_obj.deptdict)
            return queryset
        else:
            return queryset

class orderViewSet(viewsets.ModelViewSet):
    """
    宣教开单
    """
    serializer_class = orderSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = order.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('hrmdepartment_id')
            begindate = self.request.query_params.get('begindate')
            enddate = self.request.query_params.get('enddate')
            clientname = self.request.query_params.get('clientname')
            issuccess = self.request.query_params.get('issuccess')
            isacquire = self.request.query_params.get('isacquire')
            isproorder = self.request.query_params.get('isproorder')
            project = self.request.query_params.get('project')
            orderuser = self.request.query_params.get('orderuser')
            marketuser = self.request.query_params.get('marketuser')
            clientid = self.request.query_params.get('clientid')
            queryset = queryset.filter(hrmdepartment_id=hrmdepartment_id,parent__isnull=True)

            if clientid:
                queryset = queryset.filter(client_id=clientid)

            if begindate:
                if enddate:
                    queryset = queryset.filter(marketdate__range=(begindate,enddate))
                else:
                    queryset = queryset.filter(marketdate__gte=begindate)
            else:
                if enddate:
                    queryset = queryset.filter(marketdate__lte=enddate)

            if clientname:
                queryset = queryset.filter(client__name__contains=clientname)

            if issuccess:
                queryset = queryset.filter(issuccess=issuccess)

            if isacquire:
                queryset = queryset.filter(isacquire=isacquire)

            if isproorder:
                queryset = queryset.filter(isproorder=isproorder)

            if project:
                queryset = queryset.filter(project__id=project)

            if orderuser:
                queryset = queryset.filter(adduser__id=orderuser)

            if marketuser:
                queryset = queryset.filter(marketman__id=marketuser)

            return queryset.order_by('-marketdate')
        else:
            return queryset

class treatViewSet(viewsets.ModelViewSet):
    """
    检查治疗
    """
    serializer_class = treatSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = treat.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('hrmdepartment_id')
            clientid = self.request.query_params.get('clientid')
            clientname = self.request.query_params.get('clientname')
            phone = self.request.query_params.get('phone')
            begindate = self.request.query_params.get('begindate')
            enddate = self.request.query_params.get('enddate')
            project = self.request.query_params.get('project')
            isacquire = self.request.query_params.get('isacquire')
            residue = self.request.query_params.get('residue')
            todaytreated = self.request.query_params.get('todaytreated')
            queryset = queryset.filter(hrmdepartment_id=hrmdepartment_id,parent__isnull=True)
            if residue == 'true':
                residue = 1
            elif residue == 'false':
                residue = 0
            else:
                residue = ''

            if todaytreated == 'true':
                todaytreated = 1
            elif todaytreated == 'false':
                todaytreated = 0
            else:
                todaytreated = ''

            if clientid:
                queryset = queryset.filter(client_id=clientid)

            q1 = treat.objects.filter(hrmdepartment_id=hrmdepartment_id, parent__isnull=True)
            q2 = treat.objects.filter(hrmdepartment_id=hrmdepartment_id, parent__isnull=False)
            if begindate:
                if enddate:
                    q = q1.filter(operatedate__range=(begindate,enddate))
                    ids = q2.filter(operatedate__range=(begindate,enddate)).values('parent_id')
                    queryset = queryset.filter(id__in=ids) | q
                else:
                    q = q1.filter(operatedate__gte=begindate)
                    ids = q2.filter(operatedate__gte=begindate).values('parent_id')
                    queryset = queryset.filter(id__in=ids) | q
            else:
                if enddate:
                    q = q1.filter(operatedate__lte=enddate)
                    ids = q2.filter(operatedate__lte=enddate).values('parent_id')
                    queryset = queryset.filter(id__in=ids) | q

            if clientname:
                queryset = queryset.filter(client__name__contains=clientname)

            if phone:
                queryset = queryset.filter(client__phone1__contains=phone)

            if isacquire:
                queryset = queryset.filter(isacquire=isacquire)

            if residue:
                q_residue = q1.filter(residue=0)
                ids = q2.filter(residue=0).values('parent_id')
                queryset = queryset.filter(id__in=ids) | q_residue

            if project:
                q_project = q1.filter(project__name=project)
                ids = q2.filter(project__name=project).values('parent_id')
                queryset = queryset.filter(id__in=ids) | q_project

            if todaytreated:
                q_today = q1.filter(operatedate__year=now().year,operatedate__month=now().month,operatedate__day=now().day)
                ids = q2.filter(operatedate__year=now().year,operatedate__month=now().month,operatedate__day=now().day)\
                    .values('parent_id')
                queryset = queryset.filter(id__in=ids) | q_today

            return queryset.order_by('-operatedate','client_id')
        else:
            return queryset

    def destroy(self, request, *args, **kwargs):
        action = request.data.get('action')
        instance = self.get_object()

        if action == 1: # 单项的治疗记录删除
            par_treatobj = treat.objects.filter(pk=instance.parent_id).first()
            par_treatobj.residue = par_treatobj.residue + instance.amount

            exsists = treat.objects.filter(parent=instance.parent)
            if len(exsists) == 1:
                par_treatobj.treattype = 0

            par_treatobj.save()
            treat.objects.filter(pk=instance.id).delete()

        elif action == 2: # 套餐的子项删除
            operatedate = self.request.data.get('operatedate')
            exsists = treat.objects.filter(parent=instance,operatedate__exact=operatedate)
            for item in exsists:
                subs = treat.objects.filter(parent=instance,project=item.project)
                if len(subs) == 1:
                    obj = subs.first()
                    obj.residue = obj.residue + obj.amount
                    obj.amount = 0
                    obj.operatedate = None
                    obj.operator = None
                    obj.treatdept = None
                    obj.treattype = 0
                    obj.save()
                    instance.operatedate = None
                    instance.operator_id = None
                    instance.save()
                else:
                    obj = treat.objects.filter(parent=instance,project=item.project).\
                        exclude(pk=item.id).order_by('operatedate').first()
                    if obj:
                        obj.residue = obj.residue + obj.amount
                        obj.save()
                    treat.objects.filter(pk=item.id).delete()

        else:
            treat.objects.filter(pk=instance.id).delete()

        return Response('')


class treat_detailViewSet(viewsets.ModelViewSet):
    """
    单条治疗记录
    """
    serializer_class = treatSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = treat.objects.all()
        if self.action == 'list':
            treat_id = self.request.query_params.get('treat_id')
            queryset = queryset.filter(pk=treat_id)
            return queryset
        else:
            return queryset

class treat_historyViewSet(viewsets.ModelViewSet):
    """
    检查治疗历史记录
    """
    serializer_class = treat_historySerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = treat.objects.all()
        if self.action == 'list':
            project_id = self.request.query_params.get('project_id')
            treat_id = self.request.query_params.get('treat_id')
            projectobj = project.objects.filter(id=project_id).first()
            type = projectobj.type
            if type == True:
                queryset = queryset.filter(parent_id=treat_id,operatedate__isnull=False).\
                    order_by('parent__project_id','operatedate')
            else:
                queryset = queryset.filter(parent_id=treat_id,operatedate__isnull=False).order_by('operatedate')
            return queryset
        else:
            return queryset

class callbackViewSet(viewsets.ModelViewSet):
    """
    回访记录
    """
    serializer_class = callbackSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = callback.objects.all()
        if self.action == 'list':
            hrmdepartment_id = self.request.query_params.get('hrmdepartment_id')
            queryset = queryset.filter(hrmdepartment_id=hrmdepartment_id)
            order_id = self.request.query_params.get('order_id')
            begindate = self.request.query_params.get('begindate')
            enddate = self.request.query_params.get('enddate')
            project = self.request.query_params.get('project')
            hfuser = self.request.query_params.get('handleman')
            clientname = self.request.query_params.get('name')
            isfinish = self.request.query_params.get('isfinish')
            callbacktype = self.request.query_params.get('callbacktype')
            ishospital = self.request.query_params.get('ishospital')
            todaycallback = self.request.query_params.get('todaycallback')

            if order_id:
                queryset = queryset.filter(order_id=order_id)

            if project:
                queryset = queryset.filter(treat__project_id__exact=project)

            if clientname:
                queryset = queryset.filter(client__name__contains=clientname)

            if hfuser:
                queryset = queryset.filter(handleman_id__exact=hfuser)

            if isfinish:
                queryset = queryset.filter(isfinish=isfinish)

            if callbacktype:
                queryset = queryset.filter(callbacktype=callbacktype)

            if ishospital:
                queryset = queryset.filter(ishospital=ishospital)

            if todaycallback == 'true':
                queryset = queryset.filter(begindate__lte=date.today(),enddate__lte=date.today())

            if begindate:
                if enddate:
                    queryset = queryset.filter(handledate__range=(begindate,enddate))
                else:
                    queryset = queryset.filter(handledate__gte=begindate)
            else:
                if enddate:
                    queryset = queryset.filter(handledate__lte=enddate)

            return queryset
        else:
            return queryset

class surveyViewSet(viewsets.ModelViewSet):
    """
    问卷字典
    """
    queryset = survey.objects.all()
    serializer_class = surveySerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)


class survey_titleViewSet(viewsets.ModelViewSet):
    """
    问卷题目选项
    """
    queryset = survey_title.objects.all()
    serializer_class = survey_titleSerializer
    pagination_class = LargePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = survey_title.objects.all()
        if self.action == 'list':
            survey_id = self.request.query_params.get('survey_id')
            queryset = queryset.filter(survey_id=survey_id)
            return queryset
        else:
            return queryset


class treat_surveyViewSet(viewsets.ModelViewSet):
    """
    治疗所需问卷
    """
    queryset = treat_survey.objects.all()
    serializer_class = treat_surveySerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
#  开单页面的下拉框(操作人员,项目)数据
def getOrderSelectData(request):
    data = {}
    hrmdepartment_id = request.query_params.get('hrmdepartment_id')
    users = userProfile.objects.filter(hrmdepartment_id=hrmdepartment_id).values('id','name')
    data['users'] = list(users)
    projects = project.objects.filter(hrmdepartment_id=hrmdepartment_id,isindependent=1).values('id','name')
    data['projects'] = list(projects)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getAllSelectData(request):
    data = {}
    clienttype = client_type.objects.values('id','name')
    data['clienttype'] = list(clienttype)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


# 返回套餐的最晚历史治疗记录
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getTcTreatHistroryData(request):
    data = {}
    treat_id = request.query_params.get('treat_id')
    ids = treat.objects.filter(parent_id=treat_id).values('project_id').annotate(max_id=Max('id')).values('max_id')
    tchistorys = treat.objects.filter(parent_id=treat_id).filter(id__in=ids).\
        values('id','project__name','times','residue','amount')
    data['tchistorys'] = list(tchistorys)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

class LogViewSet(viewsets.ModelViewSet):
    """
    操作日志
    """
    serializer_class = APIRequestLogSerializer
    pagination_class = expensePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = APIRequestLog.objects.all()
        if self.action == 'list':
            name = self.request.query_params.get('name')
            if name is not None:
                queryset = queryset.filter(user__username__contains=name)
            return queryset.order_by('-requested_at')
        else:
            return queryset

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# 返回历史治疗记录
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def treat_histrorys(request):
    data = {}
    treat_id = request.query_params.get('treat_id')
    type = request.query_params.get('type')
    cursor = connection.cursor()

    if type == '1':
        cursor.execute('select a.id,b.operatedate,(SELECT name from backend_userprofile '
        ' where id=a.adduser_id) orderuser,(SELECT name from backend_project where id=a.project_id) projectname'
        ',a.isacquire,a.times, a.residue,a.amount, 1 as type,a.comment,'
        ' (SELECT d.name from backend_dept c, backend_dept_dict d where c.deptdict_id=d.id '
        ' and c.id=b.treatdept_id) treatdeptname,b.treatdept_id,(SELECT name from backend_userprofile where id=b.operator_id) '
        'operatename,b.operator_id from backend_treat a  LEFT JOIN (select DISTINCT parent_id,operatedate,treatdept_id,operator_id '
        'from backend_treat) b ON a.id = b.parent_id where  a.id=%s',[treat_id])
    else:
        cursor.execute('select id,operatedate,(SELECT name from backend_userprofile where id=adduser_id) '
        ' orderuser,(SELECT name from backend_project where id=project_id) projectname,isacquire,times,'
        ' residue,amount, 0 as type,comment,(SELECT d.name from backend_dept c, backend_dept_dict d where c.deptdict_id=d.id and '
        ' c.id=treatdept_id) treatdeptname,treatdept_id,(SELECT name from backend_userprofile where id=operator_id) '
        ' operatename,operator_id from backend_treat where parent_id=%s',[treat_id])

    row = dictfetchall(cursor)
    return JsonResponse(row, safe=False, json_dumps_params={'ensure_ascii': False})

# 返回套餐的子项历史治疗记录
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def treat_subhistorys(request):
    data = {}
    treat_id = request.query_params.get('treat_id')
    operatedate = request.query_params.get('operatedate')

    cursor = connection.cursor()
    cursor.execute('SELECT id,(SELECT name from backend_project where id=backend_treat.project_id) '
                   ' project__name,project_id,times,residue,amount from backend_treat '
                   ' where parent_id=%s and operatedate=%s', [treat_id,operatedate])
    row = dictfetchall(cursor)

    return JsonResponse(row, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def info(request):
    token = request.query_params.get('token')
    ustr = jwt_decode_handler(token)
    user = User.objects.get(username=ustr['username'])

    role = user.groups.all().values_list('id')
    queryset = GroupChildMenu.objects.filter(groupmenu__group_id__in=role)
    ms = GroupChildMenuSerializer(queryset, many=True)

    btn_queryset = GroupRight.objects.filter(group_id__in=role)
    btns = GroupRightSerializer(btn_queryset, many=True)

    dep_queryset = UserDepartment.objects.filter(user=user)
    deps = UserDepartmentSerializer(dep_queryset, many=True)

    d1 = {'UserRouterMap': ms.data, 'UserBtn': btns.data, 'UseDept': deps.data}
    f = 1
    return Response(d1)

@api_view(['POST'])
def logout(request):
    return  Response({"roles":"admin","name":"tomcti","avatar":"tom"})

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getOrganization(request):
    bh = request.query_params.get('code')
    cursor = connection.cursor()
    cursor.callproc('getOrganization', [bh])
    row = dictfetchall(cursor)
    return JsonResponse(row,safe=False,json_dumps_params={'ensure_ascii':False})

