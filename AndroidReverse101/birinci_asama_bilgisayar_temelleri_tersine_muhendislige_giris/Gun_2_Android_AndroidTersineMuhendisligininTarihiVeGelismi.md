# **📜 Gün 2: Android Tersine Mühendisliğinin Tarihi ve Gelişimi**

## **📌 Öğrenme Hedefleri**  
✅ Android tersine mühendisliğinin gelişim sürecini anlamak, erken APK kırılmasından modern uygulama koruma teknolojilerine kadar.  
✅ APK koruma ve kırma arasındaki mücadeleyi kavramak, güçlendirme ve ters güçlendirme gelişimini anlamak.  
✅ Gerçek vakalarla eski ve yeni Android güvenlik mekanizmalarının karşılaştırmasını öğrenmek.  
✅ Modern Android anti-debug tekniklerini öğrenerek sonraki tersine mühendislik analizlerine hazırlık yapmak.

---

## **📖 Bilgi Notları**  

### **1️⃣ Android Tersine Mühendisliğinin Gelişim Süreci**  
Android tersine mühendisliği gelişimi şu aşamalara ayrılır:

| **Aşama**       | **Zaman**   | **Özellikler**                                               |
|-----------------|-------------|--------------------------------------------------------------|
| **Erken Kırma Dönemi** | 2008 - 2012 | APK yapısı basit, doğrulamayı atlamak için `smali` dosyaları değiştirilirdi. |
| **Obfuscation ve İmza Koruması** | 2012 - 2015 | Geliştiriciler `ProGuard` ile kodu karıştırmaya başladı, doğrudan geri derleme engellendi. |
| **Güçlendirme ve Dinamik Koruma** | 2015 - 2018 | 360, Tencent, Baidu gibi firmalar kod çıkarma ve dinamik yükleme teknikleri sundu. |
| **Yapay Zeka ve İleri Güvenlik** | 2019 - Günümüz | Android, `Play Protect` ve `SafetyNet` ile güvenlik seviyesini artırdı, tersine mühendislik zorlaştı. |

---

### **2️⃣ Erken Android Tersine Yöntemleri (2008 - 2012)**  
#### **Örnek 1: VIP Üyelik Kırma**  
2010 civarında birçok uygulama basit `if (isVip) {}` mantığıyla VIP kontrolü yapıyordu.

**🔹 Erken Kırma Yöntemi**  
- `Apktool` ile APK geri derlenir.  
- `smali` kodunda `isVip()` metodu değiştirilir.  
- APK yeniden paketlenip imzalanır.  
- Değiştirilen APK yüklenerek VIP kısıtlaması aşılır.

---

### **3️⃣ Android Uygulama Korumasının Gelişimi (2012 - 2018)**  
🔹 **Kod Karıştırma (ProGuard & R8)**  
- Kod okunamaz hale gelir.

🔹 **Güçlendirme (Dex Şifreleme & Kod Çıkartma)**  
- Kod çalışma zamanında dinamik yüklenir, `classes.dex` şifrelenir.

🔹 **Dinamik Analiz Karşıtı (Anti-Debugging & Anti-Frida)**  
- `Frida` gibi araçlar tespit edilir.

---

### **4️⃣ Modern Android Anti-Debug Teknikleri (2018 - Günümüz)**  
🔹 **SafetyNet & Play Protect**  
- Kötü amaçlı uygulamalar AI ile izlenir, Root ve Hook engellenir.  
- Simülatör, Root, modifiye sistem tespiti yapılır.

🔹 **Modern Koruma Teknolojileri**  
| **Teknoloji**          | **İşlev**                                  |
|-----------------------|--------------------------------------------|
| Kod Karıştırma (ProGuard/R8) | Kodun okunmasını zorlaştırır           |
| DEX Şifreleme         | `classes.dex` okunamaz hale gelir           |
| ShellCode Dinamik Yükleme | Kod çalışma zamanında şifre çözülür       |
| Anti-Debugging        | Debugger tespiti ve işlem sonlandırma       |
| Anti-Hook             | `Frida` ve `Xposed` enjeksiyonu tespiti     |

---

## **🛠 Uygulamalı Görevler**  
1️⃣ 2012 civarı bir APK indirip `apktool` ile geri derle, `AndroidManifest.xml` ve `smali` kodunu incele, `isVip()` metodunu değiştirip doğrulamayı aş.  
2️⃣ Modern bir uygulamayı (`jadx` ile) geri derle, kod karıştırma olup olmadığını kontrol et, `Frida` ile mantığı hook’la.

---

## **📚 Kaynaklar**  
- `Apktool`: https://github.com/iBotPeaches/Apktool  
- `Frida`: https://frida.re  
- `Ghidra`: https://ghidra-sre.org  
- `Jadx`: https://github.com/skylot/jadx  
- `Xposed`: https://repo.xposed.info/module/de.robv.android.xposed.installer  

---

🔥 Görev sonunda:  
✅ Android tersine mühendislik tarihini ve teknik gelişimini öğrenmiş olacaksın.  
✅ Modern Android güvenlik önlemlerini anlayacaksın.  
✅ `apktool` ile APK geri derleme ve analiz yapabileceksin.

🚀 Sonraki adım (Gün 3): CPU Komut Seti Nedir?  
