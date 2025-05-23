# **📜 Day 5: 汇编语言基础**

## **📌 学习目标**
✅ 了解 **汇编语言** 的基本概念及其在计算机体系结构中的作用。  
✅ 学习 **x86 汇编、ARM 汇编、Smali（DEX 字节码）** 三种汇编语言的基础。  
✅ 掌握 **寄存器、指令格式、数据传输、算术运算、控制流** 等汇编语言核心概念。  
✅ 通过 **实际示例** 学习汇编如何与 C 语言进行交互，并实现简单的汇编程序。  
✅ 学习 **汇编在逆向工程和漏洞利用中的作用**，并进行简单的调试和分析。

---

# **1️⃣ 什么是汇编语言？**
**汇编语言（Assembly Language）** 是 **低级编程语言**，它使用 **助记符（Mnemonic）** 代替二进制指令，使得程序员可以更方便地控制计算机硬件。  

| **语言层级** | **示例** |
|---------|----------------------|
| **高级语言（C、Python）** | `int a = 5;` |
| **汇编语言（x86、ARM）** | `MOV R0, #5` |
| **机器码（16 进制指令）** | `B8 05 00 00 00` |

汇编语言与特定 CPU 指令集紧密相关，如：
- **x86 汇编**（Intel、AMD 处理器）
- **ARM 汇编**（移动设备、嵌入式设备）
- **Smali 汇编**（Android DEX 字节码）

---

# **2️⃣ x86 汇编基础**
### **🔹 x86 处理器架构**
x86 采用 **CISC（复杂指令集计算机）**，支持 **可变长指令** 和 **丰富的寻址模式**。

**x86 32 位（IA-32）寄存器**
| **寄存器** | **用途** |
|---------|------------|
| EAX | 累加器（运算/返回值） |
| EBX | 基址寄存器 |
| ECX | 计数寄存器（循环） |
| EDX | 数据寄存器 |
| ESI | 源索引寄存器 |
| EDI | 目标索引寄存器 |
| EBP | 栈基址指针 |
| ESP | 栈指针 |

### **🔹 x86 指令示例**
```assembly
section .text
global _start

_start:
    mov eax, 5      ; EAX = 5
    add eax, 10     ; EAX = EAX + 10
    sub eax, 2      ; EAX = EAX - 2
    int 0x80        ; 系统调用
```
📌 **特点**：
- `mov eax, 5`：将 5 赋值给 `eax`。  
- `add eax, 10`：对 `eax` 进行加法运算。  
- `int 0x80`：调用 Linux 系统 API。

---

# **3️⃣ ARM 汇编基础**
### **🔹 ARM 处理器架构**
ARM 采用 **RISC（精简指令集计算机）**，指令长度固定，执行效率更高，广泛用于 **移动设备和嵌入式系统**。

**ARMv7（ARM32）寄存器**
| **寄存器** | **用途** |
|---------|--------|
| R0-R3 | 传递函数参数 |
| R4-R11 | 通用寄存器 |
| R12 | 过程调用寄存器 |
| R13 | 栈指针（SP） |
| R14 | 链接寄存器（LR） |
| R15 | 程序计数器（PC） |

**ARMv8（ARM64）寄存器**
| **寄存器** | **用途** |
|---------|--------|
| X0-X7 | 传递参数和返回值 |
| X8 | 系统调用 |
| X9-X15 | 临时变量 |
| X19-X30 | 通用寄存器 |
| X30 (LR) | 链接寄存器 |

### **🔹 ARM 指令示例**
```assembly
.global _start
_start:
    MOV R0, #5      ; 赋值 5 给 R0
    ADD R0, R0, #3  ; R0 = R0 + 3
    LDR R1, [R2]    ; 读取 R2 指向的内存到 R1
    STR R1, [R3]    ; 存储 R1 到 R3 指向的内存
    B _start        ; 无限循环
```

---

# **4️⃣ Smali（Android DEX 汇编）**
**Smali 是 Android DEX（Dalvik Executable）文件的汇编语言**，相当于 Java 字节码的汇编版本。

### **🔹 Smali 代码示例**
```smali
.method public static sum(II)I
    .registers 3
    add-int v0, p0, p1
    return v0
.end method
```

### **🔹 Smali 破解示例**
```smali
.method public isVip()Z
    .registers 2
    const/4 v0, 0x1  # 让所有用户变成 VIP
    return v0
.end method
```
📌 **修改 Smali 代码可用于绕过 Android 应用的 VIP 限制**。

---

# **5️⃣ 汇编与 C 语言的交互**
### **🔹 C 语言调用 x86 汇编**
```c
#include <stdio.h>

int add(int a, int b) {
    int result;
    __asm__ (
        "addl %%ebx, %%eax;"
        : "=a" (result)
        : "a" (a), "b" (b)
    );
    return result;
}

int main() {
    printf("Result: %d\n", add(5, 10));
    return 0;
}
```

### **🔹 C 语言调用 ARM 汇编**
```c
int add(int a, int b) {
    int result;
    __asm__ (
        "ADD %0, %1, %2"
        : "=r" (result)
        : "r" (a), "r" (b)
    );
    return result;
}
```

---

# **🛠 实战任务**
### **✅ 1. 编写并运行 x86 汇编**
```bash
nasm -f elf64 test.asm
ld -o test test.o
./test
```

### **✅ 2. 运行 ARM 汇编**
```assembly
.global _start
_start:
    MOV R0, #1
    LDR R1, =message
    MOV R2, #13
    MOV R7, #4
    SWI 0
    MOV R7, #1
    SWI 0

.section .data
message: .ascii "Hello, ARM!\n"
```

### **✅ 3. 反编译 APK 并修改 Smali**
```bash
apktool d app.apk -o output
vim output/smali/com/example/Main.smali
```

---

# **📚 参考资料**
📌 **x86 汇编**
- `x86 指令手册`：[https://www.felixcloutier.com/x86/](https://www.felixcloutier.com/x86/)  
- `NASM 手册`：[https://nasm.us](https://nasm.us)  

📌 **ARM 汇编**
- `ARM 指令手册`：[https://developer.arm.com/documentation](https://developer.arm.com/documentation)  
- `AArch64 汇编指南`：[https://azeria-labs.com/](https://azeria-labs.com/)  

📌 **Smali**
- `Smali 教程`：[https://github.com/JesusFreke/smali](https://github.com/JesusFreke/smali)  

---

🔥 **任务完成后，你将掌握：**  
✅ **x86、ARM、Smali 汇编语言的基础知识。**  
✅ **汇编如何与 C 语言交互。**  
✅ **运行、修改和调试汇编代码。**  

🚀 **下一步（Day 6）**：**x86 vs. ARM 汇编对比！** 🎯  