概述
RBAC Server提供权限相关微服务，它包括以下功能： 
* 获取用户的权限 
* 配置用户的角色和权限 
* 资源(菜单)管理 
* 资源的操作行为(READ、EXECUTE…) 
* 预制四个角色维度：机构、产品、渠道、费用 
* 预留字段支持自定义角色维度 
* 角色分组 
* 多租户权限

RBAC Server**不提供**以下功能： 
* 用户管理 
* 机构管理 
* 用户登陆和认证

RBAC Server 依赖以下技术： 
* Spring Boot 1.4.1+ 
* Mysql或者Oracle 
* Redis用于数据缓存 
* Solr集成

模型
在RBAC中最重要的概念包括：用户(User)，角色(Role)，权限(Permission)，资源(Resource)

RBAC总体类图
- User table： 用户表。用户ID，用户Name等属性。 
- Role table : 角色表。角色ID，角色Name，角色Type等属性 
- user_Role table : 用户角色关联表。 用户角色ID,用户ID，角色ID，产品，地区，渠道，费用等属性（因为这里要考虑业务维度，所以加上产品(product)、地区(reginCode)、渠道(channel)、费用(fee)等四个业务维度）（这个思路有待验证）。 
- Permission table : 权限表。权限ID，权限类型（用来判断是哪种资源的权限），权限Name等属性。 
- role_Permission table : 角色权限关联表。 角色ID(FK)，权限ID（FK）等 
- Menu table : 菜单表（资源）。菜单ID,菜单Name,菜单路径Url, 父菜单ID等属性。 
- page_Element table :页面元素表（资源）。页面元素ID，页面元素编码等属性。 
- File table : 文件表（资源）。 文件ID，文件名，文件路径等属性。 
- permission_Menu table : 权限菜单表。 权限ID（FK1），菜单ID（FK2）等属性。 
- permission_Element table：权限页面元素关联表。 权限ID（FK1），页面元素ID（FK2）等属性。 
- permission_File table : 权限文件关联表。权限ID（FK1），文件ID（FK2）等属性。 
- Operation table : 功能操作关联表。操作ID，操作名称，操作编码，拦截URL前缀，父操作ID等属性。 
- permission_Operation table : 权限功能关联表。权限ID（FK1），操作ID（FK2）等属性。

补充：系统Code，如果要给不同系统使用，要在这些类加上区分系统的一个字段System_code。

