from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.utils.timezone import now,timedelta
from datetime import time,date
from django.db.models.aggregates import Sum,Max
from django.db.models import F,FloatField
import math
from backend.models import *
import uuid
import  datetime
from rest_framework_tracking.models import APIRequestLog


class UserSerializer(serializers.ModelSerializer):
    """
    系统user
    """
    class Meta:
        model = User
        fields = '__all__'

class GroupMenuSerializer(serializers.ModelSerializer):
    """
    部门菜单
    """
    menu_id = serializers.SerializerMethodField()
    path = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    class Meta:
        model =  GroupMenu
        fields = ('menus_id','menu_id','isvisible','label','path')
    def get_label(self, obj):
        return obj.menus.name
    def get_menu_id(self, obj):
        return obj.menus.menu_id
    def get_path(self, obj):
        return obj.menus.path

class GroupChildMenuSerializer(serializers.ModelSerializer):
    groupmenu = GroupMenuSerializer()
    class Meta:
        model =  GroupChildMenu
        fields = ('groupmenu','child_menu_id','isvisible','path','name','title','icon','component')

class sysRightSerializer(serializers.ModelSerializer):
    """
    基本权限序列化类
    """
    class Meta:
        model = sysRight
        fields = '__all__'

class GroupRightSerializer(serializers.ModelSerializer):
    rights = sysRightSerializer()
    class Meta:
        model =  GroupRight
        fields = '__all__'

class UserDepartmentSerializer(serializers.ModelSerializer):
    """
    员工组织机构权限表
    """
    depid = serializers.SerializerMethodField()
    depname = serializers.SerializerMethodField()
    depcode = serializers.SerializerMethodField()

    def get_depid(self, obj):
        return obj.dep.id

    def get_depname(self, obj):
        return obj.dep.name

    def get_depcode(self, obj):
        return obj.dep.code

    class Meta:
        model =  UserDepartment
        fields = ('id', 'depid', 'depname', 'depcode')

class invoice_dictSerializer(serializers.ModelSerializer):
    """
    发票字典
    """
    class Meta:
        model = invoice_dict
        fields = '__all__'

class jinjizhengSerializer(serializers.ModelSerializer):
    """
    禁忌症字典
    """
    class Meta:
        model = jinjizheng
        fields = '__all__'

class profit_distri_dictSerializer(serializers.ModelSerializer):
    """
    利润分成字典
    """
    class Meta:
        model = profit_distri_dict
        fields = '__all__'

class invoice_setSerializer(serializers.ModelSerializer):
    """
    发票设置
    """
    invoicename = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()

    def get_invoicename(self, obj):
        invoiceid = obj.invoice_id
        if invoiceid:
            inv_obj = invoice_dict.objects.filter(id=invoiceid).first()
            return inv_obj.name
        else:
            return ''

    def get_percent(self, obj):
        percentid = obj.profit_distri_id
        if percentid:
            percent_obj = profit_distri_dict.objects.filter(id=percentid).first()
            return percent_obj.name
        else:
            return ''

    class Meta:
        model = invoice_set
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hospital_id = self.initial_data.pop('hospital_id')
        obj = invoice_set.objects.create(hospital_id=hospital_id, **validated_data)
        return obj

class coo_hospitalSerializer(serializers.ModelSerializer):
    """
    合作医院
    """
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        json = {}
        exsists = invoice_set.objects.filter(hospital__exact=obj)
        json = invoice_setSerializer(exsists, many=True, context={'request': self.context['request']}).data
        return json

    class Meta:
        model = coo_hospital
        fields = '__all__'

class coo_hospitalDetailSerializer(serializers.ModelSerializer):
    """
    合作医院新增序列化
    """
    # invoice_id = serializers.IntegerField(write_only=True)
    # profit_id = serializers.IntegerField(write_only=True)
    # value = serializers.IntegerField(write_only=True)

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     invoice_id = validated_data.pop('invoice_id')
    #     profit_id = validated_data.pop('profit_id')
    #     value = validated_data.pop('value')
    #     obj = coo_hospital.objects.create(**validated_data)
    #     begindate = validated_data.pop('begindate')
    #     enddate = validated_data.pop('enddate')
    #     invoice_set.objects.create(hospital=obj,invoice_id=invoice_id,profit_distri_id=profit_id,
    #                                value=value,begindate=begindate,enddate=enddate)
    #     return obj

    class Meta:
        model = coo_hospital
        fields = '__all__'

class dept_dictSerializer(serializers.ModelSerializer):
    """
    公司科室字典
    """
    class Meta:
        model = dept_dict
        fields = '__all__'

class post_dictSerializer(serializers.ModelSerializer):
    """
    公司岗位字典
    """
    class Meta:
        model = post_dict
        fields = '__all__'

class project_dictSerializer(serializers.ModelSerializer):
    """
    公司项目字典
    """
    class Meta:
        model = project_dict
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        action = self.initial_data.pop('action')
        obj = {}
        if action == 'Add':
            obj = project_dict.objects.create(**validated_data)
        else:
            parentid = self.initial_data.pop('parentid')
            projectdicts = self.initial_data.pop('projectdicts')
            for item in projectdicts:
                obj = project_dict.objects.create(parent_id=parentid,name=item['name'],projectid=item['projectid'])
        return obj

class project_jinjizhengSerializer(serializers.ModelSerializer):
    """
    公司项目禁忌症
    """
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.jinjizheng.name

    class Meta:
        model = project_jinjizheng
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        project_id = self.initial_data.pop('project_id')
        jinjizhengs = self.initial_data.pop('jinjizhengs')
        obj = {}
        for item in jinjizhengs:
            obj = project_jinjizheng.objects.create(projectdict_id=project_id, jinjizheng_id=item)
        return obj

class performance_dictSerializer(serializers.ModelSerializer):
    """
    公司绩效字典
    """
    class Meta:
        model = performance_dict
        fields = '__all__'

class benefit_dictSerializer(serializers.ModelSerializer):
    """
    福利绩效字典
    """
    class Meta:
        model = benefit_dict
        fields = '__all__'

class dept_postSerializer(serializers.ModelSerializer):
    """
    科室岗位
    """
    deptname = serializers.SerializerMethodField()
    postname = serializers.SerializerMethodField()

    def get_postname(self, obj):
        return obj.postdict.name

    def get_deptname(self, obj):
        return obj.deptdict.name

    class Meta:
        model = dept_post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        deptdict_id = self.initial_data.pop('deptdict_id')
        posts = self.initial_data.pop('posts')
        obj = {}
        for item in posts:
            obj = dept_post.objects.create(deptdict_id=deptdict_id,postdict_id=item['id'])
        return obj

class dept_client_typeSerializer(serializers.ModelSerializer):
    """
    科室对应的客户来源
    """
    clienttype_id = serializers.SerializerMethodField()
    clienttype_name = serializers.SerializerMethodField()

    def get_clienttype_name(self, obj):
        return obj.clienttype.name

    def get_clienttype_id(self, obj):
        return obj.clienttype.id

    class Meta:
        model = dept_client_type
        fields = '__all__'


class deptSerializer(serializers.ModelSerializer):
    """
    中心科室
    """
    name = serializers.SerializerMethodField()
    deptname = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.hrmdepartment.name

    def get_deptname(self, obj):
        return obj.deptdict.name

    class Meta:
        model = dept
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        depts = self.initial_data.pop('depts')
        obj = {}
        for item in depts:
            obj = dept.objects.create(hrmdepartment_id=hrmdepartment_id,deptdict_id=item['id'])
        return obj

class tuitionFeeSerializer(serializers.ModelSerializer):
    """
    中心带教费
    """
    name = serializers.SerializerMethodField()
    deptname = serializers.SerializerMethodField()
    tuitionname = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.hrmdepartment.name

    def get_deptname(self, obj):
        return obj.dept.deptdict.name

    def get_tuitionname(self, obj):
        return obj.tuition.name

    class Meta:
        model = tuitionFee
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        depts = self.initial_data.pop('depts')
        obj = {}
        for item in depts:
            obj = tuitionFee.objects.create(hrmdepartment_id=hrmdepartment_id,dept_id=item['id'])
        return obj


