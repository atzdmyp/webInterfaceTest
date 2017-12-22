from common import common
from common import configHttp
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = common.get_xls("userCase.xlsx", "login")
localAddAddress_xls = common.get_xls("userCase.xlsx", "addAddress")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    localConfigHttp.set_url()

    # set header
    token = localReadConfig.get_headers("token_v")
    header = {"token": token,
              "SiteUID": "rw",
              "appclientip": "192.168.20.86"}
    localConfigHttp.set_headers(header)

    # set param
    data = {"email": "wangke@dotfashion.cn",
            "password": "123456"}
    localConfigHttp.set_data(data)

    # login
    response = localConfigHttp.post().json()
    print("response"+str(response))
    token = common.get_value_from_return_json(response, "member", "token")
    print("login_token" + token)
    return token


# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = common.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_headers(header)

    # logout
    localConfigHttp.get()


