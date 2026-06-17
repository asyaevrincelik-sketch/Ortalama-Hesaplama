vize_puanı = int(input("Lütfen vize notunuzu girin: "))
final_puanı = int(input("Lütfen final notunuzu girin: "))

ortalama_hesaplama = (vize_puanı * 40 + final_puanı * 80) / (40 + 80)

print(f"Vize Puanınız: {vize_puanı}\nFinal Puanınız: {final_puanı}\nOrtalamanız: {ortalama_hesaplama:.2f}")

if ortalama_hesaplama < 50:
    print("Kaldınız.")
else:
    print("Tebrikler, geçtiniz!")





