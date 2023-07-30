from phapbm import ErrorTemplate

class ValueTypeError(ErrorTemplate):  # 从phapbm包继承错误类模板，具体可见phapbm/__init__.py
    message = "The value's type must not be treenode."
    info_list = ['Try to change the type to "str" or "int".']

class treenode:  # 二叉树类
    '''This class is used to make treenode easier to call and use'''
    def __init__(self, val = 0, left = 0, right = 0):  # 参数分别是，初始节点参数，初始节点左边和右边的值
        self.__t = [str(self.__class__)]  # 定义一个保护类型的变量，用于识别构造函数参数的类型，用列表方便后期扩展以及其他类继承
        if str(type(val)) in self.__t:  # 如果初始节点参数是二叉树类，则报错
            self.val = 0
            raise ValueTypeError()
        else:
            self.val = val
        self.left = left  # 将本类初始节点的左右侧分别赋值
        self.right = right

    def setfromlist(self, val:list):  # 支持从列表设置本二叉树的函数，结构为[参数,左,右]，可嵌套
        '''To set the node from list'''
        self.val = val[0]  # 设置本类初始节点参数
        if str(type(val[1])) == str(type([])):  # 如果初始节点左侧是嵌套的列表
            self.left = treenode().setfromlist(val[1])  # 则创建一个新的本类实例，并将所得列表传参给实例的本函数，并将本类左侧参数赋值
        else:
            self.left = val[1]
        if str(type(val[2])) == str(type([])):  # 原理同上
            self.right = treenode().setfromlist(val[2])
        else:
            self.right = val[2]

    def get_list(self) -> list:  # 从本类获得列表（结构同上）
        l = []  # 定义一个临时的列表
        l.append(self.val)  # 将初始节点参数加入列表
        if str(type(self.left)) in self.__t:  # 如果本类左值的类型也是本类
            l.append(self.left.get_list())  # 则调用该类的本函数取得列表，并加入临时列表
        else:
            l.append(self.left)  # 否则直接加入
        if str(type(self.right)) in self.__t:  # 设置右值原理同上
            l.append(self.right.get_list())
        else:
            l.append(self.right)
        return(l)

    @property
    def listdata(self) -> list:  # 用于获取数的列表信息的只读属性
        return(self.get_list())

    @property
    def depth(self) -> int:  # 用于获取数的深度信息的只读属性
        ld = 0
        if str(type(self.left)) in self.__t:  # 统计左树深度，如果左数类型是二叉树，则调用该类统计深度的属性
            ld += self.left.depth
        else:  # 否则加一
            ld += 1
        rd = 0
        if str(type(self.right)) in self.__t:  # 原理同上
            rd += self.right.depth
        else:
            rd += 1
        return(max(ld, rd))  # 返回左右中的最大值

    def get_depth(self) -> int:  # 对于depth只读属性的函数封装
        return(self.depth)
    #def getnode(self) -> str:
    #    l = self.getlist()
    #    return("")
    #def __str__(self) -> str:
    #    return(self.getnode())
