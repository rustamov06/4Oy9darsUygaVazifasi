# 4 Oy 9 dars Uyga vazifa

# 1 vazifa

# import threading
# import time
# def raqamlar_yigindisi(num):
#     yigindi = 0
#     for raqam in num:
#         yigindi += int(raqam)
#         time.sleep()
#     print(f"Raqamlar yig'indisi: {yigindi}")
# def son_kiritish_va_hisoblash():
#     num = input("Son kiriting: ")
#     if num.isdigit():
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=raqamlar_yigindisi, args=(num,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Arixmetik amal bajarish uchun ketgan vaqt {round(end - start, 2)} vaqt ketdi.")
#     else:
#         print("Siz son kiritmadingiz!!!")
#
#
# son_kiritish_va_hisoblash()
# son_kiritish_va_hisoblash()


#--------------------------------------------------------------------------------------------------------

# 2 vazifa

# import threading
# import time
#
# def sekundlarni_formatlash(sekundlar):
#     kun = sekundlar // 86400
#     sekundlar %= 86400
#     soat = sekundlar // 3600
#     sekundlar %= 3600
#     minut = sekundlar // 60
#     sekundlar %= 60
#     time.sleep(0.5)
#     print(f"Natija: {kun} kun, {soat} soat, {minut} minut, {sekundlar} sekund")
# def son_kiritish_va_hisoblash():
#     try:
#         sekundlar = int(input("Sekundlar sonini kiriting: "))
#         if sekundlar < 0:
#             print("Musbat son kiriting!")
#             return
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=sekundlarni_formatlash, args=(sekundlar,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except ValueError:
#         print("Iltimos, faqat son kiriting!")
# son_kiritish_va_hisoblash()
# son_kiritish_va_hisoblash()


#--------------------------------------------------------------------------------------------------------

# 3 vazifa

# import threading
# import time
#
# def bosh_harflarni_katta_qilish(names):
#     natija = [name.capitalize() for name in names]
#     time.sleep(0.5)
#     print(f"Natija: {natija}")
#
# def ab():
#     try:
#         names = input("Ismlar ro'yxatini vergul bilan ajratib kiriting: ").split(',')
#         names = [name.strip() for name in names]
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=bosh_harflarni_katta_qilish, args=(names,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()


#--------------------------------------------------------------------------------------------------------

# 4 vazifa

# import threading
# import time
#
# def katta_baholarni_topish(scores):
#     natija = [score for score in scores if score > 75]
#     time.sleep(0.5)
#     print(f"Natija: {natija}")
# def baholarni_kiritish_va_filtrlash():
#     try:
#         scores = list(map(int, input("Baholar ro'yxatini vergul bilan ajratib kiriting: ").split(',')))
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=katta_baholarni_topish, args=(scores,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except ValueError:
#         print("Iltimos, faqat son kiriting!")
# baholarni_kiritish_va_filtrlash()



#--------------------------------------------------------------------------------------------------------

# 5 vazifa

# import threading
# import time
#
# def palindrom_sozlarni_topish(words):
#     natija = [word for word in words if word.lower() == word[::-1].lower()]
#     time.sleep(0.5)
#     print(f"Natija: {natija}")
# def sozlarni_kiritish_va_filtrlash():
#     try:
#         words = input("So'zlar ro'yxatini vergul bilan ajratib kiriting: ").split(',')
#         words = [word.strip() for word in words]  # Bo'sh joylarni olib tashlash
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=palindrom_sozlarni_topish, args=(words,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# sozlarni_kiritish_va_filtrlash()



#--------------------------------------------------------------------------------------------------------

# 6 vazifa

# import threading
# import time
#
# def bc(matn):
#     natija = ""
#     for harf in matn:
#         if harf.lower() == 'e':
#             natija += '3'
#         else:
#             natija += harf
#     time.sleep(0.5)
#     print(f"Natija: {natija}")
# def ab():
#     try:
#         matn = input("Matn kiriting: ")
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=bc, args=(matn,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()


#--------------------------------------------------------------------------------------------------------

# 7 vazifa

# import threading
# import time
#
# def remove_spaces(matn):
#     natija = ""
#     i = 0
#     while i < len(matn):
#         if matn[i] != " ":
#             natija += matn[i]
#         i += 1
#     return natija
# def bc(matn):
#     natija = remove_spaces(matn)
#     time.sleep(0.5)
#     print(f"Yangilangan matn: {natija}")
# def ab():
#     try:
#         matn = input("Matn kiriting: ")
#         print("Hisoblanmoqda...")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=bc, args=(matn,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()


#--------------------------------------------------------------------------------------------------------

# 8 vazifa

# import threading
# import time
#
# def multiply_by_2(index, ro_yxat):
#     ro_yxat[index] *= 2
#     print(f"Element {index+1} ko'paytirildi: {ro_yxat[index]}")
# def ab():
#     try:
#         ro_yxat = [i+1 for i in range(10, 20, 1)]
#         print(f"Boshlang'ich ro'yxat: {ro_yxat}")
#         print("Hisoblanmoqda...")
#         start = time.time()
#         threads = []
#         for i in range(len(ro_yxat)):
#             hisoblash_oqimi = threading.Thread(target=multiply_by_2, args=(i, ro_yxat))
#             threads.append(hisoblash_oqimi)
#             hisoblash_oqimi.start()
#         for oqim in threads:
#             oqim.join()
#         end = time.time()
#         print(f"Yangilangan ro'yxat: {ro_yxat}")
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()


#--------------------------------------------------------------------------------------------------------

# 9 vazifa

# import threading
# import time
# import random
#
# def generate_random_number(index):
#     random_number = random.randint(1, 100)
#     print(f"Son {index+1}: Tasodifiy son {random_number}")
# def ab():
#     try:
#         print("Hisoblanmoqda...")
#         start = time.time()
#         threads = []
#         for i in range(10):
#             hisoblash_oqimi = threading.Thread(target=generate_random_number, args=(i,))
#             threads.append(hisoblash_oqimi)
#             hisoblash_oqimi.start()
#         for oqim in threads:
#             oqim.join()
#         end = time.time()
#         print(f"Amalni bajarish uchun ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()

#==============================================UYGA VAZIFA========================================================