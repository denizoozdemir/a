d = int(input(" uzun kenarın degerini giriniz : ")) # kullanıcıdan dikdortgenin prizmanın uzun kenarın degeri isteniliyor
e = int(input(" kısa kenarın degerini giriniz : ")) # kullanıcıdan dikdörtgenin prizmanın kısa kenarın degeri isteniliyor
n = int(input(" yükseklik degerini giriniz : "))    # kullanıcıdan dikdörtgenin prizmanın yükseklik degeri isteniliyor
c =int(2)
alan =c*d*e+c*d*n+c*e*n  #alan hesaplaması yapar 
hacimi = d*e*n           #hacim hesaplaması yapar
print("Hacim :" ,hacimi) #hesaplanan dikdörtgenin prizmanın hacimini verir
print("Alan :" ,alan)    #hesaplanan dikdörtgenin prizmanın alanını verir
