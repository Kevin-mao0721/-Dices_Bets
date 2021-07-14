import json
import secret
import ybc_box as box


def read_user_list():
    filename = 'users.json'
    with open(filename, 'r') as json_file:
        udict = json.load(json_file)
    return udict


def write_user_list(users, user):
    filename = 'users.json'
    with open(filename, 'w') as json_file:
        users.append(user)
        json.dump(users, json_file)


def login():
    global name
    user_data = box.multpasswordbox('请输入账号密码登录(按❌ / Cancel退出)', ['账号', '密码'])
    for user in users:
        name, password = user.items()
        if user_data[0] in name and secret.secret_1024(user_data[1]) == password[1]:
            return True
    del name
    return False


def registered():
    global users
    users = read_user_list()
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
            write_user_list(users, user_da)
            return True


users = read_user_list()
word = '欢迎进入虚拟赌场，请选择'
while True:
    dz_choice = box.buttonbox(word + '(按❌ / Cancel退出)', ['登录(请注意大小写)', '注册(不支持重复用户名)'])
    if dz_choice is None:
        box.msgbox('您已退出，回头见……！')
        exit()
    elif dz_choice == '登录(请注意大小写)':
        if login():
            box.msgbox('欢迎您，{0}，点击🆗马上开始游戏'.format(name[1]))
            break
        else:
            word = '很抱歉，登录失败，请重试'
            continue
    else:
        if registered():
            word = '注册成功！！请按登录进入游戏'
            continue
        else:
            word = '很抱歉，注册失败(可能重名了)，请重试'
            continue