class projectSerializer(serializers.ModelSerializer):
    """
    中心项目
    """

    hrmdepartname = serializers.SerializerMethodField()
    tckind = serializers.SerializerMethodField()

    # ################################2019-09-18 add
    child_num = serializers.SerializerMethodField()
    depth = serializers.SerializerMethodField()
    Children = serializers.SerializerMethodField()
    jinjizheng = serializers.SerializerMethodField()

    def get_child_num(self, obj):
        exsists = project.objects.filter(parent=obj)
        return exsists.count()

    def get_depth(self, obj):
        num = 0
        if obj.parent:
            if obj.parent.parent:
                num = 2
            else:
                num = 1
        return num

    def get_Children(self, obj):
        json = {}
        exsists = project.objects.filter(parent__exact=obj)
        json = projectSerializer(exsists, many=True, context={'request': self.context['request']}).data
        return json
    #################################################

    def get_hrmdepartname(self, obj):
        return obj.hrmdepartment.name

    def get_tckind(self, obj):
        if obj.type == 1:
            if obj.flag == 0:
                ret = '系统'
            else:
                ret = '自定义'
        else:
            ret = ''
        return ret

    def get_jinjizheng(self, obj):
        num = 0
        register_id = self.context['request'].query_params.get('register_id')
        if register_id:
            ids = client_jinjizheng.objects.filter(clientregister_id=register_id).values('jinjizheng')
            projectdict = project_dict.objects.filter(projectid=obj.projectid).first()
            pro_jjzs = project_jinjizheng.objects.filter(projectdict=projectdict).filter(jinjizheng__in=ids)
            num = len(pro_jjzs)
        return num

    class Meta:
        model = project
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        action = self.initial_data.pop('action')
        projects = self.initial_data.pop('projects')
        obj = {}

        # 导入项目(包括单项及套餐)
        if action == 'import':
            for item in projects:
                type = item['type']
                if type == True:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id,projectid=item['projectid'],
                                                 name=item['name'],type=1,isindependent=item['isindependent'],
                                                 amount=item['amount'])
                    id = obj.id
                    exsists = list(project_dict.objects.filter(parent_id__exact=item['id']))
                    for i in range(0, len(exsists)):
                        project.objects.create(hrmdepartment_id=hrmdepartment_id,projectid=exsists[i].projectid,
                                               name=exsists[i].name,type=0,isindependent=exsists[i].isindependent,parent_id=id)
                else:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id, projectid=item['projectid'],
                                           name=item['name'], type=0, isindependent=item['isindependent'])
        # 新增套餐
        elif action == 'taocanAdd':
            parentname = validated_data.pop('name')
            parent_obj = project.objects.create(hrmdepartment_id=hrmdepartment_id, name=parentname, type=1,flag=1)
            for item in projects:
                type = item['type']
                if type == True:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id, projectid=item['projectid'],
                                                 name=item['name'], type=1, isindependent=item['isindependent'],
                                                 amount=item['amount'], parent_id=parent_obj.id)
                    id = obj.id
                    exsists = list(project_dict.objects.filter(parent_id__exact=item['id']))
                    for i in range(0, len(exsists)):
                        project.objects.create(hrmdepartment_id=hrmdepartment_id, projectid=exsists[i].projectid,
                                               name=exsists[i].name, type=0, isindependent=exsists[i].isindependent,
                                               parent_id=id)
                else:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id, projectid=item['projectid'],
                                                 name=item['name'], type=0, parent_id=parent_obj.id,
                                                 isindependent=item['isindependent'])
        # 套餐修改界面添加
        else:
            parentid = self.initial_data.pop('parentid')
            for item in projects:
                type = item['type']
                if type == True:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id,projectid=item['projectid'],
                                                 name=item['name'],type=1,isindependent=item['isindependent'],
                                                 amount=item['amount'],parent_id=parentid)
                    id = obj.id
                    exsists = list(project_dict.objects.filter(parent_id__exact=item['id']))
                    for o in exsists:
                        project.objects.create(hrmdepartment_id=hrmdepartment_id,projectid=o.projectid,
                                               name=o.name,type=0,isindependent=o.isindependent,parent_id=id)
                else:
                    obj = project.objects.create(hrmdepartment_id=hrmdepartment_id, projectid=item['projectid'],
                                         name=item['name'], type=0,parent_id=parentid,
                                         isindependent=item['isindependent'])

        return obj


class tuitionFee_detailSerializer(serializers.ModelSerializer):
    """
    中心带教费详细
    """
    projectname = serializers.SerializerMethodField()
    tuitionname = serializers.SerializerMethodField()

    def get_projectname(self, obj):
        return obj.project.name

    def get_tuitionname(self, obj):
        return obj.tuition.name

    class Meta:
        model = tuitionFee_detail
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        tuitionfee_id = self.initial_data.pop('tuitionfee_id')
        projects = self.initial_data.pop('projects')
        obj = {}
        for item in projects:
            obj = tuitionFee_detail.objects.create(tuitionfee_id=tuitionfee_id,project_id=item['id'])
        return obj

class finance_monthSerializer(serializers.ModelSerializer):
    """
    财务月
    """
    deptname = serializers.SerializerMethodField()

    def get_deptname(self, obj):
        return obj.hrmdepartment.name

    class Meta:
        model = finance_month
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        obj = finance_month.objects.create(hrmdepartment_id=hrmdepartment_id, **validated_data)
        return obj

class performanceSerializer(serializers.ModelSerializer):
    """
    中心绩效
    """
    deptname = serializers.SerializerMethodField()
    performancename = serializers.SerializerMethodField()

    def get_deptname(self, obj):
        return obj.hrmdepartment.name

    def get_performancename(self, obj):
        return obj.performancedict.name

    class Meta:
        model = performance
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        depts = self.initial_data.pop('depts')
        obj = {}
        for item in depts:
            obj = performance.objects.create(hrmdepartment_id=hrmdepartment_id,performancedict_id=item['id'])
        return obj

class benefitSerializer(serializers.ModelSerializer):
    """
    中心工资福利
    """
    deptname = serializers.SerializerMethodField()
    benefitname = serializers.SerializerMethodField()

    def get_deptname(self, obj):
        return obj.hrmdepartment.name

    def get_benefitname(self, obj):
        return obj.benefitdict.name

    class Meta:
        model = benefit
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        depts = self.initial_data.pop('depts')
        obj = {}
        for item in depts:
            obj = benefit.objects.create(hrmdepartment_id=hrmdepartment_id,benefitdict_id=item['id'])
        return obj

class huiyuan_setSerializer(serializers.ModelSerializer):
    """
    回院设置
    """
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.projectdict.name

    class Meta:
        model = huiyuan_set
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        projects = self.initial_data.pop('projects')
        obj = {}
        for item in projects:
            obj = huiyuan_set.objects.create(projectdict_id=item['id'])
        return obj

class HrmCompanySerializer(serializers.ModelSerializer):
    """
    公司
    """
    class Meta:
        model = HrmCompany
        fields = '__all__'

class HrmSubCompanySerializer(serializers.ModelSerializer):
    """
    公司分部
    """
    status = serializers.IntegerField(write_only=True)

    class Meta:
        model = HrmSubCompany
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        status = validated_data.pop('status')
        code = validated_data.pop('code')
        obj = {}
        if status == 0:
            exists = HrmSubCompany.objects.filter(companyid__exact=1).order_by('-code')
            num = str(1)
            if exists.count() > 0:
                maxcode = exists.first().code
                num = str(int(maxcode[-2:]) + 1)

            mcode = code + num.zfill(2)
            obj = HrmSubCompany.objects.create(code=mcode,**validated_data)
        else:
            exists = HrmSubCompany.objects.filter(supsubcomid__exact=code).order_by('-code')
            num = str(1)
            if exists.count() > 0:
                maxcode = exists.first().code
                num = str(int(maxcode[-2:]) + 1)

            mcode = code + num.zfill(2)
            obj = HrmSubCompany.objects.create(code=mcode, **validated_data)
        return obj

