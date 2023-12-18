import re


def count_words_in_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 移除YAML Front Matter
    content = re.sub(r"---.*?---", "", content, flags=re.DOTALL)

    # 移除代码块
    content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"```{.*?}.*?```", "", content, flags=re.DOTALL)

    # 移除HTML块
    content = re.sub(r"{=html}.*?{=html}", "", content, flags=re.DOTALL)

    # 移除Quarto特定语法
    content = re.sub(r":::.*?:::", "", content, flags=re.DOTALL)

    # 计算剩余文本的字数
    words = content.split()
    return len(words)


file_path = 'C:/Users/15827/git_demo/FSDS/Group_work_1.qmd'
word_count = count_words_in_markdown(file_path)
print(f"Word Count: {word_count}")


