import json
import gradio as gr
# import openai
import os
import sys
import traceback
import requests

# import markdown

my_api_key = ""  # 在这里输入你的 API 密钥
initial_prompt = "You are a helpful assistant."

API_URL = "https://api.openai.com/v1/chat/completions"

if my_api_key == "":
    my_api_key = os.environ.get('my_api_key')

if my_api_key == "empty":
    print("Please give a api key!")
    sys.exit(1)



title = """<h1 align="center">笨笨</h1>"""
description = """<div align=center>

阿巴阿巴阿巴
</div>
"""
with gr.Blocks() as demo:
    gr.HTML(title)
    keyTxt = gr.Textbox(show_label=True, placeholder=f"在这里输入你的OpenAI API-key...",
                        value=my_api_key, label="API Key", type="password").style(container=True)
    chatbot = gr.Chatbot()  # .style(color_map=("#1D51EE", "#585A5B"))
    history = gr.State([])
    TRUE_CONSTANT = gr.State(True)
    FALSE_CONSTANT = gr.State(False)
    topic = gr.State("未命名对话历史记录")

print("访问 http://localhost:7860 查看界面")
# 默认开启本地服务器，默认可以直接从IP访问，默认不创建公开分享链接
demo.title = "笨笨啥都不会"
demo.queue().launch(server_name="0.0.0.0", share=False)  # 改为 share=True 可以创建公开分享链接