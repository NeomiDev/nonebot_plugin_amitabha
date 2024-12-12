from pathlib import Path
from pydantic import BaseModel
from nonebot import get_plugin_config, require

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store


class Config(BaseModel):
    """插件配置项"""

    data_dir: Path = store.get_plugin_data_dir()
    """插件数据目录"""

    cache_dir: Path = store.get_plugin_cache_dir()
    """插件缓存目录"""

    reverse_proxy: str = "https://proxy.39miku.fun"
    """反向代理地址
    """
    data_source: str = (
        "https://api.github.com/repos/kaguya233qwq/nonebot-plugin-amitabha/contents/docs"
    )
    """经文下载的数据源
    """
    send_interval: int
    """每句经文发送的间隔时间
    """
    sutra: list = []


config = get_plugin_config(Config)
