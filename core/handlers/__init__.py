from .text_handlers import router as text_routers
from .callbackquery_handlers import router as callback_routers

routers = [text_routers,callback_routers]