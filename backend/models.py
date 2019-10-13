from django.db import models
from django.contrib.auth.models import User,Group
import uuid

# Create your models here.

class Permission(models.Model):
    test = models.IntegerField(default=1,verbose_name='test')
    class Meta:
         permissions = (
            # ('views_schedualodddual', '单双周排班模板定制'),
            # ('views_schedual', '实际日期排班安排'),
            # ('views_dept', '部门管理'),
            # ('views_group', '角色管理'),
            # ('views_employee', '员工管理'),
            # ('doctor_platform', '医生工作平台'),
            # ('jiaobanPatientViewSet', '医生交班记录'),
            # ('nurse', '护士工作平台'),
            # ('patient', '患者管理'),
            # ('drug_person', '自备药'),
            ('tuitionFee', '带教费'),
            # ('jiaoban_nurse', '护士交班记录'),
            # ('jiaobanDevice', '设备交班记录'),
            # ('drug', '药品管理'),
            # ('material', '耗材管理'),
            # ('device', '设备管理'),
            ('performance_dict', '绩效字典'),
            ('benefit_dict', '工资福利字典'),
            # ('expense', '费用管理'),
            # ('prepayment', '预交金管理'),
            ('performance', '中心绩效'),
            ('benefit', '中心工资福利字典'),
            # ('project_dict', '项目字典'),
            ('huiyuan_set', '回院设置'),
            ('client', '客户档案'),
            ('order', '宣教开单'),
            ('treat', '检查治疗'),
            ('callback', '客户回访'),
            # ('analyseCaP', '钙磷乘积分析'),
            # ('AlarmLab', '检验预警分析'),
            # ('analyseBfzBymonth', '并发症分析'),
            # ('analyseBloodPressure', '血压异常分析'),
            # ('analyseByYuanfa', '原发病分析'),
            # ('analyseZhuangui', '转归分析'),
            # ('analyseZhengzhuang', '症状分析'),
            # ('analyseDrugByyear', '药品分析'),
            # ('analysedrug', '药品明细汇总'),
            # ('analysematerial', '耗材明细汇总'),
            # ('analyseDrugstock', '药品出入库分析'),
            # ('analyseMaterialstock', '耗材出入库分析'),
            # ('analyseDeptCharge', '科室收费分析'),
            # ('deptChargeBymonth', '科室收费按月分析'),
            #
            ('tuition_dict', '带教费类型'),
            ('project_dict', '项目字典'),
            ('project', '中心项目'),
            ('finance_month', '财务月'),
            ('coo_hospital', '合作医院'),
            ('dept_dict', '科室字典'),
            ('post_dict', '岗位字典'),
            ('dept', '中心科室'),
            # ('maintainence', '设备保养字典'),
            ('organization', '组织机构设置'),
            ('xlog', '操作日志'),
            #
            # ('depart', '部门管理'),
            ('userProfile', '员工档案'),
            # ('role', '角色管理'),
         )