class HrmDepartmentSerializer(serializers.ModelSerializer):
    """
    公司部门
    """
    status = serializers.IntegerField(write_only=True)

    class Meta:
        model = HrmDepartment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        status = validated_data.pop('status')
        code = validated_data.pop('code')

        num = str(1)
        if status > 2:
            exists = HrmDepartment.objects.filter(supdepid__exact=code).order_by('-code')
            if exists.count() > 0:
                maxcode = exists.first().code
                num = str(int(maxcode[-2:]) + 1)

            mcode = code + num.zfill(2)
            obj = HrmDepartment.objects.create(code=mcode,**validated_data)
        else:
            exists = HrmDepartment.objects.filter(subcompanyid__exact=code).order_by('-code')
            if exists.count() > 0:
                maxcode = exists.first().code
                num = str(int(maxcode[-2:]) + 1)

            mcode = code + num.zfill(2)
            obj = HrmDepartment.objects.create(code=mcode, **validated_data)
        return obj

    def update(self, instance, validated_data):
        a = self.initial_data['aa']
        num = len(a)
        instance.name = validated_data.pop('name')
        instance.description = validated_data.pop('description')
        instance.save()
        return instance

class subCompanyFieldSerializer(serializers.ModelSerializer):
    """
    公司分部自定义
    """
    class Meta:
        model = subCompanyField
        fields = '__all__'

class userProfileSerializer(serializers.ModelSerializer):
    """
    员工档案
    """
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = userProfile
        fields = '__all__'

class clientSerializer(serializers.ModelSerializer):
    """
    客户档案
    """
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.adduser.username

    class Meta:
        model = client
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        obj = client.objects.create(adduser=user,**validated_data)
        return obj

class client_registerSerializer(serializers.ModelSerializer):
    """
    客户登记
    """
    name = serializers.SerializerMethodField()
    clienttype = serializers.SerializerMethodField()
    registerdeptname = serializers.SerializerMethodField()
    jinjizheng = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.client.name

    def get_clienttype(self, obj):
        kind = obj.client_type
        if kind == 1:
            name = '孕妇'
        elif kind == 2:
            name = '产妇'
        elif kind == 3:
            name = '备孕'
        elif kind == 4:
            name = '婴幼儿'
        else:
            name = '疾病人群'
        return name

    def get_registerdeptname(self, obj):
        return obj.dept.deptdict.name

    def get_jinjizheng(self, obj):
        jinjizhengList = client_jinjizheng.objects.filter(clientregister=obj).values('jinjizheng_id')
        return jinjizhengList

    class Meta:
        model = client_register
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        client_id = self.initial_data.pop('client_id')
        dept_id = self.initial_data.pop('dept')
        jjz = self.initial_data.pop('jinjizheng')
        obj = client_register.objects.create(client_id=client_id,dept_id=dept_id,**validated_data)
        if len(jjz) > 0:
            for item in jjz:
                client_jinjizheng.objects.create(clientregister=obj,jinjizheng_id=item,adduser=user)
                client_jinjizheng_log.objects.create(client_register=obj,jinjizheng_id=item,adduser=user,type=0)
        return obj

    def update(self, instance, validated_data):
        user = self.context['request'].user
        jinjizhengs = self.initial_data['jinjizheng']
        if len(jinjizhengs) > 0:
            client_jinjizheng.objects.filter(clientregister=instance).delete()
            for item in jinjizhengs:
                client_jinjizheng.objects.create(clientregister=instance,jinjizheng_id=item,adduser=user)
                client_jinjizheng_log.objects.create(client_register=instance, jinjizheng_id=item, adduser=user, type=1)
        instance.save()
        return instance

class orderSerializer(serializers.ModelSerializer):
    """
    宣教开单
    """
    username = serializers.SerializerMethodField()
    clientname = serializers.SerializerMethodField()
    deptname = serializers.SerializerMethodField()
    marketPostname = serializers.SerializerMethodField()
    orderPostname = serializers.SerializerMethodField()
    orderdeptname = serializers.SerializerMethodField()
    projectname = serializers.SerializerMethodField()
    marketmanname = serializers.SerializerMethodField()
    orderuser = serializers.SerializerMethodField()
    child_num = serializers.SerializerMethodField()
    Children = serializers.SerializerMethodField()
    depth = serializers.SerializerMethodField()
    times = serializers.SerializerMethodField()

    def get_depth(self, obj):
        num = 0
        if obj.parent:
            if obj.parent.parent:
                num = 2
            else:
                num = 1
        return num

    def get_username(self, obj):
        name = ''
        if obj.adduser:
            name = obj.adduser.name
        return name

    def get_clientname(self, obj):
        return obj.client.name

    def get_deptname(self, obj):
        name = ''
        if obj.marketdept:
            name = obj.marketdept.deptdict.name
        return name

    def get_marketPostname(self, obj):
        name = ''
        if obj.marketpost:
            name = obj.marketpost.name
        return name

    def get_orderPostname(self, obj):
        name = ''
        if obj.orderpost:
            name = obj.orderpost.name
        return name

    def get_orderdeptname(self, obj):
        name = ''
        if obj.orderdept:
            name = obj.orderdept.deptdict.name
        return name

    def get_projectname(self, obj):
        name = ''
        if obj.project:
            name = obj.project.name
        return name

    def get_marketmanname(self, obj):
        name = ''
        if obj.marketman:
            name = obj.marketman.name
        return name

    def get_orderuser(self, obj):
        name = ''
        if obj.adduser:
            name = obj.adduser.name
        return name

    def get_child_num(self, obj):
        exsists = order.objects.filter(parent=obj)
        return exsists.count()

    def get_Children(self, obj):
        json = {}
        exsists = order.objects.filter(parent__exact=obj)
        json = orderSerializer(exsists, many=True, context={'request': self.context['request']}).data
        return json

    def get_times(self, obj):
        num = ''
        if obj.parent:
            num = obj.times
        else:
            if obj.project:
                if obj.project.type == False:
                    num = obj.times
        return num

    class Meta:
        model = order
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        hrmdepartment_id = self.initial_data.pop('hrmdepartment_id')
        client_id = self.initial_data.pop('clientid')
        register_id = self.initial_data.pop('register_id')
        projects = self.initial_data.pop('projects')
        a = validated_data.pop('isproorder')
        firstList = [item for item in projects]
        obj = {}
        if len(firstList) > 0:
            # 第一层项目
            for item in firstList:

                if item.get('isproorder',-1) == -1:
                    item['isproorder'] = False
                if item.get('receivable', -1) == -1:
                    item['receivable'] = 0
                if item.get('discount',-1) == -1:
                    item['discount'] = 0
                if item.get('receipts', -1) == -1:
                    item['receipts'] = 0
                if item.get('times', -1) == -1:
                    item['times'] = 0

                isproorder = item.get('isproorder',0)
                tckind = item.get('tckind','')
                project_id = item.get('id',0)

                obj = order.objects.create(client_id=client_id,hrmdepartment_id=hrmdepartment_id,
                      project_id=item['id'],receivable=item.get('receivable',0),discount=item.get('discount',0),
                      receipts=item.get('receipts',0),times=item.get('times', 0),
                      isproorder=item.get('isproorder',0),register_id=register_id,**validated_data)

                if tckind == '':  # 单项
                    treat.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                 adduser=obj.adduser, orderdept=obj.orderdept, order=obj,
                                 project=obj.project, isacquire=obj.isacquire, times=obj.times,
                                 residue=obj.times,isproorder=item.get('isproorder',0),register=obj.register)

                elif tckind == '系统':  # 系统套餐

                    # 当开单项目是系统套餐时 先插治疗表
                    treat_obj = treat.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                 adduser=obj.adduser, orderdept=obj.orderdept, order=obj,
                                 project=obj.project, isacquire=obj.isacquire, times=obj.times,
                                 residue=obj.times,isproorder=item.get('isproorder',0),register=obj.register)

                    secondList = project.objects.filter(parent_id=project_id)
                    for seconditem in secondList:
                        secondobj = order.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                     project_id=seconditem.id,receivable=0,discount=0,receipts=0,
                                     parent=obj, times=seconditem.amount,register_id=register_id,**validated_data)

                        treat.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                     adduser=secondobj.adduser,orderdept=secondobj.orderdept, order=secondobj,
                                     project=secondobj.project,parent=treat_obj,isproorder=item.get('isproorder',0),
                                     isacquire=secondobj.isacquire, times=secondobj.times, residue=secondobj.times,
                                     register=secondobj.register)

                else:   # 自定义套餐
                    secondList = project.objects.filter(parent_id=project_id)

                    for seconditem in secondList:
                        secondobj = order.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                     project_id=seconditem.id,receivable=0,discount=0,receipts=0,parent=obj,
                                     times=seconditem.amount,isproorder=item.get('isproorder',0),
                                     register_id=register_id,**validated_data)

                        secondtreatobj = treat.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                         adduser=secondobj.adduser,orderdept=secondobj.orderdept, order=secondobj,
                                         project=secondobj.project,isacquire=secondobj.isacquire, times=secondobj.times,
                                         residue=secondobj.times,isproorder=item.get('isproorder',0),register=secondobj.register)

                        thirdList = project.objects.filter(parent=seconditem)
                        for thirditem in thirdList:
                            thirdobj = order.objects.create(client_id=client_id,hrmdepartment_id=hrmdepartment_id,
                                       project_id=thirditem.id,receivable=0,discount=0,receipts=0,
                                       times=thirditem.amount,parent=secondobj,register_id=register_id,**validated_data)

                            treat.objects.create(client_id=client_id, hrmdepartment_id=hrmdepartment_id,
                                             adduser=thirdobj.adduser, orderdept=thirdobj.orderdept, order=thirdobj,
                                             project=thirdobj.project, parent=secondtreatobj,
                                             isacquire=thirdobj.isacquire,isproorder=item.get('isproorder',0),
                                             times=thirdobj.times, residue=thirdobj.times,register=thirdobj.register)

        else:
            obj = order.objects.create(client_id=client_id,hrmdepartment_id=hrmdepartment_id,
                      receivable=0,discount=0, receipts=0,register_id=register_id,**validated_data)

        return obj

    def update(self, instance, validated_data):
        action = self.initial_data.pop('action')

        if action == 0:  # 缴费收单取消
            orderList = self.initial_data.pop('orders')
            order.objects.filter(id__in=orderList).update(isacquire=0)
        if action == 1:  # 缴费收单
            orderList = self.initial_data.pop('orders')
            order.objects.filter(id__in=orderList).update(isacquire=1)
        if action == 2:  # 治疗(开单中的)
            obj = treat.objects.create(client=instance.client,adduser=instance.adduser,orderdept=instance.orderdept,
                                       order=instance,project=instance.project,isacquire=instance.isacquire,
                                       times=instance.times,residue=instance.times,
                                       register=instance.register,hrmdepartment=instance.hrmdepartment)
            exsists = order.objects.filter(parent=instance)
            if len(exsists) > 0:
                for item in exsists:
                    treat.objects.create(client=item.client, adduser=item.adduser, orderdept=item.orderdept,
                                     order=item, project=item.project, isacquire=item.isacquire,
                                     times=item.times, residue=item.times,hrmdepartment=item.hrmdepartment,
                                     parent=obj,register=item.register)

        return instance

