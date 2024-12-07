
<div align="center">

<p align="center">
  <a href=""><img src="" width="200" height="200" alt="阿弥陀佛"></a>
</p>

## nonebot_plugin_amitabha

基于nonebot2的群聊自动念佛插件

</div>

</details>

## 📖 介绍

### 南无阿弥陀佛！

众所周知，以任何形式如诵读、传播、印刷佛经者都将累积对应功德。现今科学技术越发先进，自然不必拘泥于念佛的形式如何。为了打造高效、便捷、一体化的“云念佛”体系，我写了这个插件。

欢迎广大开发者和感兴趣的朋友pr、使用。愿佛祖保佑你们，功德无量，阿弥陀佛！

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
| send_interval | 是 | 无 | 念经发送信息的间隔 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 开启念佛模式 | 群员 | 否 | 群聊 | 进入念佛虚拟环境 |
| 关闭念佛模式 | 群员 | 否 | 群聊 | 退出念佛虚拟环境 |
| 念经 | 群员 | 否 | 群聊 | 开始一个念经任务 |
| 停止念经 | 群员 | 否 | 群聊 | 停止当前念经任务 |

## 👣 更新日志：

---

2024 12.7 v0.1.0

添加基础功能，发布初版代码（pypi未发布）

---

### 预计会添加的功能：

* [X]  开始念佛/诵经 [佛经名]
* [X]  停止念佛/诵经
* [ ]  每日禅修
* [ ]  语音诵经 [佛经音频名]
* （待追加...）
