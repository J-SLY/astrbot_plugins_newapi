from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口
from astrbot.api import AstrBotConfig
import requests
class MyPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig): # AstrBotConfig 继承自 Dict，拥有字典的所有方法
        super().__init__(context)
        self.config = config
        print(self.config)

    @filter.event_message_type(filter.EventMessageType.PRIVATE_MESSAGE)
    @filter.command("use")
    async def use(self, event: AstrMessageEvent, url:str, token:str, userId:str|int, key:str):
        '''这是一个兑换码兑换指令''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。非常建议填写。
        body=f"""{{
            "key": "{key}"
        }}"""
        response = requests.request("POST", url, data = body, headers = {
            "Content-Type": "application/json", 
            "Authorization": f"Bearer {token}",
            "New-Api-User": f"{userId}"
        })
        
    async def terminate(self):
        '''可选择实现 terminate 函数，当插件被卸载/停用时会调用。'''
