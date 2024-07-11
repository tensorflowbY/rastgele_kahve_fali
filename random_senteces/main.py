import random

print("Giriş kısmına kahve yazarsanız sizin için bir fal bakılacaktır.")

while True:
    user_input=input("Yazınız: ").lower()


    if user_input == "kahve":

        # Metin dosyasını okuyup cümleleri bir listeye ekleme
        with open('random_sentence.txt', 'r', encoding='utf-8') as file:
            sentences = file.readlines()

        # Listeyi temizleyip (satır sonu karakterlerinden arındırma) rastgele bir cümle seçme
        sentences = [sentence.strip() for sentence in sentences]

        random_sentence = random.choice(sentences)

        print(random_sentence)

    if user_input != "kahve":
        print("Hataı giriş.")
        break