class treatSerializer(serializers.ModelSerializer):
    """
    检查治疗
    """
    child_num = serializers.SerializerMethodField()
    depth = serializers.SerializerMethodField()
    Children = serializers.SerializerMethodField()
    clientname = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    projectname = serializers.SerializerMethodField()
    treatdeptname = serializers.SerializerMethodField()
    operatename = serializers.SerializerMethodField()
    ordermanname = serializers.SerializerMethodField()
    orderdeptname = serializers.SerializerMethodField()
    orderpostname = serializers.SerializerMethodField()
    orderdate = serializers.SerializerMethodField()
    isappoint = serializers.SerializerMethodField()
    jinjizheng = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    register = client_registerSerializer()

    def get_child_num(self, obj):
        exsists = treat.objects.filter(parent=obj)
        return exsists.count()

    def get_depth(self, obj):
        num = 0
        if obj.parent:
            num = 1
        return num

    def get_Children(self, obj):
        json = []
        if obj.project.type == True:
            ids = treat.objects.filter(parent__exact=obj).values('project_id').annotate(max_id=Max('id')).values('max_id')
            exsists = treat.objects.filter(parent__exact=obj).filter(id__in=ids)
            json = treatSerializer(exsists, many=True, context={'request': self.context['request']}).data
        return json

    def get_clientname(self, obj):
        return obj.client.name

    def get_phone(self, obj):
        clientobj = obj.client
        return clientobj.phone1

    def get_age(self,obj):
        nianling = ''
        if obj.client.birthDate:
            nianling = datetime.datetime.today().year - obj.client.birthDate.year
        return  nianling

    def get_projectname(self, obj):
        return obj.project.name

    def get_treatdeptname(self, obj):
        name = ''
        deptobj = obj.treatdept
        if deptobj:
            name = deptobj.deptdict.name
        return name

    def get_operatename(self, obj):
        name = ''
        operateobj = obj.operator
        if operateobj:
            name = operateobj.name
        return name

    def get_ordermanname(self, obj):
        return obj.adduser.name

    def get_orderdeptname(self, obj):
        return obj.orderdept.deptdict.name

    def get_orderpostname(self, obj):
        return obj.order.orderpost.name

    def get_orderdate(self, obj):
        return obj.order.marketdate

    def get_isappoint(self, obj):
        name = ''
        flag = obj.isappoint
        if flag == 1:
            name = '预约'
        return name

    def get_jinjizheng(self, obj):
        jjzs = client_jinjizheng.objects.filter(clientregister=obj.register).values('jinjizheng_id')
        if len(jjzs) > 0:
            return list(jjzs)
        else:
            return []

    def get_type(self, obj):
        ret = 0
        kind = obj.project.type
        if kind == 1:
            ret = 1
        return ret

    class Meta:
        model = treat
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        treat_id = self.initial_data.pop('id')
        action = self.initial_data.pop('action')
        num = self.initial_data.pop('num')
        treatdept = self.initial_data.pop('treatdept')
        operator = self.initial_data.pop('operator')
        healthtype = self.initial_data.pop('healthtype')
        yunzhou = self.initial_data.pop('yunzhou')
        weight = self.initial_data.pop('weight')
        operatedate = self.initial_data.pop('operatedate')
        diagnosis = self.initial_data.pop('diagnosis')
        guide = self.initial_data.pop('guide')
        comment = self.initial_data.pop('comment')
        treatobj = treat.objects.get(pk=treat_id)
        obj = {}
        if treatobj.residue > 0: # 如果剩余次数大于0 才插入记录
            if treatobj.parent: # 如果是单项第一条
                obj = treat.objects.create(client=treatobj.client,adduser=treatobj.adduser,orderdept=treatobj.orderdept,
                      order=treatobj.order,project=treatobj.project,parent=treatobj.parent,treattype=1,
                      isacquire=treatobj.isacquire,times=treatobj.times,residue=treatobj.residue-num,
                      amount=num,treatdept_id=treatdept,operator_id=operator, healthtype=healthtype,
                      yunzhou=yunzhou,weight=weight,operatedate=operatedate,diagnosis=diagnosis,guide=guide,
                      register=treatobj.register,hrmdepartment=treatobj.hrmdepartment,comment=comment)
            else:
                recnum = treatobj.treattype
                if recnum == 0:
                    flag = 1
                else:
                    flag = 2
                obj = treat.objects.create(client=treatobj.client, adduser=treatobj.adduser, orderdept=treatobj.orderdept,
                       order=treatobj.order, project=treatobj.project, parent_id=treat_id,treattype=flag,
                       isacquire=treatobj.isacquire, times=treatobj.times,residue=treatobj.residue - num,
                       amount=num, treatdept_id=treatdept, operator_id=operator, healthtype=healthtype,
                       yunzhou=yunzhou, weight=weight, operatedate=operatedate, diagnosis=diagnosis,
                       guide=guide,register=treatobj.register,hrmdepartment=treatobj.hrmdepartment, comment=comment)

                if recnum == 0:
                    begindate = datetime.datetime.strptime(operatedate, '%Y-%m-%d') + timedelta(days=7)
                    startdate = begindate.strftime('%Y-%m-%d')
                    enddate = datetime.datetime.strptime(operatedate, '%Y-%m-%d') + timedelta(days=10)
                    jieshudate = enddate.strftime('%Y-%m-%d')
                    callback.objects.create(client=treatobj.client, dept_id=treatdept, order=treatobj.order,
                                            times=treatobj.times, residue=treatobj.residue - num, begindate=startdate,
                                            enddate=jieshudate,ispreorder=treatobj.isproorder,healthtype=treatobj.healthtype,
                                            diagnosis=treatdept.diagnosis,guide=treatdept.guide,
                                            hrmdepartment=treatobj.hrmdepartment)

                treatobj.treattype = flag
                treatobj.residue = treatobj.residue - num
                treatobj.amount = num
                treatobj.treatdept_id = treatdept
                treatobj.operatedate = date.today()
                treatobj.operator_id = operator
                treatobj.healthtype = healthtype
                treatobj.yunzhou = yunzhou
                treatobj.weight = weight
                treatobj.diagnosis = diagnosis
                treatobj.guide = guide
                treatobj.comment = comment
                treatobj.save()

        return obj

    def update(self, instance, validated_data):
        user = self.context['request'].user
        action = self.initial_data.pop('action')
        num = self.initial_data.get('num')
        treatdept = self.initial_data.get('treatdept')
        operator = self.initial_data.get('operator')

        if action == 0:  # 批量治疗
            treatList = self.initial_data.pop('treats')
            for item in treatList:
                treatobj = treat.objects.get(pk=item)
                person = treatobj.operator
                projecttype = treatobj.project.type
                if projecttype == 0: # 单项的处理
                    if treatobj.residue > 0: # 如何剩余次数等于0 既不插入也不更新
                        recnum = treat.objects.filter(order=treatobj.order,project=treatobj.project).count()
                        if recnum == 1:
                            flag = 1
                        else:
                            flag = 2
                        obj = treat.objects.create(client=treatobj.client, adduser=treatobj.adduser,
                               orderdept=treatobj.orderdept,
                               order=treatobj.order, project=treatobj.project,
                               parent=treatobj,operatedate = date.today(),
                               isacquire=treatobj.isacquire, times=treatobj.times,
                               residue=treatobj.residue - num,
                               amount=num, treatdept_id=treatdept, operator_id=operator,
                               treattype=flag,register=treatobj.register,
                               hrmdepartment=treatobj.hrmdepartment, comment=treatobj.comment)

                        treatobj.residue = treatobj.residue - num
                        treatobj.amount = num
                        treatobj.treatdept_id = treatdept
                        treatobj.operatedate = date.today()
                        treatobj.operator_id = operator
                        treatobj.treattype = flag
                        treatobj.save()
                else: # 套餐的处理
                    exsists = treat.objects.filter(parent=treatobj)
                    for o in exsists:
                        onum = treat.objects.filter(parent=treatobj,project=o.project).count()
                        if onum == 1:
                            oflag = 1
                        else:
                            oflag = 2

                        if o.treattype == 0: # 第一次治疗--开单加入的第一条
                            o.amount = num
                            o.treatdept_id = treatdept
                            o.residue = o.residue - num
                            o.operator_id = operator
                            o.operatedate = date.today()
                            o.treattype = oflag
                            o.save()
                        else: # 第二次及更多治疗
                            if o.residue > 0: # 如何治疗次数为0 就不插入记录
                                treat.objects.create(client=o.client, adduser=o.adduser,orderdept=o.orderdept,
                                     order=o.order, project=o.project,parent=o.parent,operatedate=date.today(),
                                     isacquire=o.isacquire, times=o.times,residue=o.residue - num,
                                     amount=num, treatdept_id=treatdept, operator_id=operator,
                                     treattype=oflag, register=o.register,hrmdepartment=o.hrmdepartment,
                                     comment=o.comment)

        elif action == 1:  # 点击营养治疗按钮的操作
            healthtype = self.initial_data.pop('healthtype')
            yunzhou = self.initial_data.pop('yunzhou')
            weight = self.initial_data.pop('weight')
            operatedate = self.initial_data.pop('operatedate')
            diagnosis = self.initial_data.pop('diagnosis')
            guide = self.initial_data.pop('guide')
            comment = self.initial_data.pop('comment')

            if instance.residue > 0: # 如何剩余次数大于0 才插入记录
                recnum = instance.treattype
                if recnum == 0: # 第一次治疗
                    flag = 1
                else: # 第二次及更多次治疗
                    flag = 2
                treat.objects.create(client=instance.client, adduser=instance.adduser,
                                   orderdept=instance.orderdept,
                                   order=instance.order, project=instance.project,
                                   parent=instance,operatedate = operatedate,
                                   isacquire=instance.isacquire, times=instance.times,
                                   residue=instance.residue - num,healthtype=healthtype,
                                   yunzhou=yunzhou,weight=weight,diagnosis=diagnosis,guide=guide,
                                   amount=num, treatdept_id=treatdept, operator_id=operator,
                                   treattype=flag,register=instance.register,
                                   hrmdepartment=instance.hrmdepartment, comment=instance.comment)

                # 治疗保存时 同时要向回访表里插入回访记录
                if recnum == 0:
                    begindate = datetime.datetime.strptime(operatedate, '%Y-%m-%d') + timedelta(days=7)
                    startdate = begindate.strftime('%Y-%m-%d')
                    enddate = datetime.datetime.strptime(operatedate, '%Y-%m-%d') + timedelta(days=10)
                    jieshudate = enddate.strftime('%Y-%m-%d')
                    callback.objects.create(client=instance.client,dept_id=treatdept,order=instance.order,
                                            times=instance.times,residue=instance.residue-num,begindate=startdate,
                                            enddate=jieshudate,ispreorder=instance.isproorder,treat=instance,
                                            healthtype=instance.healthtype,diagnosis=diagnosis,guide=guide,
                                            callbacktype=0,hrmdepartment=instance.hrmdepartment)

                instance.treattype = flag
                instance.amount = 1
                instance.residue = instance.residue - 1
                instance.healthtype = healthtype
                instance.yunzhou = yunzhou
                instance.weight = weight
                instance.treatdept_id = treatdept
                instance.operator_id = operator
                instance.operatedate = operatedate
                instance.diagnosis = diagnosis
                instance.guide = guide
                instance.comment = comment
                instance.save()

        elif action == 2: # 点击全套治疗按钮时的操作
            parantid = self.initial_data.get('id')
            treatdept = validated_data.get('treatdept')
            operator = validated_data.get('operator')
            operatedate = validated_data.get('operatedate')
            s_callback = self.initial_data.get('s_callback')
            e_callback = self.initial_data.get('e_callback')
            s_treat = self.initial_data.get('s_treat')
            e_treat = self.initial_data.get('e_treat')
            comment = validated_data.get('comment')
            sons = self.initial_data.get('children')
            for item in sons:
                itemobj = treat.objects.get(pk=item.get('id'))
                objs = treat.objects.filter(parent_id=parantid,project=itemobj.project)
                if len(objs) == 1:
                    currentobj = objs.first()
                    if currentobj.residue > 0:
                        if currentobj.treattype == 0:
                            currentobj.residue = currentobj.residue - item.get('amount')
                            currentobj.amount = item.get('amount')
                            currentobj.treatdept_id = treatdept
                            currentobj.operator_id = operator
                            currentobj.operatedate = operatedate
                            currentobj.treattype = 1
                            currentobj.comment = comment
                            currentobj.save()
                        else:
                            treat.objects.create(client=currentobj.client, adduser=currentobj.adduser,
                                   orderdept=currentobj.orderdept,order=currentobj.order, project=currentobj.project,
                                   parent=currentobj.parent,operatedate = operatedate,
                                   isacquire=currentobj.isacquire, times=currentobj.times,
                                   residue=currentobj.residue - item.get('amount'),
                                   amount=item.get('amount'), treatdept=treatdept, operator=operator,
                                   treattype=2,register=currentobj.register,
                                   hrmdepartment=currentobj.hrmdepartment, comment=currentobj.comment)
                else:
                    currentobj = objs.order_by('-id').first()
                    if currentobj.residue > 0:
                        treat.objects.create(client=currentobj.client, adduser=currentobj.adduser,
                                             orderdept=currentobj.orderdept, order=currentobj.order,
                                             project=currentobj.project,
                                             parent=currentobj.parent, operatedate=operatedate,
                                             isacquire=currentobj.isacquire, times=currentobj.times,
                                             residue=currentobj.residue - item.get('amount'),
                                             amount=item.get('amount'), treatdept=treatdept, operator=operator,
                                             treattype=2, register=currentobj.register,
                                             hrmdepartment=currentobj.hrmdepartment, comment=currentobj.comment)

            # 如果有预约回访时间，则向回访表里插入回访记录
            if s_callback:
                callback.objects.create(client=instance.client, dept=treatdept, order=instance.order,
                                        begindate=s_callback,enddate=e_callback, ispreorder=instance.isproorder,
                                        treat=instance,callbacktype=2,hrmdepartment=instance.hrmdepartment)

            # 如果有预约治疗时间，则向治疗表里的第一条记录更新预约标志
            if s_treat:
                instance.isappoint = 1
                instance.begindate = s_treat
                instance.enddate = e_treat
                instance.save()
            else:
                instance.isappoint = 0
                instance.begindate = None
                instance.enddate = None
                instance.save()


        elif action == 3:   # 历史治疗记录修改
            healthtype = self.initial_data.pop('healthtype')
            yunzhou = self.initial_data.pop('yunzhou')
            weight = self.initial_data.pop('weight')
            operatedate = self.initial_data.pop('operatedate')
            diagnosis = self.initial_data.pop('diagnosis')
            guide = self.initial_data.pop('guide')
            comment = self.initial_data.pop('comment')
            instance.healthtype = healthtype
            instance.yunzhou = yunzhou
            instance.weight = weight
            instance.treatdept_id = treatdept
            instance.operator_id = operator
            instance.operatedate = operatedate
            instance.diagnosis = diagnosis
            instance.guide = guide
            instance.comment = comment
            instance.save()

        elif action == 4: # 点击套餐历史治疗记录时的修改
            operator = self.initial_data.get('operator')
            operatedate = self.initial_data.get('operatedate')
            treatdept = self.initial_data.get('treatdept')
            children = self.initial_data.get('children')
            comment = self.initial_data.get('comment')

            for item in children:
                childtreat = treat.objects.get(pk=item.get('id'))
                childtreat.residue = childtreat.residue - item.get('amount') + childtreat.amount
                childtreat.amount = item.get('amount')
                childtreat.treatdept_id = treatdept
                childtreat.operator_id = operator
                childtreat.operatedate = operatedate
                childtreat.comment = comment
                childtreat.save()
                lasttreat = treat.objects.filter(parent_id=instance.id,project_id=item.get('project_id')).\
                    exclude(pk=item.get('id')).order_by('-operatedate').first()
                if lasttreat:
                    lasttreat.residue = lasttreat.residue - item.get('amount') + childtreat.amount
                    lasttreat.save()

            instance.treatdept_id = treatdept
            instance.operator_id = operator
            instance.operatedate = operatedate
            instance.comment = comment
            instance.save()

        elif action == 5: # 点击除套餐外的其他产后治疗按钮时的操作
            amount = self.initial_data.get('amount')
            s_callback = self.initial_data.get('s_callback')
            e_callback = self.initial_data.get('e_callback')
            s_treat = self.initial_data.get('s_treat')
            e_treat = self.initial_data.get('e_treat')
            energy = self.initial_data.get('energy')
            jinjizheng = self.initial_data.get('jinjizheng')
            operator = self.initial_data.get('operator')
            operatedate = self.initial_data.get('operatedate')
            report = self.initial_data.get('report')
            treatdept = self.initial_data.get('treatdept')
            wendu = self.initial_data.get('wendu')
            yaling = self.initial_data.get('yaling')
            comment = self.initial_data.pop('comment')

            if instance.residue > 0:  # 如何剩余次数大于0 才插入记录
                recnum = instance.treattype
                if recnum == 0:  # 第一次治疗
                    flag = 1
                else:  # 第二次及更多次治疗
                    flag = 2
                treat.objects.create(client=instance.client, adduser=instance.adduser,
                                     orderdept=instance.orderdept,
                                     order=instance.order, project=instance.project,
                                     parent=instance, operatedate=operatedate,
                                     isacquire=instance.isacquire, times=instance.times,
                                     residue=instance.residue - amount, yaling=yaling,
                                     energy=energy, report=report, wendu=wendu,
                                     amount=amount, treatdept_id=treatdept, operator_id=operator,
                                     treattype=flag, register=instance.register,
                                     hrmdepartment=instance.hrmdepartment, comment=instance.comment)

                # 如果有预约回访时间，则向回访表里插入回访记录
                if s_callback:
                    callback.objects.create(client=instance.client, dept_id=treatdept, order=instance.order,
                                            times=instance.times, residue=instance.residue - amount, begindate=s_callback,
                                            enddate=e_callback, ispreorder=instance.isproorder,
                                            treat=instance,callbacktype=2,hrmdepartment=instance.hrmdepartment)

                # 如果有预约治疗时间，则向治疗表里的第一条记录更新预约标志
                if s_treat:
                    instance.isappoint = 1
                    instance.begindate = s_treat
                    instance.enddate = e_treat
                    instance.save()
                else:
                    instance.isappoint = 0
                    instance.begindate = None
                    instance.enddate = None
                    instance.save()

                # 如果禁忌症不为空 插入客户禁忌症表
                if len(jinjizheng) > 0:
                    client_jinjizheng.objects.filter(clientregister=instance.register).delete()
                    for item in jinjizheng:
                        client_jinjizheng.objects.create(clientregister=instance.register, jinjizheng_id=item, adduser=user)
                        client_jinjizheng_log.objects.create(client_register=instance.register, jinjizheng_id=item, adduser=user,
                                                             type=1)

                instance.treattype = flag
                instance.amount = 1
                instance.residue = instance.residue - 1
                instance.treatdept_id = treatdept
                instance.operator_id = operator
                instance.operatedate = operatedate
                instance.comment = comment
                instance.save()

        elif action == 6: # 点击除套餐外的其他产后治疗历史记录的修改
            amount = self.initial_data.get('amount')
            energy = self.initial_data.get('energy')
            jinjizheng = self.initial_data.get('jinjizheng')
            operator = self.initial_data.get('operator')
            operatedate = self.initial_data.get('operatedate')
            report = self.initial_data.get('report')
            treatdept = self.initial_data.get('treatdept')
            wendu = self.initial_data.get('wendu')
            yaling = self.initial_data.get('yaling')
            comment = self.initial_data.pop('comment')

            if instance.amount == amount:  # 治疗次数未修改
                if len(jinjizheng) > 0: # 如果禁忌症不为空 插入客户禁忌症表
                    client_jinjizheng.objects.filter(clientregister=instance.register).delete()
                    for item in jinjizheng:
                        client_jinjizheng.objects.create(clientregister=instance.register,
                                                         jinjizheng_id=item,adduser=user)
                        client_jinjizheng_log.objects.create(client_register=instance.register,
                                                             jinjizheng_id=item,adduser=user,type=1)
                instance.energe = energy
                instance.report = report
                instance.wendu = wendu
                instance.yaling = yaling
                instance.treatdept_id = treatdept
                instance.operator_id = operator
                instance.operatedate = operatedate
                instance.comment = comment
                instance.save()
            else:
                if amount - instance.amount <= instance.residue:
                    par_obj = treat.objects.filter(pk=instance.parent_id).first()
                    par_obj.residue = par_obj.residue - amount + instance.amount
                    par_obj.save()

                    if len(jinjizheng) > 0:
                        client_jinjizheng.objects.filter(clientregister=instance.register).delete()
                        for item in jinjizheng:
                            client_jinjizheng.objects.create(clientregister=instance.register,
                                                             jinjizheng_id=item,adduser=user)
                            client_jinjizheng_log.objects.create(client_register=instance.register,
                                                                 jinjizheng_id=item,adduser=user,type=1)
                    instance.amount = amount
                    instance.residue = instance.residue - amount + instance.amount
                    instance.energe = energy
                    instance.report = report
                    instance.wendu = wendu
                    instance.yaling = yaling
                    instance.treatdept_id = treatdept
                    instance.operator_id = operator
                    instance.operatedate = operatedate
                    instance.comment = comment
                    instance.save()


        return instance


