class Telebe():  # Python-da bir sinif təyin etmək üçün "class" açar sözündən istifadə olunur.

   # Sinif dəyişəni
   mekteb_adi = "1 Nömrəli Məktəb"

   # Statik metodlar
   @staticmethod
   def yashi_boyukdurmu(telebe):
       if telebe.yash > 18:
           return "_icaze_verilir_"
       else:
           return "_icaze_verilmir_"

   # Konstruktor
   def __init__(self, ad, yash, unvan, sira_nomresi):
       # __init__() funksiyası hər dəfə sinif yeni obyekt yaratmaq üçün istifadə olunanda avtomatik olaraq çağrılır.
       self.ad = ad
       self.yash = yash
       self.unvan = unvan
       self.sira_nomresi = sira_nomresi

   # İnstans metodları
   def ozunu_tesdiqle(self):
       return f"Adım {self.ad} və yaşım {self.yash}"

   def proqramlasdirma_bacarigi(self, python_bilir=False):
       if python_bilir:
           return f"{self.ad} Python proqramlaşdırma dilini bilir"
       else:
           return f"{self.ad} Python proqramlaşdırma dilini bilmir"

   def mugeyet_oxuya_biler(self, mugeyet_oxuya_bilir=False):
       if mugeyet_oxuya_bilir:
           return f"{self.ad} muğəyyət oxuya bilər"
       else:
           return f"{self.ad} muğəyyət oxuya bilməz"

################################################################################################

# Üç obyekt yaradılır
telebe_1 = Telebe("Hesen", 15, "Bakı", "322718")
telebe_2 = Telebe("Zaman", 17, "Quba", "296584")
telebe_3 = Telebe("Qasım", 16, "Lənkəran", "289658")

# Obyekt metodlarına müraciət
print(telebe_1.ozunu_tesdiqle())
print(telebe_1.proqramlasdirma_bacarigi(True))
print(telebe_3.mugeyet_oxuya_biler(mugeyet_oxuya_bilir=True))
print(telebe_2.mugeyet_oxuya_biler(mugeyet_oxuya_bilir=False))

# Obyekt xüsusiyyətlərini dəyişdirmək
telebe_1.ad = "Ramazan"

# Obyekt xüsusiyyətlərini silmək
del telebe_1.sira_nomresi

# Yaş həddi üçün nəzarət
print(Telebe.yashi_boyukdurmu(telebe_1))
print(Telebe.yashi_boyukdurmu(telebe_2))
print(Telebe.yashi_boyukdurmu(telebe_3))