class Menus(models.Model):
    '''
    动态菜单
    '''
    name = models.CharField(max_length=64)
    # 绝对url和动态url
    url_type_choices = ((0, 'absolute'), (1, 'dynamic'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    path = models.CharField(max_length=128, default='')

    # route = models.CharField(max_length=128,default='')
    parent_id = models.CharField(null=True, blank=True, max_length=20)
    menu_id = models.IntegerField(default='', null=True, blank=True)

    def __str__(self):
        return self.name

class GroupMenu(models.Model):
    '''
    角色菜单对照表
    '''
    group = models.ForeignKey(Group, default=1, verbose_name="用户")
    # 一个角色可以访问多个菜单，一个菜单可以被多个角色访问
    menus = models.ForeignKey(Menus, default=1, blank=True, verbose_name='动态菜单')
      # 菜单是否可见（是否有访问该菜单权限）
    isvisible = models.BooleanField(default=1)
    # url = models.CharField(max_length=160,default='')
    # btn_label = models.CharField(max_length=160,default='')
    # browser = models.BooleanField(default=False)
    # menuself = models.BooleanField(default=False)

class GroupChildMenu(models.Model):
    '''
    角色菜单与子菜单对照表，通过权限设置界面插入
    '''
    groupmenu = models.ForeignKey(GroupMenu, default=1, blank=True, verbose_name='角色菜单')
    # 子菜单是否可见
    isvisible = models.BooleanField(default=1)
    # 子菜单path
    path = models.CharField(max_length=160,blank=True)
    name = models.CharField(max_length=160,blank=True,default='')
    title = models.CharField(max_length=160,default='')
    icon =  models.CharField(max_length=160,default='')
    component=  models.CharField(max_length=260,default='')
    child_menu_id = models.IntegerField(default=1,verbose_name='childid')

class ChildMenu(models.Model):
    '''
    基础数据，菜单与子菜单对照表，手工插入
    '''
    menu = models.ForeignKey(Menus, default=1, blank=True, verbose_name='菜单')
    # 子菜单是否可见
    isvisible = models.BooleanField(default=False)
    # 子菜单path
    path = models.CharField(max_length=160,blank=True)
    name = models.CharField(max_length=160,blank=True)
    title = models.CharField(max_length=160,default='')
    icon =  models.CharField(max_length=160,default='')
    component=  models.CharField(max_length=260,default='')
    child_menu_id = models.IntegerField(default=1,verbose_name='childid')
    # 权限字符串，不是外键，不是权限对象
    permission = models.CharField(max_length=100, null=True, blank=True, verbose_name='urr')

class sysRight(models.Model):
    """
    系统基本权限--按钮
    """
    name = models.CharField(max_length=100,verbose_name='权限名称')
    description = models.CharField(max_length=300, verbose_name='权限描述')
    modName = models.CharField(max_length=100, verbose_name='模块名称')
    type = models.IntegerField(default=0,verbose_name='权限类别')

    def __str__(self):
        return self.name

class GroupRight(models.Model):
    '''
    角色按钮对照表
    '''
    group = models.ForeignKey(Group, default=1, verbose_name="角色")
    # 一个角色可以有多个按钮，一个按钮可以被多个角色访问
    rights = models.ForeignKey(sysRight, default=1, blank=True, verbose_name='权限')
    # 按钮是否可见（是否有访问该按钮权限）
    isvisible = models.BooleanField(default=1)

class invoice_dict(models.Model):
    """
    开票名称字典
    """
    name = models.CharField(max_length=200,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

class profit_distri_dict(models.Model):
    """
    利润分成类型
    """
    name = models.CharField(max_length=200,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

class coo_hospital(models.Model):
    """
    合作医院
    """
    name = models.CharField(max_length=200,verbose_name='名称')
    begindate = models.DateField(null=True, blank=True, verbose_name='开始日期')
    enddate = models.DateField(null=True, blank=True, verbose_name='结束日期')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='地址')
    contactman = models.CharField(max_length=60, null=True, blank=True, verbose_name='联系人')
    telphone = models.CharField(max_length=60, null=True, blank=True, verbose_name='电话')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

class project_dict(models.Model):
    """
    公司项目字典
    """
    projectid = models.UUIDField(default=uuid.uuid4,auto_created=True,editable=False,verbose_name='项目id')
    name = models.CharField(max_length=100,verbose_name='名称')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    isindependent = models.BooleanField(default=1,verbose_name='能否独立开单')
    type = models.BooleanField(default=0,verbose_name='是否为套餐')
    amount = models.IntegerField(null=True, blank=True,verbose_name='数量')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')


class invoice_set(models.Model):
    """
    开票设置
    """
    hospital = models.ForeignKey(coo_hospital, default=1, related_name='hzhospital', verbose_name="合作医院")
    invoice_id = models.IntegerField(default=1, null=True, blank=True, verbose_name="开票名称")
    profit_distri_id = models.IntegerField(default=1, null=True, blank=True, verbose_name="利润分成")
    begindate = models.DateField(null=True, blank=True, verbose_name='开始日期')
    enddate = models.DateField(null=True, blank=True, verbose_name='结束日期')
    value = models.FloatField(default=0, null=True, blank=True,verbose_name='数值')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

class dept_dict(models.Model):
    """
    公司科室字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.name

class post_dict(models.Model):
    """
    公司岗位字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.name

class tuition_dict(models.Model):
    """
    带教费类型字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.name

class performance_dict(models.Model):
    """
    绩效字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    def __str__(self):
        return self.name

class benefit_dict(models.Model):
    """
    工资福利字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    def __str__(self):
        return self.name

class client_type(models.Model):
    """
    客户类型字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    def __str__(self):
        return self.name

class dept_client_type(models.Model):
    """
    公司科室客户类型
    """
    deptdict = models.ForeignKey(dept_dict, default=1, null=True, verbose_name="科室")
    clienttype = models.ForeignKey(client_type, null=True, blank=True, verbose_name='客户类型')

    def __str__(self):
        return self.clienttype.name

class jinjizheng(models.Model):
    """
    禁忌症字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    def __str__(self):
        return self.name

class project_jinjizheng(models.Model):
    """
    项目禁忌症
    """
    projectdict = models.ForeignKey(project_dict, null=True,blank=True, verbose_name="项目id")
    jinjizheng = models.ForeignKey(jinjizheng, null=True, blank=True, verbose_name="禁忌症id")
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')


class client_from(models.Model):
    """
    客户来源字典
    """
    name = models.CharField(max_length=100,verbose_name='名称')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    def __str__(self):
        return self.name

class dept_post(models.Model):
    """
    公司科室岗位
    """
    deptdict = models.ForeignKey(dept_dict, default=1, null=True, verbose_name="科室")
    postdict = models.ForeignKey(post_dict, null=True, blank=True, verbose_name='岗位')

    def __str__(self):
        return self.postdict.name


class HrmCompany(models.Model):
    """
    公司总部
    """
    name = models.CharField(max_length=1000,verbose_name='名称')    #不能重
    description = models.CharField(max_length=2000,verbose_name='简称')
    web = models.CharField(max_length=500,verbose_name='公司网址')

    def __str__(self):
        return self.name

class HrmSubCompany(models.Model):
    """
    公司分部
    """
    name = models.CharField(max_length=1000,verbose_name='名称')
    description = models.CharField(max_length=2000,verbose_name='简称')
    companyid = models.IntegerField(null=True, verbose_name='公司总部id')
    supsubcomid = models.IntegerField(null=True, verbose_name='上级分部id')
    url = models.CharField(max_length=1000,verbose_name='url')
    showorder = models.IntegerField(default=0, verbose_name='序号')
    canceled = models.IntegerField(default=0, verbose_name='封存标志')
    code = models.CharField(max_length=500,verbose_name='分部编号')
    tlevel = models.IntegerField(default=0,verbose_name='等级')

    def __str__(self):
        return self.name

class HrmDepartment(models.Model):
    """
    公司部门
    """
    name = models.CharField(max_length=1000,verbose_name='名称')
    description = models.CharField(max_length=1000,verbose_name='标识')
    subcompanyid = models.IntegerField(null=True, verbose_name='所属分部id')
    supdepid = models.IntegerField(null=True, verbose_name='所属部门id')
    allsupdepid = models.CharField(null=True, max_length=2000,verbose_name='所有上级部门id')
    showorder = models.IntegerField(default=0, verbose_name='序号')
    canceled = models.IntegerField(default=0, verbose_name='封存标志')
    code = models.CharField(max_length=500,verbose_name='分部编号')
    bmfzr = models.CharField(null=True, max_length=1000,verbose_name='负责人')
    bmfgld = models.CharField(null=True, max_length=1000,verbose_name='分管领导')
    tlevel = models.IntegerField(default=0,verbose_name='等级')

    def __str__(self):
        return self.name

class subCompanyField(models.Model):
    """
    公司分部字段显示属性
    """
    name = models.CharField(max_length=100,verbose_name='字段名称')
    display = models.CharField(max_length=200,verbose_name='中文名称')
    show = models.BooleanField(default=0,verbose_name='是否显示')
    width = models.IntegerField(default=60,verbose_name='宽度')

    def __str__(self):
        return self.name

class UserDepartment(models.Model):
    """
    员工管理的中心--数据权限
    """
    user = models.ForeignKey(User, default=1, related_name='employee', null=True, verbose_name="员工")
    dep = models.ForeignKey(HrmDepartment, to_field='id', related_name='depCenter', null=True, blank=True, verbose_name='中心')

    def __str__(self):
        return self.user.username

class dept(models.Model):
    """
    中心科室字典
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    deptdict = models.ForeignKey(dept_dict, default=1, verbose_name="科室id")
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.deptdict.name

class finance_month(models.Model):
    """
    财务月
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='月份')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.name

class project(models.Model):
    """
    中心项目字典
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, null=True, blank=True, verbose_name='中心')
    projectid = models.UUIDField(default=uuid.uuid4,auto_created=True,editable=False,verbose_name='项目id')
    name = models.CharField(max_length=100,verbose_name='名称')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    isindependent = models.BooleanField(default=1,verbose_name='能否独立开单')
    type = models.BooleanField(default=0,verbose_name='是否为套餐')
    amount = models.IntegerField(null=True, blank=True,verbose_name='数量')
    price = models.FloatField(null=True, blank=True, verbose_name='价格')
    flag = models.BooleanField(default=0,verbose_name='是否为系统套餐')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')


class tuitionFee(models.Model):
    """
    中心带教费
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    dept = models.ForeignKey(dept, default=1, verbose_name="科室id")
    tuition = models.ForeignKey(tuition_dict, default=1, verbose_name="带教费类型id")
    value = models.FloatField(default=0, verbose_name='数值')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')


class tuitionFee_detail(models.Model):
    """
    中心带教费详细
    """
    tuitionfee = models.ForeignKey(tuitionFee, default=1, verbose_name="带教费id")
    tuition = models.ForeignKey(tuition_dict, default=1, verbose_name="带教费类型id")
    project = models.ForeignKey(project, default=1, verbose_name="项目id")
    value = models.FloatField(default=0, verbose_name='数值')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

class performance(models.Model):
    """
    中心绩效字典
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    performancedict = models.ForeignKey(performance_dict, default=1, verbose_name="绩效id")
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.performancedict.name

class benefit(models.Model):
    """
    中心工资福利字典
    """
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    benefitdict = models.ForeignKey(benefit_dict, default=1, verbose_name="绩效id")
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.benefitdict.name

class huiyuan_set(models.Model):
    """
    回院设置
    """
    projectdict = models.ForeignKey(project_dict, default=1, verbose_name="项目id")
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.projectdict.name

class userProfile(models.Model):
    """
    员工表
    """
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='姓名')
    sex = models.CharField(max_length=10, null=True, blank=True,verbose_name='性别')
    birthDate = models.DateField(null=True, blank=True,verbose_name='出生日期')
    profession = models.CharField(max_length=100, null=True, blank=True,verbose_name='职称')
    education = models.CharField(max_length=100, null=True, blank=True,verbose_name='学历')
    type = models.CharField(max_length=10, null=True, blank=True,verbose_name='职工类型')
    phone1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='电话1')
    phone2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='电话2')
    hiredate = models.DateField(null=True, blank=True,verbose_name='入职日期')
    state = models.SmallIntegerField(default=1, verbose_name='入职状态')
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

