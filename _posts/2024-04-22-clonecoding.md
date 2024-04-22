---
title: 화면 만들기
date: 2024-03-29 00:00:00 +09:00
categories: [html,]
---
flex를 사용해 화면 clone coding 하기.
```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>first coding</title>
    <style>
        
    body,html {
       
       height: 100%;
       
   }

   body {
       width: 1000px;
       display: flex;
       flex-direction: column;
       margin: 0px;
   }

   html {
       display: flex;
       justify-content: center;
       align-items: center;
       flex-direction: column;
   }

   header {
       background-color: #2d3a4b;
       height: 100px;
       padding: 1%;
   }
   
   #menu {
       color: white;
       padding-top: 0.3%;
       font-size: 15PX;
       display: flex;
       justify-content: flex-end;
       align-items: flex-end;
   }

   #logo {
       padding-left: 18px;
       display: flex;
       justify-content: flex-start;
   }

   #logo>img {
       width: 220px;
   }

   #category {
       margin-left: 26%;
       margin-right: 26%;
       font-size: 16px;
       display: flex;
       flex-direction: row;
       align-content: end;
       flex-wrap: wrap;
       justify-content: space-around;
       align-items: center;
   }

   #category>div {
       color: white;
   }
   #topImg {
       background-image: url(https://images-ext-1.discordapp.net/external/sG9mnFSJldckI8fmoJI0k8OyaO88f1GQpNg7rU4RJeI/https/firstcoding-kr.github.io/deep-web/html/website/main.jpg?format=webp&width=600&height=400);
       background-size: cover;
       height: 500px;
       background-repeat: no-repeat;
       display: flex;
       justify-content: center;
       align-items: center;
   }
   #topImg>p {
       color: white;
       font-size: 30pt;
       font-weight: bold;
       text-shadow: 3px 4px 5px black;
   }

   .line {
       display: flex;
       justify-content: space-between;
       align-items: center;
       margin: 50px;
       padding-left: 1%;
       padding-right: 1%;
   }


   .line>.content>img {
           padding-top: 15px;
           width: 260px;
   }

   
   footer {
       background-color: #f5f6f7;
       margin: 0px;
       padding-top: 60px;
       padding-bottom: 25px;
       width: 100%;
       height: 7%;
       margin-top: auto;
       display: flex;
       flex-direction: row;
       justify-content: space-evenly;
   
   }

   #logo2 {
       height: 60px;
       display: flex;

   }
   #name {
       font-size: 24px;
       font-weight: bold;
   }
    </style>
    

<body>
    <header>
        <div id="menu">
            HOMEㅣNOTICEㅣLOGINㅣJOIN   
        </div>
        <div id="logo">
            <img src="https://images-ext-1.discordapp.net/external/F1GPeRU-DLxRK8U2l4kGC6wAe4EuKXK06ihzjd6PqK8/https/firstcoding-kr.github.io/deep-web/html/website/logo.png?format=webp&quality=lossless&width=600&height=147"
                alt="">
        </div>
        <div id="category">
            <div>COMPANY</div> 
            <div>PRODUCT</div> 
            <div>CUSTOMER</div> 
            <div>SERVICE</div>
            <div>RECRUIT</div>
        </div>
    </header>

    <div id="topImg">
        <p>코딩의 시작, 퍼스트 코딩</p>
    </div>

    <div class="line">
        <div class="content">
            <img src="https://images-ext-1.discordapp.net/external/H6tz4KQO4yp5u-aSbBHuoEEOCSyoluvzJyHwnciEs4o/https/firstcoding-kr.github.io/deep-web/html/website/banner1.jpg?format=webp&width=316&height=450"
                alt="">
        </div>
        <div class="content">
            <img src="https://images-ext-1.discordapp.net/external/fAqEDomBCqmRm07d9Cnq2BbI8I9QaUeUgHN1Q2yX30g/https/firstcoding-kr.github.io/deep-web/html/website/banner2.jpg?format=webp&width=316&height=450"
                alt="">
        </div>
        <div class="content">
            <img src="https://images-ext-1.discordapp.net/external/XJr-Ehu0-x1XsjDKiaAaqfSOsdRhFfbRSFR6Ny0Fi5Q/https/firstcoding-kr.github.io/deep-web/html/website/banner3.jpg?format=webp&width=316&height=450"
                alt="">
        </div>
    </div>

    <footer>
        <div id="logo2">
            <img src="https://images-ext-1.discordapp.net/external/F1GPeRU-DLxRK8U2l4kGC6wAe4EuKXK06ihzjd6PqK8/https/firstcoding-kr.github.io/deep-web/html/website/logo.png?format=webp&quality=lossless&width=600&height=147"
                alt="">
        </div>
        <div id="text">
            <div id="name">퍼스트코딩학원</div>
            <div id="address">경남 진주시 초전북로 57, 3층</div>
        </div>
    </footer>
</body>

</html>
```