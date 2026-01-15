import os
import json

# TG机器人的令牌，tg找@BotFather创建机器人即可获取
TOKEN = os.getenv('TOKEN', 'token')
# TG用户ID，限制发送消息的用户（环境变量用逗号分隔，如 "123,456"）
ADMIN_IDS = os.getenv('ADMIN_IDS', '').split(',') if os.getenv('ADMIN_IDS') else ['12345678']
# pikpak账号，可以为手机号、邮箱，支持任意多账号（环境变量用逗号分隔）
USER = os.getenv('PIKPAK_USER', '').split(',') if os.getenv('PIKPAK_USER') else ["example_user1", "example_user2"]
# 账号对应的密码，注意与账号顺序对应！！！（环境变量用逗号分隔）
PASSWORD = os.getenv('PIKPAK_PASSWORD', '').split(',') if os.getenv('PIKPAK_PASSWORD') else ["example_password1", "example_password2"]
# 自动删除配置，未配置默认开启自动删除（环境变量为JSON格式，如 '{"user1": "True"}'）
AUTO_DELETE = json.loads(os.getenv('AUTO_DELETE', '{}')) if os.getenv('AUTO_DELETE') else {}
# 以下分别为aria2 RPC的协议（http/https）、host、端口、密钥
ARIA2_HTTPS = os.getenv('ARIA2_HTTPS', 'false').lower() == 'true'
ARIA2_HOST = os.getenv('ARIA2_HOST', 'example.aria2.host')
ARIA2_PORT = os.getenv('ARIA2_PORT', 'port')
ARIA2_SECRET = os.getenv('ARIA2_SECRET', 'secret')
# aria2下载根目录
ARIA2_DOWNLOAD_PATH = os.getenv('ARIA2_DOWNLOAD_PATH', '/mnt/sda1/aria2/pikpak')
# 可以自定义TG API，也可以保持默认
TG_API_URL = os.getenv('TG_API_URL', 'https://api.telegram.org')

# 自定义Pikpak离线下载路径
PIKPAK_OFFLINE_PATH = os.getenv('PIKPAK_OFFLINE_PATH', 'None')