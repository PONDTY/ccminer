import os, json, time
from progress.spinner import MoonSpinner

# banner
setting_banner = """
███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ 
███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗
╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║
███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝
╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝"""

running_banner = """
██████╗ ██╗   ██╗███╗   ██╗         
██╔══██╗██║   ██║████╗  ██║         
██████╔╝██║   ██║██╔██╗ ██║         
██╔══██╗██║   ██║██║╚██╗██║         
██║  ██║╚██████╔╝██║ ╚████║██╗██╗██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝╚═╝"""

# banner function
def banner(logo):
    os.system("clear")
    
# install miner function 
def install():
    # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
     os.system("git clone https://github.com/PONDTY/ccminer_mmv")

# run miner function
def run():
    print(running_banner)
    with open("set-miner/miner.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        pool = loads['Pool']
        wallet = loads['Wallet']
        password = loads['Pass']
        cpu = loads['Cpu']
    if pool == "" or wallet == "":
        print("pool หรือ wallet กรุณาตั้งค่าใหม่")
        time.sleep(3)
        set_miner()
#     print(pool, wallet, password, cpu)
    print("\033[91mBy : Pond")
    print("\033[93mPool :\033[00m "+pool)
    print("\033[93mwallet :\033[00m "+wallet)
    print("\033[93mpassword :\033[00m "+password)
    print("\033[93mcpu :\033[00m "+str(cpu))

    
    os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")

def set_miner():
    banner(setting_banner)
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("Pool[-o]: ")

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
        wallet = input("Wallet[-u]: ")

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        password = input("Password[-p]: ")

        print("\033[93m 0 ขึ้นไป หรือ เท่ากับจำนวณเธรดCPUท่าน เช็ค 'lscpu'\033[00m")
        cpu = int(input("CPU[-t]: "))

        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
        time.sleep(2)
        set_miner()
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)

while True:
    os.system("clear")
    with MoonSpinner("กำลังทำงาน...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
    if os.path.exists("ccminer_mmv") == False:
        install()
        break
    if os.path.exists("set-miner") == True:
        if os.path.isfile("set-miner/miner.json") == True:
            run()
            break
        else:
            set_miner()
    else:
        os.system("mkdir set-miner")

    
    
