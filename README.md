<<<<<<< HEAD
# LLM_Chat_Server
A lightweight Flask-based chat server integrating pre-trained LLMs for intelligent responses via RESTful API
=======
# LLM Chat Server Project

## 📖 项目简介

本项目旨在提供一个基于 Flask 的轻量级聊天服务器，利用预训练的大型语言模型（LLM）生成响应。通过简单的 RESTful API 接口，客户端可以发送消息并接收模型生成的回复。项目结构清晰，便于扩展和维护。

## 🛠 技术栈

- **后端框架**: Flask
- **模型加载**: Transformers
- **日志系统**: Python 标准库 logging

## 🏃‍♂️ 快速上手指南

### 环境准备

1. **安装 Python 3.8+**: 确保你的系统中安装了 Python 3.8 或更高版本。

2. **安装依赖**: 项目依赖通过 `requirements.txt` 管理。首先，克隆此仓库到本地，然后进入项目根目录。

```shell
git clone https://github.com/liu673/LLM_Chat_Server.git
cd LLM_Chat_Server
# 创建并激活虚拟环境，然后安装依赖 PS: 可根据需要安装适合你的torch版本
pip install -r requirements.txt
```

### 配置项目

#### （1）配置环境变量
复制 .env.example 文件为 .env，并根据实际情况填写必要的环境变量，例如模型路径、端口号、模型路由等。
```shell
cp .env.example .env
```

#### （2）下载模型
目前只是对LLM的chat版本进行了封装，所以需要下载chat版本的模型，使用以下命令下载模型：
```shell
python scripts/download_model.py
```

### 启动服务
使用以下命令启动 Flask 应用：
```shell
python scripts/run_project.py
```

### 客户端请求示例
python
```shell
python services/llm_server.py
```
curl
```shell
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"message": [{"role": "user", "content": "你是谁？"}], "history": ''}' \
     http://127.0.0.1:3001/generate
# 注意更换成你的路由
```

## 🚀 部署注意事项
- **网络配置**：配置合适的防火墙规则，限制不必要访问。
- **资源规划**：评估模型对硬件的需求，提前规划服务器资源。
- **安全信息**：在生产环境中，请确保使用更安全的方式管理环境变量和敏感信息。


## 📄 许可协议
该项目遵循 MIT 许可证。详细条款请见 LICENSE 文件。

## 💬 联系方式
对于任何疑问、建议或合作意向，欢迎通过 [GitHub Issues](https://github.com/liu673/LLM_Chat_Server/issues) 或电子邮件与我们取得联系。
>>>>>>> a77d89a (更新代码)
