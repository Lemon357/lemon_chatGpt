# openAI API密钥
import os
import sys
import gradio as gr

my_api_key = ""
# API URl
API_URL = "https://api.openai.com/v1/chat/completions"

if my_api_key == "":
    my_api_key = os.environ.get('my_api_key')
    print(my_api_key)

if my_api_key == "empty":
    print("Please give a api key!")
    sys.exit(1)

title = """<h1 align="center">笨笨</h1>"""
description = """<div align=center>
阿巴阿巴阿巴
</div>
"""
# gradio构建页面
with gr.Blocks() as demo:
    gr.HTML(title)
    # API输入框
    keyTxt = gr.Textbox(show_label=True, placeholder=f"在这里输入你的OpenAI API-key...",
                        value=my_api_key, label="API Key", type="password").style(container=True)
    # chat聊天框
    chatbot = gr.Chatbot()
    # 状态
    history = gr.State([])
    TRUE_CONSTANT = gr.State(True)
    FALSE_CONSTANT = gr.State(False)
    topic = gr.State("未命名对话历史记录")
    # 聊天输入框
    with gr.Row():
        with gr.Column(scale=12):
            gr.Textbox(show_label=False, placeholder="你想和它说~~~~~").style(
                container=False)
        with gr.Column(min_width=50, scale=1):
            gr.Button("😇", variant="primary")
    # 功能区
    with gr.Row():
        emptyBtn = gr.Button("🧹 新的对话")
        retryBtn = gr.Button("🔄 重新生成")
        delLastBtn = gr.Button("🗑️ 删除上条对话")
        reduceTokenBtn = gr.Button("♻️ 总结对话")

    systemPromptTxt = gr.Textbox(show_label=True, placeholder=f"在这里输入System Prompt...",
                                 label="System prompt", value=initial_prompt).style(container=True)

    demo.title = "笨笨啥都不会"
    demo.queue().launch(server_name="127.0.0.1", share=False)
