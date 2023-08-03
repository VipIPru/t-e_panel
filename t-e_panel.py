 # meta developer: @bruhHikkaModules 
 # created for @TriggerEarth 
 # Автор модуля не несёт ответственность за происходящее на хостинге 
 # ❌✅  
 import re 
 import telethon 
 import asyncio 
 from telethon import events,functions 
 from telethon.errors.rpcerrorlist import YouBlockedUserError 
 from telethon.tl.types import Message, ChatAdminRights 
 from .. import loader, utils 
 from ..inline.types import InlineCall 
  
 @loader.tds 
 class TriggerEarthPanel(loader.Module): 
         '''Модуль для управления вашими контейнерами в @Triggerhub_Bot и @triggerpanel_bot''' 
         strings = { 
             "name": "T-E Panel" 
         } 
         @loader.command() 
         async def tup(self, message): 
                 ''' - Включить контейнер ''' 
                 async with self.client.conversation("@triggerpanel_bot") as conv: 
                         try: 
                                 await conv.send_message("/up") 
                         except YouBlockedUserError: 
                                 await message.edit("❌ <b>Ошибка:</b>\n Вы заблокировали @triggerpanel_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 await conv.send_message("/panel") 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await utils.answer(message,"❌ <b>Ошибка</b>\n В ответ на ваш запрос (/up) бот, к сожаленнию ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError: 
                                 return 
                         links_regex = re.compile(r'.(https?://\S+).') 
                         response.text = links_regex.sub('Ссылка вырезана в целях безопасности.', response.text) 
                         if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text): 
                                 response.text = '\n'.join(response.text.split('\n')[:-2]) 
                         await utils.answer(message, response.text + "\n\nВаш запрос был /up\n<i> ℹ️ Если с вашим контейнером ничего не происходит, подождите</i>") 
              
         @loader.command() 
         async def tdown(self, message): 
                 ''' - Выключить контейнер''' 
                 async with self.client.conversation("@triggerpanel_bot") as conv: 
                         try: 
                                 await conv.send_message("/down") 
                         except YouBlockedUserError: 
                                 await message.edit("❌ <b>Ошибка:</b>\n Вы заблокировали @triggerpanel_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 await conv.send_message("/panel") 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await utils.answer(message,"❌ <b>Ошибка</b>\n В ответ на ваш запрос (/down) бот, к сожаленнию ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError: 
                                 return 
                         await utils.answer(message, response.text + "\n\nВаш запрос был /down\n<i> ℹ️ Если с вашим контейнером ничего не происходит, подождите</i>") 
         @loader.command() 
         async def tsubs(self, message): 
                 ''' - Информация о подписке''' 
                 async with self.client.conversation("@triggerhub_bot") as conv: 
                         try: 
                                 await conv.send_message("/subs") 
                         except YouBlockedUserError: 
                                 await message.edit("❌ <b>Ошибка</b>\n Вы заблокировали @triggerhub_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await utils.answer(message,"❌ <b>Ошибка</b>\n В ответ на ваш запрос (/subs) бот, к сожаленнию ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError: 
                                 return 
                         await utils.answer(message, f"ℹ️ <b>Информация о тарифе:</b>\n\n{response.text}") 
         @loader.command() 
         async def trestart(self, message): 
                 ''' - Перезагрузить контейнер''' 
                 async with self.client.conversation("@triggerpanel_bot") as conv: 
                         try: 
                                 await conv.send_message("/restart") 
                         except YouBlockedUserError: 
                                 await message.edit("❌ <b>Ошибка</b>\n Вы заблокировали @triggerpanel_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 await conv.send_message("/panel") 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await utils.answer(message,"❌ <b>Ошибка</b>\n В ответ на ваш запрос (/restart) бот, к сожаленнию ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError: 
                                 return 
                         await utils.answer(message, response.text + "\n\nВаш запрос был /restart\n<i>ℹ️ Если с вашим контейнером ничего не происходит, подождите</i>") 
         @loader.command() 
         async def tweburl(self,message): 
                 ''' - Ссылка для настройки вашего бота''' 
                 await self.inline.form( 
                 text="<b>Вы уверены что хотите посмотреть ссылку для настройки юзербота?</b>\n <b>Эту ссылку ни в коем случае нельзя распостранять,</b> поэтому эту команду лучше выполнять в Избранном", 
                 message=message, 
                 reply_markup=[ 
                     [ 
                         { 
                             "text": "✅ Подтверждаю", 
                             "callback": self.answy, 
                         }, 
                         { 
                             "text": "❌ Отмена", 
                             "action": "close", 
                         }, 
                     ] 
                 ] 
                 ) 
          
         async def answy(self, call: InlineCall): 
                 async with self.client.conversation("@triggerpanel_bot") as conv: 
                         try: 
                                 await conv.send_message("/weburl") 
                         except YouBlockedUserError: 
                                 await call.edit("❌ <b>Ошибка</b>\n Вы заблокировали @triggerpanel_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await call.edit(message,"❌ <b>Ошибка</b>\n В ответ на ваш запрос (/weburl) бот, к сожаленнию ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError: 
                                 return 
                         if response.text == "Ссылка для настройки -": 
                                 await call.edit("ℹ️ <b>Информация</b>\nУ вас скорее всего нет подписки или не выбран юзербот") 
                         else: 
                                 await call.edit(response.text) 
  
         @loader.command(alias = '') 
         async def tstatus(self,message): 
                 ''' - Состояние вашего контейнера''' 
                 async with self.client.conversation("@triggerpanel_bot") as conv: 
                         try: 
                                 await conv.send_message("/status") 
                         except YouBlockedUserError: 
                                 await message.edit("❌ <b>Ошибка</b>\n Вы заблокировали @triggerpanel_bot\nРазблокируйте, иначе модуль работать не будет") 
                         try: 
                                 response = await asyncio.wait_for(conv.get_response(), timeout=5) 
                         except asyncio.TimeoutError: 
                                 await utils.answer(message,"❌ <b>Ошибка</b>\n К сожалению бот ничего не ответил в течении 5 секунд") 
                                 return 
                         except ValueError as e: 
                                 return 
                         await utils.answer(message, await self.inline.form( 
                             message=message, 
                             text=response.text, 
                             reply_markup=[[{"text":"Наш канал 👻","url":"https://t.me/triggerearth"}]], 
                             ), 
                         )
