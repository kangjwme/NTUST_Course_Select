# 臺灣科技大學輔助選課程式

## 免責聲明
此程式僅為教學示範用途，旨在推廣寫程式的樂趣，使用者須自行負責相關責任及追究。



## 前提說明
僅適用於加退選開放時段，初選、暑期選課等不適用於此程式


## 設定說明（以 Google Chrome 為例）
1. 到[Release](https://github.com/kangjwme/NTUST_Course_Select/releases)下載最新版本後解壓縮（或是 git clone 也可以）
2. 到 https://courseselection.ntust.edu.tw/ 點選 F12 開啟開發者工具
3. 點選「應用程式」、「Cookie」，依序複製「ntustsecret」、「ASP.NET_SessionId」、「.AspNet.ApplicationCookie」的「值」到 config.json 中對應的欄位(雙引號""中)。
![](https://i.imgur.com/LoBruKn.png)
![](https://i.imgur.com/lAQ08fz.png)
4. 找到你想要選課的課程代碼，輸入到 config.json 的「CourseNo」中（有範例，記得看）
5. 執行 main.py 檔案，如果成功將會顯示你的名字
```
登入身份：OOO。若登入身分或課碼錯誤，請立即退出，將於 5 秒後開始執行
```