class client(models.Model):
    """
    客户表
    """
    name = models.CharField(max_length=100,verbose_name='姓名')
    clientno = models.UUIDField(default=uuid.uuid4, auto_created=True, editable=False, verbose_name='客户编号')
    sex = models.CharField(max_length=10, null=True, blank=True,verbose_name='性别')
    birthDate = models.DateField(null=True, blank=True,verbose_name='出生日期')
    nation = models.SmallIntegerField(default=1,null=True, blank=True,verbose_name='民族')
    profession = models.SmallIntegerField(default=1,null=True, blank=True, verbose_name='职业')
    education = models.SmallIntegerField(default=1,null=True, blank=True, verbose_name='学历')
    phone1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='电话1')
    phone2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='电话2')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='家庭住址')
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    adduser = models.ForeignKey(User, default=1, verbose_name="添加人id")
    adddate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='添加日期')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

class client_register(models.Model):
    """
    客户登记表
    """
    client = models.ForeignKey(client, default=1, verbose_name="客户id")
    dept = models.ForeignKey(dept, null=True, blank=True, verbose_name="登记科室id")
    client_type = models.SmallIntegerField(null=True, blank=True, verbose_name="客户类型")
    registerdate = models.DateField(null=True, blank=True, verbose_name='登记日期')
    lastyuejing = models.DateField(null=True, blank=True, verbose_name='末次月经')
    yunci = models.IntegerField(null=True, blank=True, verbose_name='孕次')
    chanci = models.IntegerField(null=True, blank=True, verbose_name='产次')
    taishu = models.SmallIntegerField(null=True, blank=True, verbose_name='胎数')
    height = models.FloatField(null=True, blank=True, verbose_name='身高cm')
    preweight = models.FloatField(null=True, blank=True, verbose_name='孕前体重kg')
    preBMI = models.FloatField(null=True, blank=True, verbose_name='孕前BMI')
    workqiangdu = models.SmallIntegerField(null=True, blank=True, verbose_name='工作强度')
    sporttype = models.SmallIntegerField(null=True, blank=True, verbose_name='运动类型')
    sportttime = models.SmallIntegerField(null=True, blank=True, verbose_name='运动时间')
    frequency = models.SmallIntegerField(null=True, blank=True, verbose_name='运动频率')
    healthtype = models.CharField(max_length=500, null=True, blank=True, verbose_name='健康类型')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='家长手机')
    fenmiandate = models.DateField(null=True, blank=True, verbose_name='分娩日期')
    fenmiantype = models.SmallIntegerField(null=True, blank=True, verbose_name='分娩方式')
    burutype = models.SmallIntegerField(null=True, blank=True, verbose_name='哺乳方式')
    shoushudate = models.DateField(null=True, blank=True, verbose_name='手术日期')
    shoushuype = models.SmallIntegerField(null=True, blank=True, verbose_name='手术方式')
    weight = models.FloatField(null=True, blank=True, verbose_name='当前体重kg')
    BMI = models.FloatField(null=True, blank=True, verbose_name='当前BMI')
    sourcedept = models.SmallIntegerField(null=True, blank=True, verbose_name="来源科室id")
    yunzhou = models.IntegerField(null=True, blank=True, verbose_name='孕周')
    chanhouzhouqi = models.IntegerField(null=True, blank=True, verbose_name='产后周期')
    ganyutype = models.SmallIntegerField(null=True, blank=True, verbose_name='干预方式')
    diagnose = models.CharField(max_length=500, null=True, blank=True, verbose_name='诊断')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')

