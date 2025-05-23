# ==============================================================================
# Copyright (C) 2025 Evil0ctal
#
# This file is part of the AndroidReverse101 project.
# Github: https://github.com/Evil0ctal/AndroidReverse101
#
# This project is licensed under the MIT license.
# ==============================================================================
#                                     ,
#              ,-.       _,---._ __  / \
#             /  )    .-'       `./ /   \
#            (  (   ,'            `/    /|
#             \  `-"             \'\   / |
#              `.              ,  \ \ /  |
#               /`.          ,'-`----Y   |
#              (            ;        |   '
#              |  ,-.    ,-'         |  /
#              |  | (   |  Evil0ctal | /
#              )  |  \  `.___________|/  Github - AndroidReverse101
#              `--'   `--'
# ==============================================================================

import os

# 定义根目录
BASE_DIR = "AndroidReverse101"

# 定义学习阶段及目录
stages = {
    "birinci_asama_bilgisayar_temelleri_tersine_muhendislige_giris": [
        (1, "什么是逆向工程"),
        (2, "Android 逆向的历史与发展"),
        (3, "什么是 CPU 指令集"),
        (4, "进制转换_为什么16进制很重要"),
        (5, "汇编语言基础"),
        (6, "x86 vs. ARM 汇编"),
        (7, "ARM 汇编指令解析"),
        (8, "函数调用与返回"),
        (9, "Android CPU 架构解析"),
        (10, "Dalvik vs. ART 运行时"),
        (11, "Android 进程管理"),
        (12, "Android 权限机制"),
        (13, "Android APP 目录结构"),
        (14, "APK 是如何加载的"),
        (15, "手写 ARM 汇编代码_实验"),
        (16, "反汇编工具介绍"),
        (17, "ELF 文件解析"),
        (18, "如何调试 Native 层"),
        (19, "Android APP 安全机制"),
        (20, "CTF 逆向挑战_初级"),
    ],
    "第二阶段_APK逆向基础": [
        (21, "APK 文件结构解析"),
        (22, "如何反编译 APK"),
        (23, "DEX 文件结构解析"),
        (24, "Smali 语言入门"),
        (25, "Smali 代码修改实验"),
        (26, "APK 重新打包_签名"),
        (27, "动态调试入门"),
        (28, "使用 Frida Hook Java 方法"),
        (29, "Frida Hook 实战"),
        (30, "逆向 JNI 和 Native 方法"),
        (31, "Xposed 入门"),
        (32, "破解 VIP 限制"),
        (33, "绕过 SSL Pinning"),
        (34, "Android 代码混淆与解混淆"),
        (35, "逆向加密算法_MD5_AES_RSA"),
        (36, "分析 WebSocket_API 请求"),
        (37, "破解应用限制_实战"),
        (38, "游戏破解基础"),
        (39, "反反调试"),
        (40, "Android 加固原理"),
        (41, "解密加固 APK_初级"),
    ],
    "第三阶段_高级逆向_CTF挑战": [
        (60, "深入分析 CTF 逆向挑战"),
        (70, "逆向挖掘 0Day 漏洞"),
        (100, "终极挑战_逆向一个完整 APP"),
    ]
}


def create_files():
    """ 创建目录和 Markdown 文件 """
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)

    for stage, topics in stages.items():
        stage_path = os.path.join(BASE_DIR, stage)
        os.makedirs(stage_path, exist_ok=True)  # 创建阶段目录

        for day, title in topics:
            filename = f"Day_{day}_{title.replace(' ', '_')}.md"
            file_path = os.path.join(stage_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# Day {day}: {title}\n\n")
                f.write("## 学习目标\n\n")
                f.write("## 知识点\n\n")
                f.write("## 实战任务\n\n")
                f.write("## 参考资料\n\n")

            print(f"✅ 创建: {file_path}")

    print("\n🎉 所有 Markdown 文件创建完成！")


if __name__ == "__main__":
    create_files()
