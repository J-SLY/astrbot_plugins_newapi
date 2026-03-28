from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口
import requests
class MyPlugin(Star):
    def __init__(self, context: Context): 
        super().__init__(context)

    @filter.event_message_type(filter.EventMessageType.PRIVATE_MESSAGE)
    @filter.command("login",alias={"登录"})
    async def login(self,event:AstrMessageEvent,token:str,userId:int|str):
        """这是一个登录指令"""
        sendId=await event.get_sender_id()
        await self.put_kv_data(f"{sendId}Token",token)
        await self.put_kv_data(f"{sendId}Token",token)
    @filter.event_message_type(filter.EventMessageType.PRIVATE_MESSAGE)
    @filter.command("exchange",alias={"兑换"})
    async def use(self, event: AstrMessageEvent, key:str):
        '''这是一个兑换码兑换指令''' 
        sendId=await event.get_sender_id()
        token=await self.get_kv_data(f"{sendId}Token","")
        userId=await self.get_kv_data(f"{sendId}Id","")
        url="https://ai.luogu.me/api/user/topup"

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
