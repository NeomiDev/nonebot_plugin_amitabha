import asyncio
import re
from pathlib import Path
from typing import Tuple

import httpx
from nonebot import on_command, logger
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
from nonebot.internal.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message

from nonebot import get_driver
from .exception import GroupCacheNotFoundError
from .config import Config, config
from .util import check_sutras

# nonebot的插件元数据标准
__plugin_meta__ = PluginMetadata(
    name="南无阿弥陀佛",
    description="基于nonebot2的群聊自动念佛插件",
    usage="""
- 念佛 [佛经名]
- 停止念佛
- 念佛模式
- 关闭念佛模式
- 佛经列表
    """,
    config=Config,
    type="application",
    extra={"author": "Kaguya姬辉夜", "qq": "1435608435", "version": "0.1.0"},
    homepage="https://github.com/Kaguya233qwq/nonebot_plugin_amitabha",
    supported_adapters={"~onebot.v11"},
)

FOn = on_command("fon", aliases={"念佛模式", "阿弥陀佛"})
FOff = on_command("foff", aliases={"关闭念佛模式", "退出念佛模式"})
StartChant = on_command("chantstart", aliases={"念佛", "念诵"})
StopChant = on_command("chantstop", aliases={"停止念佛", "停止念诵"})
Sutras = on_command("sutras", aliases={"佛经列表"})


async def create_cache(group_id, group_name, bot_card) -> None:
    """创建群信息缓存"""
    # 若不存在文件夹则进行创建
    cache_path: Path = Path(config.data_path) / "cache"
    if not cache_path.exists():
        cache_path.mkdir()
    #  腾讯qq群头像原生接口
    group_profile = f"http://p.qlogo.cn/gh/{group_id}/{group_id}/640/"
    async with httpx.AsyncClient() as client:
        img = await client.get(group_profile)
        save_path = cache_path / f"{group_id}_{group_name}_{bot_card}.jpg"
        with open(save_path, "wb") as f:
            f.write(img.content)


async def load_cache(group_id: int) -> Tuple[str]:
    """按群组id读取群信息缓存"""
    cache_path: Path = Path(config.data_path) / "cache"
    for file_path in cache_path.iterdir():
        if str(group_id) in file_path.name:  # 比较文件名
            matcher = re.findall(r"(\d*)_(.*)_(.*)\.jpg", file_path.name)
            if matcher:
                logger.success("读取群信息缓存成功")
                return matcher[0][0], matcher[0][1], matcher[0][2], file_path.name
    # 如果未找到匹配的文件抛出异常
    raise GroupCacheNotFoundError("群缓存信息未找到")


@FOn.handle()
async def fo_on(bot: Bot, event: GroupMessageEvent, matcher: Matcher):
    #  念佛初始化：缓存原始信息，修改群名称、群头像群名片
    group_id = event.group_id
    user_id = bot.self_id
    group_info = await bot.get_group_info(group_id=group_id)
    member_info = await bot.get_group_member_info(
        group_id=group_id, user_id=int(user_id)
    )
    await create_cache(
        group_id, group_info["group_name"], member_info["card"]
    )  # 缓存原始信息

    await bot.set_group_name(group_id=group_id, group_name="净")
    await bot.set_group_card(group_id=group_id, user_id=int(user_id), card="功德无量")
    profile = "https://proxy.39miku.fun/Kaguya233qwq/nonebot-plugin-amitabha/refs/heads/main/images/amitabha.jpg"
    await bot.call_api("set_group_portrait", group_id=group_id, file=profile)
    await bot.set_group_whole_ban(group_id=group_id)  # 启动清净模式
    logger.success("念佛环境准备完成")
    await matcher.finish("阿弥陀佛！念佛绝佳环境已准备完毕")


@FOff.handle()
async def fo_off(bot: Bot, event: GroupMessageEvent, matcher: Matcher):
    group_id, group_name, bot_card, filename = await load_cache(event.group_id)
    user_id = bot.self_id
    await bot.set_group_name(group_id=group_id, group_name=group_name)
    await bot.set_group_card(group_id=group_id, user_id=int(user_id), card=bot_card)
    cache_path: Path = Path(config.data_path) / "cache"
    file_path: Path = cache_path / filename

    await bot.call_api(
        "set_group_portrait", group_id=event.group_id, file=file_path.resolve().as_uri()
    )
    await bot.set_group_whole_ban(group_id=event.group_id, enable=False)  # 关闭清净模式
    logger.success("念佛模式已关闭")
    await matcher.finish("阿弥陀佛！您已关闭念佛模式")


@StartChant.handle()
async def start_chant(args: Message = CommandArg()):
    """开始念经的handler"""
    param_list = args.extract_plain_text().split()
    if len(param_list) < 1:
        await StartChant.finish("参数数量不正确，用法：chantstart [佛经名] [循环次数]")
    elif len(param_list) < 2:
        # 将此参数作为佛经名进行念诵，并默认只念诵一遍
        file_path: Path = Path(config.data_path) / "data" / f"{param_list[0]}.txt"
        if not file_path.exists():
            await StartChant.finish("佛经不存在，请重新输入")
        with open(file_path, "r", encoding="utf-8") as f:
            # 将经文加载至配置
            config.sutra = f.readlines()
            for words in config.sutra:
                if config.sutra:
                    await StartChant.send(words.strip())
                    await asyncio.sleep(config.send_interval)
                else:
                    break
    elif len(param_list) == 2:
        for _ in range(param_list[1]):
            # 将此参数作为佛经名进行念诵，并念诵第二个参数值的次数
            file_path: Path = Path(config.data_path) / "data" / f"{param_list[0]}.txt"
            if not file_path.exists():
                await StartChant.finish("佛经不存在，请重新输入")
            with open(file_path, "r", encoding="utf-8") as f:
                # 将经文加载至配置
                config.sutra = f.readlines()
                for words in config.sutra:
                    if config.sutra:
                        await StartChant.send(words.strip())
                        await asyncio.sleep(config.send_interval)
                    else:
                        return


@StopChant.handle()
async def stop_chant():
    """停止当前的念佛任务"""
    # 清空加载的经文
    config.sutra = []
    await StartChant.finish("用户终止念佛")


@Sutras.handle()
async def sutras_list():
    """查看佛经列表"""
    sutra_path: Path = Path(config.data_path) / "data"
    files = [
        file.name.replace(".txt", "")
        for file in sutra_path.rglob("*.txt")
        if file.is_file()
    ]
    msg = "佛经数据目录为空！"
    if files:
        msg = "\n".join(files)
    await Sutras.finish(msg)


driver = get_driver()


@driver.on_startup
async def startup_checking():
    await check_sutras()
