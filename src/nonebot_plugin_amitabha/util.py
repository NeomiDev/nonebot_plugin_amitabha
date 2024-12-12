import asyncio
import httpx
from nonebot import logger

from .config import config
import nonebot_plugin_localstore as store


async def download_sutras() -> None:
    """从仓库下载佛经"""

    async def _download_file(download_url: str, file_name: str) -> None:
        async with httpx.AsyncClient() as client:
            download_url = download_url.replace(
                "https://raw.githubusercontent.com", config.reverse_proxy
            )
            response = await client.get(download_url)
            if response.status_code == 200:
                sutra = store.get_plugin_data_file(file_name)
                sutra.write_bytes(response.content)
                logger.success(f"佛经 {file_name} 下载成功")

    async with httpx.AsyncClient(follow_redirects=True) as client:
        tasks = []
        resp = await client.get(config.data_source)
        if resp.status_code == 200:
            file_list = resp.json()
            for sutra in file_list:
                file_name = sutra.get("name")
                download_url: str = sutra.get("download_url")
                logger.info(f"{file_name} 加入队列")
                tasks.append(_download_file(download_url, file_name))

        await asyncio.gather(*tasks)


async def check_sutras() -> None:
    """检查是否需要下载佛经"""
    sutra_list = [i for i in store.get_plugin_data_dir().iterdir()]
    if not sutra_list:
        logger.info("开始从仓库下载可用的佛经..")
        await download_sutras()