class client_jinjizheng(models.Model):
    """
    客户禁忌症表
    """
    clientregister = models.ForeignKey(client_register, default=1, verbose_name="客户登记id")
    jinjizheng = models.ForeignKey(jinjizheng, null=True, blank=True, verbose_name="禁忌症id")
    adduser = models.ForeignKey(User, default=1, verbose_name="添加人id")
    adddate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='添加日期')

class client_jinjizheng_log(models.Model):
    """
    客户禁忌症表
    """
    client_register = models.ForeignKey(client_register, default=1, verbose_name="客户id")
    jinjizheng = models.ForeignKey(jinjizheng, null=True, blank=True, verbose_name="禁忌症id")
    type = models.SmallIntegerField(null=True, blank=True, verbose_name="操作类型")
    adduser = models.ForeignKey(User, default=1, verbose_name="添加人id")
    adddate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='添加日期')

class order(models.Model):
    """
    开单
    """
    client = models.ForeignKey(client, default=1, verbose_name="客户id")
    register = models.ForeignKey(client_register, null=True, blank=True, verbose_name="客户登记id")
    marketdept = models.ForeignKey(dept, related_name='market_dept',null=True, blank=True, verbose_name="宣教科室id")
    marketpost = models.ForeignKey(post_dict, related_name='market_post', null=True, blank=True, verbose_name="宣教岗位id")
    marketman = models.ForeignKey(userProfile, related_name='market_man',null=True, blank=True, verbose_name="宣教人id")
    marketdate = models.DateField(null=True, blank=True, verbose_name='宣教日期')
    orderdept = models.ForeignKey(dept, related_name='order_dept',null=True, blank=True, verbose_name="开单科室id")
    orderpost = models.ForeignKey(post_dict, related_name='order_post', null=True, blank=True, verbose_name="开单岗位id")
    adduser = models.ForeignKey(userProfile, related_name='add_user',null=True, blank=True, verbose_name="开单人id")
    # orderdate = models.DateField(null=True, blank=True, verbose_name='开单日期')
    times = models.IntegerField(default=0,verbose_name='开单次数')
    project = models.ForeignKey(project, null=True, blank=True, verbose_name="开单项目id")
    issuccess = models.SmallIntegerField(default=1, verbose_name="宣教是否成功")
    reason = models.SmallIntegerField(null=True, blank=True, verbose_name="宣教失败原因")
    issell = models.SmallIntegerField(default=0, verbose_name="是否需宣教")
    residue = models.IntegerField(default=0,verbose_name='剩余次数')
    receivable = models.FloatField(default=0,verbose_name='应收金额')
    discount = models.FloatField(default=0, verbose_name='优惠金额')
    receipts = models.FloatField(default=0, verbose_name='实收金额')
    isproorder = models.SmallIntegerField(default=0, verbose_name="是否立即治疗")
    isacquire = models.SmallIntegerField(default=0, verbose_name="是否收单")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')
    type = models.SmallIntegerField(default=0, verbose_name="是否套餐")
    price = models.FloatField(default=0, verbose_name='价格')
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')
    iszengpin = models.SmallIntegerField(default=0, verbose_name="是否赠品")

    def __str__(self):
        return self.name


