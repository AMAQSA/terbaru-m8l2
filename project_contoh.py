#import
import pyautogui , time , random , discord , os , requests







#list
pesan = []
game = ["spam chat, ","random nama, ","auto cliker, " ,"discord"]

#variable
waktu = 10

#aksesoris
a = ("_____________________________________________________________________________________________")

#pertanyaan bukan di for i
jenis_game = input("Welcome to game from aqsa, mau game apa?" + " ada " + game[0] + game[1] + game[2] + game[3] + ":" )
print(a)
#game yang pertama
if jenis_game == "spam":
    pertanyaan_berapa_diulang = int(input("mau berapakali di spam nya?:"))
    print(a)
    pesannya = int(input("pesannya mau brp?:"))
    print(a)
    for i in range(pesannya):
        pertanyaan_mau_pesan_apa = input("pesannya mau apa:")
        print(a)
        pesan.append(pertanyaan_mau_pesan_apa)
        print("pesan ditambahkan ke list")
        print(a)
        time.sleep(0.5)
    print("arahkan kursor ke kotak pesan")
    time.sleep(1)
    print(a)
    for i in range(10):
        print("program akan di mulai dalam waktu",waktu)
        print(a)
        waktu = waktu - 1
        time.sleep(1)
    for i in range(pertanyaan_berapa_diulang):
        posisi = pyautogui.position()
        random_teks = random.choice(pesan)
        pyautogui.click(posisi.x,posisi.y)
        pyautogui.typewrite(random_teks)
        pyautogui.press("enter")
        time.sleep(1)
    print("Program spam sudah selesai \n anda bisa memilih game apa yang mau di mainkan lagi \n program break selama 10 detik")
    time.sleep(10)
        
#GAME MENGACAK NAMA


#variable
nama = []
a = 0
enter = "____________________________________________________"


#aksesoris V1
print(enter)

#game ke 2
if jenis_game == "random nama":
    orang = int(input("Mau berapa orang:"))
    #masukkan nama orang
    for i in range(orang):
        a = a + 1 
        masukkan_nama = input("Nama orang ke " + str(a) + " :" )
        nama.append(masukkan_nama)

    #diacak berapa kali?
    acak = int(input("Mau di ulang berapa kali?"))

    #aksesoris V1
    print(enter)

    #pengacakan nama
    for i in range(acak):
        acak = acak - 1
        x = random.choice(nama)
        print(x , acak ,"proses lagi")
        time.sleep(0.5)
        print(enter)

    #hasil pengacakan nama
    print("Yang kena adalah", x )

#valiable_2
waktu_2 = 0
count = 0

#game ke 3
if jenis_game == "auto cliker":
    pertanyaan_click = int(input("Mau berapa kali di klik nya?"))
    pertanyaan_mode_click = input("Mau yang pake jeda atau tidak?")
    if pertanyaan_mode_click == "tidak":
        for i in range(10):
            waktu_2 = waktu_2 + 1
            print("Arahkan ke game atau apk yang ingin di klik, auto kliker ini akan berjalan dalam waktu",waktu_2)
            time.sleep(1)
        for i in range(pertanyaan_click):
            count = count + 1
            print("program sedang menjalan kan tugas sebanyak" ,count, "kali")
            posisi_2 = pyautogui.position()
            pyautogui.click(posisi_2.x,posisi_2.y)
        print("Program telah selesai")    
    elif pertanyaan_mode_click == "ya":
        pertanyaan_waktu = input("jedanya mau berapa?")
        for i in range(10):
            waktu_2 = waktu_2 + 1
            print("Arahkan ke game atau apk yang ingin di klik, auto kliker ini akan berjalan dalam waktu",waktu_2)
            time.sleep(1)
        for i in range(pertanyaan_click):
            count = count + 1
            print("program sedang menjalan kan tugas sebanyak" ,count, "kali")
            posisi_2 = pyautogui.position()
            pyautogui.click(posisi_2.x,posisi_2.y)
            if pertanyaan_waktu >= "1":
                time.sleep(int(pertanyaan_waktu)) 
            if pertanyaan_waktu == "0.9":
                time.sleep(0.9)
            if pertanyaan_waktu == "0.8":
                time.sleep(0.8)
            if pertanyaan_waktu == "0.7":
                time.sleep(0.7)
            if pertanyaan_waktu == "0.6":
                time.sleep(0.6)
            if pertanyaan_waktu == "0.5":
                time.sleep(0.5)
            if pertanyaan_waktu == "0.4":
                time.sleep(0.4)
            if pertanyaan_waktu == "0.3":
                time.sleep(0.3)
            if pertanyaan_waktu == "0.2":
                time.sleep(0.2)
            if pertanyaan_waktu == "0.1":
                time.sleep(0.1)
            if pertanyaan_waktu == "0":
                time.sleep(0)
            else:
                print("maaf anda salah memasukan angka")
        print("Program telah selesai")
if jenis_game == "discord":
    from discord.ext import commands
    from model import get_class
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)
    
   
    list = ["hello","heh","spam","ukuran_layar","tolong"]

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command()
    async def hello(ctx):
        await ctx.send(f'Hi! I am a bot {bot.user}!')

    @bot.command()
    async def heh(ctx, count_heh = 5):
        await ctx.send("he" * count_heh)

    @bot.command()
    async def spam(ctx):
        a = 0
        for i in range(10):
            a = a + 1
            await ctx.send("halo" + str(a))
            time.sleep(1)

    @bot.command()
    async def ukuran_layar(ctx):
        await ctx.send(pyautogui.size())

    @bot.command()
    async def tolong(ctx):
        await ctx.send("ini list game nya:")
        for i in range(4):
            await ctx.send(list[i])
    

    @bot.command()
    async def check(ctx):
        if ctx.message.attachments:
            for attachment in ctx.message.attachments:
                file_name = attachment.filename
                file_url = attachment.url
                await attachment.save(f"./{attachment.filename}")
                await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
        else:
            await ctx.send("Anda lupa mengunggah gambar :(")

    bot.run("MTEwNjgwNTAxMDI5NTE3MzE3MA.GXU6Kj.lyAEnmIqQtxYVJlEWMkaH7qtIqinL5j-yZGcWU")
else:
    print ("maaf adanya cuma")
    for i in range(4):
        print(game[i])