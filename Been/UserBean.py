class UserBean:
    def __init__(self, id, name, assets, department, description=""):
        self.id = id
        self.name = name
        self.assets = assets
        self.department = department
        self.description = description

    def __str__(self):
        return f"UserBean(id='{self.id}', name='{self.name}', assets='{self.assets}', department='{self.department}', " \
               f"description='{self.description}')"

if __name__ == '__main__':
    user_set = ('zhangsan', '张三', 1, '社畜科', '')
    print(user_set[0])