class treat(models.Model):
    """
    治疗
    """
    client = models.ForeignKey(client, default=1, verbose_name="客户id")
    register = models.ForeignKey(client_register, null=True, blank=True, verbose_name="客户登记id")
    adduser = models.ForeignKey(userProfile, related_name='adduser_treat',null=True, blank=True, verbose_name="开单人id")
    orderdept = models.ForeignKey(dept, related_name='orderdept_treat', null=True, blank=True, verbose_name="开单科室id")
    order = models.ForeignKey(order, null=True, blank=True, verbose_name="订单id")
    project = models.ForeignKey(project, null=True, blank=True, verbose_name="开单项目id")
    parent = models.ForeignKey('self',related_name='parent_treat', null=True, blank=True, on_delete=models.CASCADE)
    isacquire = models.SmallIntegerField(default=0, verbose_name="是否收单")
    isproorder = models.SmallIntegerField(default=0, verbose_name="是否立即治疗")
    times = models.IntegerField(default=0, verbose_name='开单次数')
    residue = models.IntegerField(default=0, verbose_name='剩余次数')
    amount = models.IntegerField(default=0, verbose_name='今天治疗次数')
    treatdept = models.ForeignKey(dept, related_name='treat_dept', null=True, blank=True, verbose_name="治疗科室id")
    operator = models.ForeignKey(userProfile, related_name='operate_user', null=True, blank=True, verbose_name="操作人id")
    operatedate = models.DateField(null=True, blank=True, verbose_name='操作日期')
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')
    #add at 2019-09-29
    healthtype = models.CharField(max_length=500, null=True, blank=True, verbose_name='健康类型')
    yunzhou = models.IntegerField(null=True, blank=True, verbose_name='孕周')
    weight = models.FloatField(null=True, blank=True, verbose_name='当前体重kg')
    treatpost = models.ForeignKey(post_dict, related_name='treat_post', null=True, blank=True, verbose_name="治疗岗位id")
    treattype = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='检测类型') #1为初检2为复检
    diagnosis = models.SmallIntegerField(null=True, blank=True, verbose_name='诊断')
    guide = models.CharField(max_length=500, null=True, blank=True, verbose_name='膳食指导')
    # add 2019-10-04
    isappoint = models.SmallIntegerField(default=0, verbose_name="是否预约")
    begindate = models.DateField(null=True, blank=True, verbose_name='预约开始日期')
    enddate = models.DateField(null=True, blank=True, verbose_name='预约结束日期')
    # add 2019-10-07
    energy = models.FloatField(null=True, blank=True, verbose_name='治疗能量')
    report = models.CharField(max_length=500, null=True, blank=True, verbose_name='评估报告')
    wendu = models.FloatField(null=True, blank=True, verbose_name='温度')
    yaling = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name="是否使用引导哑铃")


