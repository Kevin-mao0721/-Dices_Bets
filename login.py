import ybc_box as box
import secret


class Login:
    def __init__(self, js_sets):
        self.js_sets = js_sets


    def login(self):
        user_data = box.multpasswordbox('请输入账号密码登录(按❌ / Cancel退出)', ['账号', '密码'])
        for user in self.js_sets.users:
            new_user = [data for data in user.values()]
            print(new_user)
            this_name, this_password = new_user[0], new_user[1]
            if this_name == user_data[0] and secret.secret_1024(user_data[1]) == this_password:
                return True, this_name
        return False

    def registered(self):
        users = self.js_sets.read_user_list()
        user_data = box.multpasswordbox('欢迎注册，请输入(按❌ / Cancel退出)', ['账号', '密码'])
        for user in users:
            if user_data is None:
                box.msgbox('您已退出，回头见……！')
                exit()
            # name, password = user.keys()
            if user_data[0] == user['User']:
                return False
            else:
                user_da = {"User": user_data[0], "Password": secret.secret_1024(user_data[1], 'd'), "Money": "100"}
                self.js_sets.write_user_list(user_da)
                return True