class treat_historySerializer(serializers.ModelSerializer):
    """
    检查治疗历史记录
    """
    clientname =  serializers.SerializerMethodField()
    orderuser = serializers.SerializerMethodField()
    parentname = serializers.SerializerMethodField()
    projectname = serializers.SerializerMethodField()
    isacquire = serializers.SerializerMethodField()
    treatdeptname = serializers.SerializerMethodField()
    operatename = serializers.SerializerMethodField()

    def get_clientname(self, obj):
        return obj.client.name

    def get_orderuser(self, obj):
        return obj.adduser.name

    def get_parentname(self, obj):
        name = ''
        if obj.parent:
            name = obj.parent.project.name
        return name

    def get_projectname(self, obj):
        return obj.project.name

    def get_isacquire(self, obj):
        val = 0
        if obj.parent:
            val = obj.parent.isacquire
        return val

    def get_treatdeptname(self, obj):
        name = ''
        deptobj = obj.treatdept
        if deptobj:
            name = deptobj.deptdict.name
        return name

    def get_operatename(self, obj):
        name = ''
        operateobj = obj.operator
        if operateobj:
            name = operateobj.name
        return name

    class Meta:
        model = treat
        fields = '__all__'


class callbackSerializer(serializers.ModelSerializer):
    """
    客户回访
    """
    clientname = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    taishu = serializers.SerializerMethodField()
    preBMI = serializers.SerializerMethodField()
    hftype = serializers.SerializerMethodField()
    hytype = serializers.SerializerMethodField()
    ordertype = serializers.SerializerMethodField()
    hfstatus = serializers.SerializerMethodField()
    deptname = serializers.SerializerMethodField()
    handlemanname = serializers.SerializerMethodField()
    execute = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()

    def get_clientname(self, obj):
        return obj.client.name

    def get_age(self,obj):
        nianling = ''
        if obj.client.birthDate:
            nianling = datetime.datetime.today().year - obj.client.birthDate.year
        return  nianling

    def get_taishu(self,obj):
        return  obj.order.register.taishu

    def get_preBMI(self,obj):
        return  obj.order.register.preBMI

    def get_hftype(self, obj):
        name = ''
        type = obj.callbacktype
        if type == 0:
            name = '营养回访'
        elif type == 1:
            name = '心理回访'
        else:
            name = '产康回访'
        return name

    def get_hytype(self, obj):
        name = ''
        type = obj.ishospital
        if type == 0:
            name = '未回院'
        else:
            name = '已回院'
        return name

    def get_ordertype(self, obj):
        name = ''
        type = obj.isacquire
        if type == 0:
            name = '预开单'
        else:
            name = '现场缴费'
        return name

    def get_hfstatus(self, obj):
        name = ''
        type = obj.isfinish
        if type == 0:
            name = '未回访'
        else:
            name = '已回访'
        return name

    def get_deptname(self, obj):
        name = ''
        deptobj = obj.dept
        if deptobj:
            name = deptobj.deptdict.name
        return name

    def get_handlemanname(self, obj):
        name = ''
        operateobj = obj.handleman
        if operateobj:
            name = operateobj.name
        return name

    def get_execute(self, obj):
        str = ''
        name = obj.execute
        if name == 1:
            str = '好'
        elif name == 2:
            str = '一般'
        elif name == 3:
            str = '差'
        elif name == 4:
            str = '完全未执行'
        return str

    def get_weight(self, obj):
        str = ''
        name = obj.weight
        if name != 0:
            str = name
        return str

    class Meta:
        model = callback
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        treat_id = self.initial_data.pop('treat_id')
        treatobj = treat.objects.get(pk=treat_id)
        begindate = validated_data.pop('begindate')
        enddate = validated_data.pop('enddate')
        obj = callback.objects.create(client=treatobj.client,dept=treatobj.register.dept,order=treatobj.order,
                                        times=treatobj.times,residue=treatobj.residue,begindate=begindate,
                                        enddate=enddate,ispreorder=treatobj.isproorder,callbacktype=0,
                                        treat=treatobj,hrmdepartment=treatobj.hrmdepartment)

        return obj

    def update(self, instance, validated_data):
        user = self.context['request'].user
        handleman = userProfile.objects.filter(user=user).first()
        action = self.initial_data.pop('action')

        if action == 1: # 回院
            ishospital = self.initial_data.pop('ishospital')
            hospitaldate = self.initial_data.get('hospitaldate', 0)
            instance.ishospital = ishospital
            instance.hospitaldate = hospitaldate
            instance.save()

        elif action == 0: # 回访
            hftype = self.initial_data.get('hftype')
            begindate = self.initial_data.get('nextbegindate')
            enddate = self.initial_data.get('nextenddate')
            s_treat = self.initial_data.get('s_treat')
            e_treat = self.initial_data.get('e_treat')
            execute = self.initial_data.get('zhixing')
            weight = self.initial_data.get('weight')
            healthtype = self.initial_data.get('healthtype')
            burufs = self.initial_data.get('burufs')
            breast = self.initial_data.get('breast')
            milk = self.initial_data.get('milk')
            rutou = self.initial_data.get('rutou')
            elu = self.initial_data.get('elu')
            yinshi = self.initial_data.get('yinshi')
            sleep = self.initial_data.get('sleep')
            huiyin = self.initial_data.get('huiyin')
            treat_id = self.initial_data.get('treat')
            order_id = self.initial_data.get('order')
            comment = self.initial_data.get('comment')
            finish = self.initial_data.get('finish',0)

            if hftype == '营养回访':
                instance.execute = execute
                instance.weight = weight

                if finish == 1:
                    instance.isfinish = 1
                    instance.handleman = handleman
                    instance.handledate = date.today()
                    counts = callback.objects.filter(order_id=order_id).count()
                    if counts == 1:
                        orderobj = order.objects.get(pk=order_id)
                        begindate = date.today() + timedelta(days=30)
                        startdate = begindate.strftime('%Y-%m-%d')
                        enddate = date.today() + timedelta(days=37)
                        jieshudate = enddate.strftime('%Y-%m-%d')

                        callback.objects.create(client=orderobj.client, dept=orderobj.register.dept, order=orderobj,
                                            times=orderobj.times, residue=orderobj.residue, begindate=startdate,
                                            enddate=jieshudate, ispreorder=orderobj.isproorder,treat_id=treat_id,
                                            healthtype=healthtype,callbacktype=0,hrmdepartment=orderobj.hrmdepartment)
                    elif counts == 2:
                        if s_treat:
                            ordobj = order.objects.get(pk=order_id)
                            treatobj = treat.objects.get(pk=treat_id)

                            # 先插入预约治疗记录
                            treatobj.isappoint = 1
                            treatobj.begindate = s_treat
                            treatobj.enddate = e_treat
                            treatobj.save()

                            ksdate = datetime.datetime.strptime(s_treat, '%Y-%m-%d') + timedelta(days=-7)
                            startdate = ksdate.strftime('%Y-%m-%d')
                            jsdate = datetime.datetime.strptime(e_treat, '%Y-%m-%d') + timedelta(days=-7)
                            jieshudate = jsdate.strftime('%Y-%m-%d')

                            # 再插入预约回访记录--在预约治疗前7天
                            callback.objects.create(client=ordobj.client, dept=ordobj.register.dept, order=ordobj,
                                                    times=ordobj.times, residue=ordobj.residue, begindate=startdate,
                                                    enddate=jieshudate, ispreorder=ordobj.isproorder,treat_id=treat_id,
                                                    healthtype=healthtype,callbacktype=0,
                                                    hrmdepartment=ordobj.hrmdepartment)
            else:
                instance.burufs = burufs
                instance.breast = breast
                instance.milk = milk
                instance.rutou = rutou
                instance.elu = elu
                instance.yinshi = yinshi
                instance.sleep = sleep
                instance.huiyin = huiyin

                if finish == 1:
                    instance.isfinish = 1
                    instance.handleman = handleman
                    instance.handledate = date.today()

                ordobj = order.objects.get(pk=order_id)
                treatobj = treat.objects.get(pk=treat_id)

                if begindate: # 预约回访记录
                    callback.objects.create(client=ordobj.client, dept=ordobj.register.dept, order=ordobj,
                                            times=ordobj.times, residue=ordobj.residue, begindate=begindate,
                                            enddate=enddate, ispreorder=ordobj.isproorder,treat=treatobj,
                                            healthtype=healthtype,callbacktype=2,hrmdepartment=ordobj.hrmdepartment)

                if s_treat: # 预约治疗记录
                    treatobj.isappoint = 1
                    treatobj.begindate = s_treat
                    treatobj.enddate = e_treat
                    treatobj.save()

            instance.comment = comment
            instance.save()
        return instance