class callback(models.Model):
    """
    回访
    """
    client = models.ForeignKey(client, default=1, verbose_name="客户id")
    dept = models.ForeignKey(dept, related_name='dept_register', null=True, blank=True, verbose_name="登记科室id")
    treat = models.ForeignKey(treat, null=True, blank=True, verbose_name="治疗id")
    order = models.ForeignKey(order, null=True, blank=True, verbose_name="订单id")
    times = models.IntegerField(default=0, verbose_name='开单次数')
    residue = models.IntegerField(default=0, verbose_name='剩余次数')
    handleman = models.ForeignKey(userProfile, related_name='handle_user', null=True, blank=True, verbose_name="回访人id")
    callbacktype = models.SmallIntegerField(null=True, blank=True, verbose_name="回访类型") # 0营养 1心理其他产康
    ishospital = models.SmallIntegerField(default=0, verbose_name="是否回院")
    hospitaldate = models.DateField(null=True, blank=True, verbose_name='回院日期')
    isfinish = models.SmallIntegerField(default=0, verbose_name="是否完成")
    handledate = models.DateField(null=True, blank=True, verbose_name='回访日期')
    begindate = models.DateField(null=True, blank=True, verbose_name='开始日期')
    enddate = models.DateField(null=True, blank=True, verbose_name='结束日期')
    isacquire = models.SmallIntegerField(default=0, verbose_name="是否收单")
    ispreorder = models.SmallIntegerField(default=0, verbose_name="是否立即治疗")

    healthtype = models.CharField(max_length=500, null=True, blank=True, verbose_name='健康类型')
    diagnosis = models.SmallIntegerField(null=True, blank=True, verbose_name='诊断')
    guide = models.CharField(max_length=500, null=True, blank=True, verbose_name='膳食指导')
    execute = models.SmallIntegerField(default=0, verbose_name="执行情况") # 0 好1一般2差3完全未执行
    weight = models.FloatField(default=0,verbose_name='体重')
    hrmdepartment = models.ForeignKey(HrmDepartment, default=1, verbose_name="中心id")
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')
    # add at 2019-10-07
    burufs = models.SmallIntegerField(null=True, blank=True, verbose_name='哺乳方式')
    breast = models.SmallIntegerField(null=True, blank=True, verbose_name='乳房情况')
    milk = models.SmallIntegerField(null=True, blank=True, verbose_name='乳汁情况')
    rutou = models.SmallIntegerField(null=True, blank=True, verbose_name='乳头情况')
    elu = models.SmallIntegerField(null=True, blank=True, verbose_name='恶露情况')
    yinshi = models.SmallIntegerField(null=True, blank=True, verbose_name='饮食情况')
    sleep = models.SmallIntegerField(null=True, blank=True, verbose_name='睡眠情况')
    huiyin = models.SmallIntegerField(null=True, blank=True, verbose_name='伤口会阴情况')

