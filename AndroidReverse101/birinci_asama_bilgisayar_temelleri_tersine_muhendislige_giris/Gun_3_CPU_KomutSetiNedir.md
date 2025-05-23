# **📜 Gün 3: CPU Komut Seti Nedir?**

## **📌 Öğrenme Hedefleri**  
✅ **CPU komut seti** kavramını ve farklı mimarilerde (x86, ARM, Smali) nasıl uygulandığını öğrenmek.  
✅ **x86 (CISC) vs. ARM (RISC) vs. Smali (Android DEX komutları)** arasındaki farklılıkları anlamak.  
✅ **ARMv7 (ARM32) ve ARMv8 (ARM64)** komutları arasındaki farkları kavramak.  
✅ **C dili ile assembly dilleri (x86, ARM, Smali) arasındaki dönüşümleri** anlamak.  
✅ Gerçek kod örnekleri ile farklı CPU komut setlerinin temel kullanımlarına alışmak.

---

# **1️⃣ CPU Komut Seti Nedir?**  
**CPU komut seti mimarisi (Instruction Set Architecture, ISA)**, CPU’nun çalıştırdığı yazılım komutlarının kümesidir ve CPU’nun ikili kodları nasıl çözüp işleyeceğini belirler.

🔹 Temel görevler:  
- Veri erişimi, aritmetik ve mantıksal işlemleri kontrol eder.  
- CPU performansı, güç tüketimi ve uyumluluğunu etkiler.  
- Farklı CPU üreticileri farklı komut seti mimarileri kullanır.

🔹 **Üç temel CPU komut seti**  
| **Mimari**     | **Özellikleri**                      | **Kullanım Alanları**                    |
|---------------|-----------------------------------|----------------------------------------|
| **x86 (CISC)**| Karmaşık komut seti, değişken uzunluklu komutlar, gelişmiş adresleme | PC, sunucular (Intel, AMD)              |
| **ARM (RISC)**| Basitleştirilmiş komut seti, sabit uzunluklu komutlar, düşük güç tüketimi ve yüksek performans | Mobil cihazlar, gömülü sistemler (Qualcomm, Apple, Huawei) |
| **Smali (DEX bytecode)** | Android DEX sanal makine komutları, Java/ART için | Android tersine mühendisliği             |

---

# **2️⃣ x86 Komut Seti**  
**x86 (CISC)**, **Intel ve AMD** tarafından geliştirilen mimari olup, başlıca PC ve sunucularda kullanılır.

🔹 **Özellikleri:**  
- Komut uzunluğu sabit değildir (1-15 byte arası), ARM’a göre daha karmaşıktır.  
- Çoklu adresleme modları ile daha karmaşık işlemler desteklenir.

### **🔹 x86 Assembly Örneği**  
```assembly
section .text
global _start

_start:
    mov eax, 5      ; eax registerına 5 ata
    add eax, 10     ; eax = eax + 10
    sub eax, 2      ; eax = eax - 2
    mov ebx, eax    ; eax’i ebx registerına kopyala
    int 0x80        ; sistem çağrısını tetikle
```

🔹 **Özellikler:**  
- `mov eax, 5`: Veri taşıma komutu.  
- `add eax, 10`: Toplama işlemi.  
- `int 0x80`: Linux altında sistem çağrısı.  

---

# **3️⃣ ARM Komut Seti**  
**ARM (RISC)**, mobil cihazlar için uygun olan **Basitleştirilmiş Komut Seti (RISC)** mimarisidir.  

🔹 **ARM Özellikleri**  
- **Komut uzunluğu sabittir** (4 byte).  
- **Register sayısı fazladır** (bellek erişimini azaltır, performansı artırır).  
- **Düşük güç tüketimi ve yüksek performans**, mobil cihazlar için uygundur.  

### **🔹 ARM Komutları vs. x86 Komutları**  
| **İşlem**       | **x86 Komutu (CISC)** | **ARM Komutu (RISC)**   |
|-----------------|-----------------------|------------------------|
| Atama           | `mov eax, 5`          | `MOV R0, #5`           |
| Toplama         | `add eax, 10`         | `ADD R0, R0, #10`      |
| Bellekten Okuma | `mov eax, [ebx]`      | `LDR R0, [R1]`         |
| Belleğe Yazma   | `mov [ebx], eax`      | `STR R0, [R1]`         |

