# Luogu-Bot

## 基于[CodingOIer](https://github.com/CodingOIer/Luogu-Bot)的洛谷的机器人。

<br />

<p align="center">
  <a href="https://www.luogu.com.cn/chat?uid=754324">
    <img src="https://fecdn.luogu.com.cn/luogu/logo.png" alt="Logo" height="80">
  </a>
  <h3 align="center">洛谷机器人</h3>
  <p align="center">
    为你的在洛谷的 OI 生活增加一份乐趣
    <br />
    <a href="https://github.com/CodingOIer/Luogu-Bot"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://www.luogu.com.cn/chat?uid=661094">查看 Demo</a>
    ·
    <a href="https://github.com/Github-liyifan202201/Luogu-Bot-GPT/issues">报告 Bug</a>
    ·
    <a href="https://github.com/Github-liyifan202201/Luogu-Bot-GPT/issues">提出新特性</a>
  </p>

</p>


 本篇 README.md 面向开发者

### 上手指南

你也可以看看发行版本的自动安装脚本

###### 开发前的配置要求

1. 在本地运行洛谷本地代理，仓库链接：[CodingOIer/Luogu-Proxy (github.com)](https://github.com/CodingOIer/Luogu-Proxy)
2. 安装依赖 `pip install requests, openai, loguru`。

###### **安装步骤**

1. 准备一台云服务器。

3. 克隆本仓库。


4. 编写 `settings.json` 形如：

   ```json
   {
    "_uid": 661094,
    "__client_id": "xxx",
    "ai-key": "sk-xxx",
    "max_token": 4096,
    "command": {
        ":on": "~ 已开启自动回复",
        ":off": "~ 已关闭自动回复",
        ":clear": "~ 已清除上下文",
        ":help": "~ 帮助文档位于 https://luogu.codingoier.work/bot/help.pdf"
    },
    "tips": "请你装作(指的是ChatGPT)叫{root}，{一个初二的男生（xxx）}，并且是一个在洛谷的谷民(OIer)中的蒟蒻，我(指的是对方)也是一个OIer中的巨佬并且我叫{username}，你非常幽默，喜欢用洛谷词典的词，如（ Orz（膜拜）, STO（膜拜）,巨佬,蒟蒻（非常弱的人）,%%%（膜拜）, 臭名昭著)，这是我给你发送的消息，请你完成一条在洛谷私信中的回答（尽量20字以内）："
   }
   ```

   > [!TIP]
   >
   > `tips` 中的 `{username}` 会被替换为正在对话的用户，`{root}` 会被替换为当前的机器人用户名。

5. 运行。

   ```shell
   python server.py
   ```

   

#### 如何参与开源项目

~~目前本项目仍处于开发初期，所以暂时不接受 PR，但是你可以提出 issue。~~



### 作者

原作者：CodingOIer 

改本作者：liyifan202201

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了 GNU GPLv3 授权许可，详情请参阅 [LICENSE.txt](https://github.com/CodingOIer/Luogu-Bot/blob/main/LICENSE.txt)

### 鸣谢


- [Luogu](https://www.luogu.com.cn)
