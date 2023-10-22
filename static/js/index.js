//愛心動畫
const hearts = document.querySelectorAll(".heart");
hearts.forEach(heart => {
heart.addEventListener("click", () => {
    heart.classList.toggle("clicked");
});
});

 // 默認顯示 Tab 1 的内容
 showTab(1);

 function showTab(tabNumber) {
     // 隐藏所有選項卡内容
     var tabContents = document.querySelectorAll('.tab-content');
     tabContents.forEach(function(content) {
         content.style.display = 'none';
     });

     // 顯示所選擇的選項卡内容
     var selectedTabContent = document.getElementById('content' + tabNumber);
     selectedTabContent.style.display = 'block';
 }

 function showNewContent(contentNumber) {
     // 隐藏當前内容區域
     document.getElementById('content2').style.display = 'none';

     // 顯示所選擇的新内容區域
     var newContent = document.getElementById('newContent' + contentNumber);
     newContent.style.display = 'block';
 }

 function returnToContent2() {
     // 隐藏新内容區域
     var newContent = document.querySelectorAll('.tab-content[id^="newContent"]');
     newContent.forEach(function(content) {
         content.style.display = 'none';
     });

     // 顯示原始的内容2
     document.getElementById('content2').style.display = 'block';
 }

 function addImageToContent1(imageSrc) {
     // 創建一个新圖片元素
     var img = document.createElement('img');
     img.src = imageSrc;
     img.alt = '新图片';
     
     // 添加點擊事件處理程序
     img.onclick = function() {
         showNewContent(1);
     };

     // 将圖片添加到内容1中
     var content1Images = document.getElementById('content1Images');
     content1Images.appendChild(img);
 }

 // 添加新的图片到内容1
 addImageToContent1('new-image1.jpg');
 addImageToContent1('new-image2.jpg');


  