class survey(models.Model):
    """
    问卷字典
    """
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='问卷名称')
    adduser = models.ForeignKey(userProfile, null=True, blank=True, verbose_name="添加人id")
    adddate = models.DateField(auto_now_add=True, verbose_name='添加日期')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

    def __str__(self):
        return self.name

class survey_title(models.Model):
    """
    问卷题目
    """
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='问卷名称')
    survey = models.ForeignKey(survey, null=True, blank=True, verbose_name="问卷id")
    type = models.SmallIntegerField(default=0,null=True, blank=True, verbose_name='题目类型') #0为单选1为填空2为显示
    adduser = models.ForeignKey(userProfile, null=True, blank=True, verbose_name="添加人id")
    adddate = models.DateField(auto_now_add=True, verbose_name='添加日期')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')
    sn = models.IntegerField(default=0, verbose_name='序列号,每张问卷的所有题目都有唯一序列号')

    def __str__(self):
        return self.title

class survey_title_answer(models.Model):
    # """
    # 问卷题目选项
    # """
    title  = models.ForeignKey(survey_title, null=True, blank=True, verbose_name="题目id")
    answer = models.CharField(max_length=200, null=True, blank=True, verbose_name='题目回答选项')
    score  = models.IntegerField(default=0,verbose_name='每个选项的分数')
    sn = models.IntegerField(default=0, verbose_name='序列号,每张问卷的所有选项都有唯一序列号')

    def __str__(self):
        return self.answer

