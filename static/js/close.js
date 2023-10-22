 // 獲取所有關閉框的按鈕 
 const closeButtons = document.querySelectorAll(".close-voice");
 const confirmButton = document.querySelector(".s2-vd-2"); // 這是你的 "確定" 按钮
 
 // 為每個關閉按鈕添加點擊事件
 closeButtons.forEach(button => {
     button.addEventListener("click", function() {
         const targetModalId = this.getAttribute("data-target");
         const targetModal = document.getElementById(targetModalId);
 
         if (targetModal) {
             targetModal.style.display = "none";
         }
     });
 });
 
 // "確定" 按鈕點擊事件
 confirmButton.addEventListener("click", function() {
     const targetModalId = confirmButton.getAttribute("data-target");
     const targetModal = document.getElementById(targetModalId);
 
     if (targetModal) {
         targetModal.style.display = "none";
     }
 });
 
 