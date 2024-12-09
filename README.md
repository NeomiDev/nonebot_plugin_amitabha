
<div align="center">

<p align="center">
  <a href=""><img src="https://proxy.39miku.fun/Kaguya233qwq/nonebot-plugin-amitabha/refs/heads/main/images/amitabha.jpg" width="200" height="200" alt="阿弥陀佛"></a>
</p>

## nonebot_plugin_amitabha


<span style="color: yellow; font-size: 15px;">✨ _基于nonebot2的群聊赛博念佛插件_ ✨</span>

</div>

</details>

## 📖 介绍

### 🪷南无阿弥陀佛🪷

众所周知，以任何形式如诵读、传播、印刷佛经者都将累积对应功德。现今科学技术越发先进，自然不必拘泥于念佛的形式如何。为了打造高效、便捷、一体化的“赛博念佛”生态，本人编写了此插件。

**💡佛经数据源：docs/**
- 如果你有不错的佛经或佛咒，欢迎提交相关的pull request
- 佛经佛咒是txt文本文档格式，经文一行一句
- 推荐以经文名作为文件名保存，它将作为念经指令的经文名参数

**💡本地佛经目录：Amitabha/data/**
- 加载插件时将会从仓库中的docs文件夹下载所有经文
- 如果你想和最新的经文保持同步，请备份自己本地的经文，并删除data目录，重启nonebot即可


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot_plugin_amitabha

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot_plugin_amitabha
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot_plugin_amitabha
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot_plugin_amitabha
</details>
<details>
<summary>conda</summary>

    conda install nonebot_plugin_amitabha
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_amitabha"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| send_interval | 是 | 无 | 念经时发送信息的间隔 |

## 🎉 使用
### 🤖 指令表
**以下指令均需要命令前缀**
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 念佛模式 | 群员 | 否 | 群聊 | 进入念佛虚拟环境 |
| 关闭念佛模式 | 群员 | 否 | 群聊 | 退出念佛虚拟环境 |
| 念佛 [经文名] | 群员 | 否 | 群聊 | 开始一个念经任务 |
| 停止念佛 | 群员 | 否 | 群聊 | 停止当前念经任务 |

## ⚠️ 注意

开启念佛模式会有以下行为：

- 备份群头像与机器人群名片
- 修改群头像为佛陀头像，修改群名称
- 开启全员禁言

大群推荐在群聊宵禁时使用，日常使用可能会导致群员流失
关闭念佛模式会恢复以上被修改的内容并解除全员禁言

## 👣 更新日志：

---

2024 12.7 v0.1.0

添加基础功能，发布初版代码

---

### ✅ TODO：

* [X]  进入和退出念佛的虚拟环境
* [X]  开始和停止念佛的基本功能
* [ ]  每日禅修
* [ ]  语音诵经
* （待追加...）

### ❤️鸣谢

[[Nonebot](https://github.com/nonebot/nonebot2)] 超好用的跨平台bot开发框架

### 如果你喜欢此插件请不要忘记点个⭐~