---


# **4️⃣ ARMv7 (32-bit) vs. ARMv8 (64-bit)**
🔹 **ARMv7 (ARM32)**  
```assembly
.global _start
_start:
    MOV R0, #5      ; R0’a 5 ata
    ADD R0, R0, #3  ; R0 = R0 + 3
    LDR R1, [R2]    ; R2’nin gösterdiği bellekten R1’e oku
    STR R1, [R3]    ; R1’i R3’ün gösterdiği belleğe yaz
    B _start        ; sonsuz döngü
```

🔹 **ARMv8 (ARM64)**  
```assembly
.global _start
_start:
    MOV X0, #5      ; X0’a 5 ata
    ADD X0, X0, #3  ; X0 = X0 + 3
    LDR X1, [X2]    ; X2’nin gösterdiği bellekten X1’e oku
    STR X1, [X3]    ; X1’i X3’ün gösterdiği belleğe yaz
    B _start        ; sonsuz döngü
```

📌 **Farklar:**  
- ARMv7 `R0-R15` registerlarını kullanır, ARMv8 `X0-X30` registerlarını kullanır.  
- ARMv8 komutları 64-bit veri işlemesini destekler, işlem gücünü artırır.

---

# **5️⃣ Smali Assembly Dili (Android DEX Komutları)**  
**Smali, Android DEX’in assembly dili olup, Java bytecode’unun assembly versiyonudur.**

### **🔹 Smali Kod Örneği**  
```smali
.method public static sum(II)I
    .registers 3
    add-int v0, p0, p1
    return v0
.end method
```

🔹 **Smali Temel Noktalar**  
| **Komut**           | **İşlevi**              |
|---------------------|-------------------------|
| `add-int v0, p0, p1`| p0 ile p1 toplanır, sonuç v0’a yazılır |
| `return v0`         | Hesaplanan sonuç döndürülür |

### **🔹 Smali Kırma Örneği**  
```smali
.method public isVip()Z
    .registers 2
    const/4 v0, 0x1  # Tüm kullanıcıları VIP yap
    return v0
.end method
```

---

# **6️⃣ C Dili vs. Assembly (x86/ARM/Smali)**  
### **🔹 C Kodu**  
```c
int sum(int a, int b) {
    return a + b;
}
```

### **🔹 x86 Assembly**  
```assembly
sum:
    mov eax, edi
    add eax, esi
    ret
```

### **🔹 ARM Assembly**  
```assembly
sum:
    ADD R0, R0, R1
    BX LR
```

### **🔹 Smali Kodu**  
```smali
.method public static sum(II)I
    .registers 3
    add-int v0, p0, p1
    return v0
.end method
```

---

# **🛠 Uygulamalı Görevler**  
1️⃣ **Android cihazın CPU mimarisini kontrol et**  
```bash
cat /proc/cpuinfo
```

2️⃣ **x86 assembly kodunu çalıştır**  
```bash
nasm -f elf64 test.asm
ld -o test test.o
./test
```

3️⃣ **Android APK’yı geri derle**  
```bash
apktool d myapp.apk -o output_dir
```

---

# **📚 Kaynaklar**  
📌 **ARM Komut Seti**  
- ARM Resmi Dokümantasyonu: [https://developer.arm.com/documentation](https://developer.arm.com/documentation)  

📌 **x86 Komut Seti**  
- Intel Kılavuzu: [https://software.intel.com/en-us/articles/intel-sdm](https://software.intel.com/en-us/articles/intel-sdm)  

📌 **Smali Rehberi**  
- Smali Kılavuzu: [https://github.com/JesusFreke/smali](https://github.com/JesusFreke/smali)  

---

🔥 **Görev tamamlandıktan sonra kazanacaklarınız:**  
✅ x86, ARM ve Smali komut setleri arasındaki farklar.  
✅ ARM32 ile ARM64 arasındaki evrim.  
✅ Smali kodlarını çalıştırma ve değiştirme.

🚀 **Sonraki adım (Gün 4):**  
**Sayı Sistemleri: Neden 16’lık Sistem Önemlidir?** 🎯  