class surveySerializer(serializers.ModelSerializer):
    """
    问卷字典
    """
    class Meta:
        model = survey
        fields = '__all__'


class survey_title_answerSerializer(serializers.ModelSerializer):
    """
    题目选项及分数
    """
    class Meta:
        model = survey_title_answer
        fields = '__all__'

class survey_titleSerializer(serializers.ModelSerializer):
    """
    问卷题目
    """
    items = serializers.SerializerMethodField()
    val = serializers.SerializerMethodField()

    def get_items(self, obj):
        exsists = survey_title_answer.objects.filter(title=obj)
        json = survey_title_answerSerializer(exsists, many=True, context={'request': self.context['request']}).data
        return json

    def get_val(self, obj):
        treat_id = self.context['request'].query_params.get('treat_id')
        if treat_id:
            resultobj = survey_result.objects.filter(treat_id=treat_id,title_id=obj.id).first()
            if obj.type == 0:
                if resultobj:
                    return resultobj.item_id
                else:
                    return None
            elif obj.type == 1:
                if resultobj:
                    return resultobj.score
                else:
                    return None
            else:
                return None
        else:
            return None

    class Meta:
        model = survey_title
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        adduser = userProfile.objects.filter(user=user).first()
        survey_id = self.initial_data.get('survey_id')
        treat_id = self.initial_data.get('treat_id')
        type = self.initial_data.get('type')
        titles = self.initial_data.get('titles')
        survey_result.objects.filter(treat_id=treat_id,survey_id=survey_id).delete() #先删除

        for item in titles:
            type = item.get('type',1)
            if type == 0: # 单选
                itemid = item.get('val')
                itemobj = survey_title_answer.objects.get(pk=itemid)
                survey_result.objects.create(treat_id=treat_id,survey_id=survey_id,title_id=item.get('id'),
                                             item_id=itemid,score=itemobj.score,adduser=adduser)
            elif type == 1: # 填空
                survey_result.objects.create(treat_id=treat_id, survey_id=survey_id, title_id=item.get('id'),
                                             score=item.get('val',0), adduser=adduser)
        # 求问卷得分
        if survey_id < 4:
            totalobj = survey_result.objects.filter(survey_id=survey_id,treat_id=treat_id).aggregate(totalscore=Sum('score'))
            total = totalobj.get('totalscore')
            treat_survey.objects.filter(survey_id=survey_id,treat_id=treat_id).update(score=total)
        elif survey_id == 4:
            psqi_result.objects.filter(survey_id=survey_id,treat_id=treat_id).delete()

            # A.睡眠质量
            item6_obj = survey_result.objects.filter(title_id=43,survey_id=survey_id,treat_id=treat_id).first()
            psqi_result.objects.create(name='睡眠质量',survey_id=survey_id,treat_id=treat_id,score=item6_obj.score)

            # B.入睡时间
            item2_obj = survey_result.objects.filter(title_id=29, survey_id=survey_id, treat_id=treat_id).first()
            item5a_obj = survey_result.objects.filter(title_id=33, survey_id=survey_id, treat_id=treat_id).first()
            item25a_score = item2_obj.score + item5a_obj.score
            num =  0
            if item25a_score >= 1 and item25a_score <= 2:
                num = 1
            elif item25a_score >= 3 and item25a_score <= 4:
                num = 2
            elif item25a_score >= 5 and item25a_score <= 6:
                num = 3
            else:
                num = 0
            psqi_result.objects.create(name='入睡时间', survey_id=survey_id, treat_id=treat_id, score=num)

            # C.睡眠时间
            item4_obj = survey_result.objects.filter(title_id=31, survey_id=survey_id, treat_id=treat_id).first()
            num = 0
            if item4_obj.score > 7:
                num = 0
            elif item4_obj.score > 6 and item4_obj.score <=7:
                num = 1
            elif item4_obj.score >= 5 and item4_obj.score <= 6:
                num = 2
            elif item4_obj.score < 5:
                num = 3
            psqi_result.objects.create(name='睡眠时间', survey_id=survey_id, treat_id=treat_id, score=num)

            # D.睡眠效率
            item1_obj = survey_result.objects.filter(title_id=28, survey_id=survey_id, treat_id=treat_id).first()
            item3_obj = survey_result.objects.filter(title_id=30, survey_id=survey_id, treat_id=treat_id).first()
            item4_obj = survey_result.objects.filter(title_id=31, survey_id=survey_id, treat_id=treat_id).first()
            xiaolv = item4_obj.score/(item3_obj.score - item1_obj.score)
            num = 0
            if xiaolv > 0.85:
                num = 0
            elif xiaolv > 0.75 and xiaolv <= 0.85:
                num = 1
            elif xiaolv >= 0.65 and xiaolv <= 0.75:
                num = 2
            elif xiaolv < 0.65:
                num = 3
            psqi_result.objects.create(name='睡眠效率', survey_id=survey_id, treat_id=treat_id, score=num)

            # E.睡眠障碍
            item5b5j_obj = survey_result.objects.filter(treat_id=treat_id, survey_id=survey_id,title_id__gte=32,
                                                        title_id__lte=42).aggregate(zongfen=Sum('score'))
            item5b5j_score = item5b5j_obj.get('zongfen')
            num = 0
            if item5b5j_score >=1 and  item5b5j_score <= 9:
                num = 1
            elif item5b5j_score >=10 and  item5b5j_score <= 18:
                num = 2
            elif item5b5j_score >=19 and  item5b5j_score <= 27:
                num = 3
            else:
                num = 0
            psqi_result.objects.create(name='睡眠障碍', survey_id=survey_id, treat_id=treat_id, score=num)

            # F.催眠药物
            item7_obj = survey_result.objects.filter(title_id=44, survey_id=survey_id, treat_id=treat_id).first()
            psqi_result.objects.create(name='催眠药物', survey_id=survey_id, treat_id=treat_id, score=item7_obj.score)

            # G.日间功能障碍
            item89_obj = survey_result.objects.filter(treat_id=treat_id, survey_id=survey_id,title_id__gte=45,
                                                      title_id__lte=46).aggregate(zongfen=Sum('score'))
            item89_score = item89_obj.get('zongfen')
            num = 0
            if item89_score >= 1 and item89_score <= 2:
                num = 1
            elif item89_score >= 3 and item89_score <= 4:
                num = 2
            elif item89_score >= 5 and item89_score <= 6:
                num = 3
            else:
                num = 0
            psqi_result.objects.create(name='日间功能障碍', survey_id=survey_id, treat_id=treat_id, score=num)

            totalobj = psqi_result.objects.filter(survey_id=survey_id, treat_id=treat_id).\
                                                  aggregate(totalscore=Sum('score'))
            total = totalobj.get('totalscore')
            treat_survey.objects.filter(survey_id=survey_id, treat_id=treat_id).update(score=total)

        obj = survey_title.objects.all().first()
        return obj

class treat_surveySerializer(serializers.ModelSerializer):
    """
    治疗所需问卷
    """
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.survey.name

    class Meta:
        model = treat_survey
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        adduser = userProfile.objects.filter(user=user).first()
        surveys = self.initial_data.get('surveys')
        treat_id = self.initial_data.get('treat_id')
        obj = {}
        for item in surveys:
            obj = treat_survey.objects.create(treat_id=treat_id,survey_id=item.get('id'),
                                              adduser=adduser,valuedate=date.today())
        return obj

class APIRequestLogSerializer(serializers.ModelSerializer):
    """
    操作日志序列化
    """
    name = serializers.SerializerMethodField()
    class Meta:
        model =  APIRequestLog
        fields = '__all__'

    def get_name(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return ''