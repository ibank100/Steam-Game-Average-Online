# Steam-Game-Average-Online
<a href=""><img src="Data/a.jpg" width="600px"  height="250"></a><br>
<br><h1>Descriptions</h1>
วิเคราะห์ยอดผู้เล่นสูงสุดต่อวันจากเกมบนsteam เพื่อหาวันที่มีผู้เล่นบนsteamนิยมเล่นกันมากที่สุด<br>
-Data_export.py เก็บข้อมูลจำนวนคนออนไลน์สูงสุดต่อวัน ในเดือนตุลาคม2018ที่ผ่านมา แล้วทำการแยกข้อมูลเหล่านั้น ออกไปเป็นเกมต่อเกม<br>
-Day_Average.py ใส่ลิสข้อมูลลงไป(รับค่าเป็นlist) โดยโค้ดนี่จะแสดงผลค่าเฉลี่ยจำนวนคนออนไลน์ในแต่ละวันออกมา จะรันตั้งแต่วันจันทร์เป็นวันแรก(1ตุลา2018เป็นวันจันทร์พอดี)<br>
## Target
-เป้าหมายของโปรเจ็ค คือ ต้องการศึกษาจำนวนของผู้เล่นเกม DOTA2, CS:GO, POE, PUBG, Rainbow Six เพื่อเปรียบเทียบจำนวนผู้เล่นของแต่ละเกม<br>
## Results
-นำข้อมูลการออนไลน์ของผู้เล่น เพื่อหาวันที่มีจำนวนผู้เล่นสูงสุดนำไปต่อยอดอธิเช่น การจัดกิจกรรม อีเวนท์ภายในเกม หรือควรเลือกปิดปรับปรุงเซิฟเวอร์ในวันที่คนเล่นน้อยที่สุดเพื่อส่งผลกระทบกับตัวผู้เล่นน้อยที่สุดเป็นต้น
## ผลการทำงาน
หลังจากนำข้อมูลมาวิเคราะห์ จะได้ผลลัพธ์ดังนี้
  - PLAYERUNKNOWN'S BATTLEGROUNDS
  ![PUBG](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/PLAYERUNKNOWN'S%20BATTLEGROUNDS.svg)
  - DOTA 2
  ![DOTA2](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/DOTA%202.svg)
  - Counter-Strike: Global Offensive
  ![CSGO](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/COUNTER-STRIKE%20GLOBAL%20OFFENSIVE.svg)
  - Path of Exile
  ![POE](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/PATH%20OF%20EXILE.svg)
  - Tom Clancy's Rainbow Six Siege
  ![RAINBOW6](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/TOM%20CLANCY'S%20RAINBOW%20SIX%20SIEGE.svg)
และสุดท้ายคือ ค่าเฉลี่ยจำนวนผู้เล่นออนไลน์ของทั้ง 5 เกม ต่อวัน
  ![ALLGAME](https://github.com/ibank100/Steam-Game-Average-Online/blob/master/Graph/ALL%20GAME%20LIST.svg)
## ข้อมูลมาจาก
- https://steamdb.info/graph/?fbclid=IwAR05OA_gA3hQPdUil1VGjdzsNfDexe_y12n1_JXWwFAgZBXTiwraEBeAYOE
- https://steamcharts.com/
## เครื่องมือที่ใช้
- Python
- Pygal
## Project's member
๐ นายสินสวัสดิ์ อภิชัยสมพล - 61070240<br>
๐ นายภาคภูมิ สวัสดี - 61070158<br>
๐ นายพสธร ภักดิ์แจ่มใส - 61070132<br>
๐ นายวรรธนะ มนรักษา - 61070202<br>
