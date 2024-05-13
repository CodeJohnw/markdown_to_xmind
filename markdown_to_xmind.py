import os
import subprocess

def create_and_edit_txt():
    # 获取当前用户的桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    txt_file_path = os.path.join(desktop_path, 'markdown_text.txt')
    
    # 在桌面创建文本文件
    os.system(f'touch "{txt_file_path}"')
    # 使用TextEdit打开文本文件供编辑
    subprocess.run(['open', '-a', 'TextEdit', txt_file_path])

    input("请在打开的文本文件中粘贴 Markdown 内容，完成后保存并关闭文本编辑器，然后回到这里按 Enter 继续...")

def txt_to_md():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    txt_file_path = os.path.join(desktop_path, 'markdown_text.txt')
    md_file_path = os.path.join(desktop_path, 'markdown_text.md')
    
    # 将文本文件重命名为Markdown文件
    os.rename(txt_file_path, md_file_path)

def open_xmind():
    # 打开XMind应用，这里假设XMind已经安装在Applications文件夹中
    os.system('open -a /Applications/XMind.app')
    
    input("请手动在 XMind 中导入位于桌面的 'markdown_text.md' 文件，完成后按 Enter 结束脚本运行。")

def main():
    create_and_edit_txt()
    txt_to_md()
    open_xmind()

if __name__ == "__main__":
    main()
