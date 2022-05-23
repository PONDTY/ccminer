# 1 เปิด Termux และรัน ubuntu โดยอัตโมัติ แก้ลงไม่ผ่าน CCMINER-v.1
## ให้ติดตั้ง Linux (ubuntu)
การติดตั้ง
ถ้าติดตั้งแอพ Termux ใหม่ อย่าลืมใช้คำสั่ง ```termux-setup-storage``` ก่อนเพื่อกำหนด dir
```
termux-setup-storage
```
คัดลอกและวางคำสั่งนี้ลงใน Termux:
```
pkg install proot-distro -y
```
```
proot-distro install ubuntu
```
# 2 รัน ubuntu โดยอัตโมัติ
```
pkg install nano && cd /data/data/com.termux/files/usr/etc && nano profile
```
เมื่อใช้คำสั่งด้านบนเสร็จแล้ว และไม่มี error ขั้นตอนต่อไปเราจะมาเพิ่มข้อมูลในไฟล์ profile กันโดยที่ไฟล์นี้
จะเปิดขึ้นมาเองหลังจากใช้คำสั่งด้านบน สิ่งที่จะเพิ่มไปตามระบบที่คุณติดตั้ง
Linux (Debian) เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
```
proot-distro login ubuntu
```
ออกจาก ubuntu จากเทอร์มินัล
```
exit
```
จบขั้นตอน เปิด Termux และรัน ubuntu โดยอัตโมัติ
# 3 AUTO รัน CCMINER-v.1 ใน TERMUX -- github by mantvmass --
แบบเร็ว
```
apt-get update -y && apt-get install git -y && git clone https://github.com/PONDTY/ccminer && cd ccminer && sh setup.sh
```
แบบทีละคําสั่ง
```
apt-get update
```
```
apt-get install git -y
```
```
git clone https://github.com/thaiboy001/ccminer
```
```
cd ccminer
```
```
sh setup.sh
```
หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น
```
run-miner
```
## pool
stratum+tcp://verushash.asia.mine.zergpool.com:3300
```
## wallet
DP31VzSZkefNkfAAEGuG7caFgcyg9438vb
```
แล้ว save
```
## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน pool or wallet ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```
* ออกจาก ubuntu จากเทอร์มินัล  ```exit```
```
## สนับสนุนนักพัฒนา
- ชื่อ ```ภูมินท์ มะลิวรรณ```
- กสิกรไทย ```0608905863```
- พร้อมเพย์ ```0639723211```

## ติดต่อ
* [Facebook](https://www.facebook.com/PhuminMaliwan)
* YouTube
   * [MANTVMASS](https://www.youtube.com/channel/UCYJk0E1wwY3zX-i8tn95mhw)
   * [MOBILE MINING](https://www.youtube.com/channel/UCevNnlKLgRTg-cku5JQ2Ahw) 
