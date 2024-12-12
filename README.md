
<div align="center">

<p align="center">
  <a href=""><img src="https://proxy.39miku.fun/Kaguya233qwq/nonebot-plugin-amitabha/refs/heads/main/images/amitabha.jpg" width="200" height="200" alt="阿弥陀佛"></a>
</p>

## nonebot_plugin_amitabha


<span style="color: yellow; font-size: 15px;">✨ _🙏基于nonebot2的群聊赛博念佛插件🙏_ ✨</span>

</div>

</details>

## 📖 介绍

### 🪷南无阿弥陀佛🪷

众所周知，以任何形式如诵读、传播、印刷佛经者都将累积对应功德。现今科学技术越发先进，自然不必拘泥于念佛的形式如何。为了打造高效、便捷、一体化的“赛博念佛”生态，并通过网络更好地广泛传播佛法，本人编写了此插件🙏。

**💡佛经数据源：docs/**
- 如果你有不错的佛经或佛咒，欢迎提交相关的pull request
- 佛经佛咒是txt文本文档格式，经文一行一句
- 推荐以经文名作为文件名保存，它将作为念经指令的经文名参数

**💡本地佛经目录：参考localstore的默认存储目录**
- 加载插件时将会从仓库中的docs文件夹下载所有经文
- 如果你想和最新的经文保持同步，请备份自己本地的经文，并删除[data_dir]下的所有文件，重启nonebot即可


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

## ⚙️ 配置 (必要)

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| send_interval | 是 | 无 | 念经时发送信息的间隔 |

## 🎉 简单使用

- 首先，你应该在群内发送"经文列表"以确认下载到本地的经文名称列表。

- 发送“念佛+[经文名]+[念诵次数]”来开始一个念佛任务。

- 你可以在念佛过程中发送“停止念佛”来终止当前的念佛任务。

- 发送“念佛模式”获得沉浸式的念佛体验，可发送“关闭念佛模式”来退出。

### 🤖 指令表
**以下指令均需要命令前缀**
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 念佛模式 | 群员 | 否 | 群聊 | 进入念佛虚拟环境 |
| 关闭念佛模式 | 群员 | 否 | 群聊 | 退出念佛虚拟环境 |
| 念佛 [经文名] [念诵次数]| 群员 | 否 | 群聊 | 开始一个念佛任务 |
| 停止念佛 | 群员 | 否 | 群聊 | 停止当前念佛任务 |
| 佛经列表 | 群员 | 否 | 群聊 | 查看下载的佛经名称列表 |

## ⚠️ 注意

开启**念佛模式**会有以下行为：

- 备份群头像与机器人群名片
- 修改群头像为佛陀头像，修改群名称
- 开启全员禁言

大群推荐在群聊**宵禁**时使用，日常使用可能会导致**群员流失**

关闭念佛模式会**恢复**以上被修改的内容并解除全员禁言

## 👣 更新日志：

---

2024 12.12 v0.1.3

使用localstore数据存储标准

2024 12.9 v0.1.2

修复已知问题，构建项目发布至pypi

2024 12.7 v0.1.0

添加基础功能，发布初版代码

---

## ✅ TODO：

* [X]  进入和退出念佛的虚拟环境
* [X]  开始和停止念佛的基本功能
* [ ]  每日禅修
* [ ]  敲木鱼功能
* [ ]  语音诵经
* （待追加...）

## ❤️鸣谢

[[Nonebot](https://github.com/nonebot/nonebot2)] 超好用的跨平台bot开发框架

### 如果你喜欢此插件请不要忘记点个⭐~