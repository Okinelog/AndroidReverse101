### **📜 Gün 1: Tersine Mühendislik Nedir?**

#### **📌 Öğrenme Hedefleri**
✅ **Tersine mühendisliğin** ne olduğunu ve uygulama alanlarını öğrenmek  
✅ **Tersine mühendislik** ile **doğrudan mühendislik** arasındaki farkları anlamak  
✅ **Yazılım tersine mühendisliği** ile ilgili temel kavramlara (statik analiz, dinamik analiz) aşina olmak  
✅ Temel tersine mühendislik araçlarını tanımak ve kurulum yapmak

---

#### **📖 Bilgi Notları**

### **1️⃣ Tersine Mühendislik Nedir?**
Tersine mühendislik, mevcut bir sistemin **yapısını, işlevini ve çalışma mantığını** analiz ederek anlamaya çalışma sürecidir.

🔹 Tersine mühendisliğin özü **parçalarına ayırmak ve anlamak**tır; sadece yazılımda değil, donanımda, ağ protokollerinde, güvenlik araştırmalarında ve hatta yapay zekâ modellerinde de kullanılır.

### **2️⃣ Tersine Mühendisliğin Uygulama Alanları**
| **Alan**           | **Uygulama**                                       |
|--------------------|----------------------------------------------------|
| **Yazılım Analizi**| Uygulama analizleri, yazılım kırma, protokol analizi, API inceleme |
| **Güvenlik**       | Zararlı yazılım analizi, zafiyet araştırma, virüs inceleme, web güvenliği |
| **Donanım Analizi**| Çip analizi, PCB tasarımı, IoT cihazlarını inceleme |
| **Yapay Zekâ**     | Model analizleri, ağırlık çıkartma, optimizasyon   |
| **Oyun Tersine**   | Oyun içi hile geliştirme, kaynak çıkartma, ağ trafiği inceleme |

**🌟 Örnek 1: Yazılım Kırma**  
- Bir **ücretli uygulamanın** satın alma doğrulamasını analiz ederek kısıtlamaları aşmaya çalışmak

**🌟 Örnek 2: Protokol Analizi**  
- Sadece resmi istemciye açık bir API’yi analiz edip kendine özel bir istemci yazmak

### **3️⃣ Tersine Mühendislik vs. Doğrudan Mühendislik**
|                | **Doğrudan Mühendislik** | **Tersine Mühendislik**      |
|----------------|-------------------------|------------------------------|
| **Bakış Açısı** | Tasarlayıp oluşturmak   | Parçalayıp analiz etmek      |
| **Amaç**        | Sıfırdan ürün geliştirmek| Var olan ürünü anlamak       |
| **Alan**        | Yazılım geliştirme, sistem tasarımı | Kırma, zafiyet bulma, optimizasyon  |
| **Araçlar**     | IDE’ler (VS Code, Android Studio) | Geri derleyici, debugger   |

### **4️⃣ Statik Analiz vs. Dinamik Analiz**
|                | **Statik Analiz**               | **Dinamik Analiz**              |
|----------------|---------------------------------|---------------------------------|
| **Yöntem**     | Dosya ve kodu doğrudan incelemek| Programı çalıştırıp izlemek     |
| **Araçlar**    | Geri derleyici (jadx, Ghidra)   | Debugger (Frida, GDB, LLDB)     |
| **Avantajı**   | Hızlı analiz, anti-debug tetiklemeden| Gerçek ortamda davranışı gözleme |
| **Dezavantajı**| Bazen tüm mantığı görememe       | Anti-debug korumalarına takılma |

---

#### **🛠️ Uygulamalı Görevler**
1️⃣ **Temel Tersine Araçlarını Kur**  
🔹 **jadx** (APK geri derleyici) indir, `classes.dex` analiz et  
🔹 **Frida** (hook aracı) kur, basit bir Python scriptini hookla  
🔹 **Ghidra / IDA Free** kur, bir ELF dosyasını incele  

2️⃣ **Basit Bir APK Analiz Et**
- Herhangi bir **APK dosyasını** indir (örn: `Calculator.apk`)
- `jadx` ile decompile edip `MainActivity.java` kodunu incele

---

#### **📚 Kaynaklar**
📌 **Android Tersine Araçları**  
- `jadx` : [https://github.com/skylot/jadx](https://github.com/skylot/jadx)  
- `Frida` : [https://frida.re](https://frida.re)  
- `Ghidra`: [https://ghidra-sre.org](https://ghidra-sre.org)  
- `APKTool`: [https://github.com/iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool)  

📌 **Tavsiye Edilen Okumalar**  
- Android Yazılım Güvenliği ve Tersine Analiz  
- The Art of Reverse Engineering  
- Tersine mühendislik blogu: [https://reverseengineering.stackexchange.com](https://reverseengineering.stackexchange.com)  

---

🔥 **Bu günü tamamladığında öğreneceklerin:**  
✅ Tersine mühendisliğin temel kavramları  
✅ Tersine ve doğrudan mühendisliğin farkları  
✅ Temel araç kurulum ve kullanımı

🚀 **Bir Sonraki Adım (Gün 2):** Android tersine mühendisliğin tarihi ve gelişimi 🎯
