import asyncio
from pathlib import Path
import httpx
from nonebot import logger

from .config import config

async def download_sutras() -> None:
    """从仓库下载佛经
    """
    async def _download_file(download_url: str, file_name: str) -> None:
        sutras_path: Path = Path(config.data_path) / "data"
        if not sutras_path.exists():
            sutras_path.mkdir()
        
        async with httpx.AsyncClient() as client:
            download_url = download_url.replace(
                "https://raw.githubusercontent.com",
                config.reverse_proxy
                )
            response = await client.get(download_url)
            if response.status_code == 200:
                save_path = sutras_path / file_name
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                    logger.success(f"佛经 {file_name} 下载成功")
    
    async with httpx.AsyncClient(timeout=5) as client:
        tasks = []
        resp = await client.get(config.data_source)
        if resp.status_code == 200:
            file_list = resp.json()

            for sutra in file_list:
                file_name = sutra.get("name")
                download_url: str = sutra.get("download_url")
                logger.info(f"{file_name} 加入队列")
                tasks.append(_download_file(download_url,file_name))
        
        await asyncio.gather(*tasks)
        
async def check_sutras() -> None:
    """检查是否需要下载佛经
    """
    root = Path(config.data_path)
    if not root.exists():
        root.mkdir()
    
    sutras_path: Path = root / "data"
    if not sutras_path.exists():
        logger.info("开始从仓库下载可用的佛经..")
        await download_sutras()
            