class treat_survey(models.Model):
    """
    治疗所需问卷
    """
    treat = models.ForeignKey(treat, null=True, blank=True, verbose_name="治疗id")
    survey = models.ForeignKey(survey, null=True, blank=True, verbose_name="问卷id")
    score = models.FloatField(default=0, verbose_name='分数')
    valuedate = models.DateField(null=True, blank=True, verbose_name='评估(干预)日期')
    adduser = models.ForeignKey(userProfile, null=True, blank=True, verbose_name="添加人id")
    adddate = models.DateField(auto_now_add=True,null=True, blank=True, verbose_name='添加日期')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

class survey_result(models.Model):
    """
    问卷答题结果
    """
    treat = models.ForeignKey(treat, null=True, blank=True, verbose_name="治疗id")
    survey = models.ForeignKey(survey, null=True, blank=True, verbose_name="问卷id")
    title = models.ForeignKey(survey_title, null=True, blank=True, verbose_name="题目id")
    item = models.ForeignKey(survey_title_answer, null=True, blank=True, verbose_name="项目id")
    score = models.FloatField(default=0,null=True, blank=True, verbose_name='分数')
    adduser = models.ForeignKey(userProfile, null=True, blank=True, verbose_name="添加人id")
    adddate = models.DateField(auto_now_add=True,null=True, blank=True, verbose_name='添加日期')
    comment = models.CharField(max_length=500, null=True, blank=True,verbose_name='备注')

class psqi_result(models.Model):
    """
    psqi中间结果
    """
    treat = models.ForeignKey(treat, null=True, blank=True, verbose_name="治疗id")
    survey = models.ForeignKey(survey, null=True, blank=True, verbose_name="问卷id")
    name = models.CharField(max_length=100, null=True, blank=True,verbose_name='名称')
    score = models.FloatField(default=0,null=True, blank=True, verbose_name='分数')










