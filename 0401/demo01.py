"""
python高级：属性与方法
"""

class Good():
    """
    动态的添加属性方法
    """
    def __init__(self,_name):
        self.name = _name

a1 = Good("shanghai")
print(a1.name)