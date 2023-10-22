document.addEventListener("DOMContentLoaded", function () {
    const tabButtons = document.querySelectorAll(".tab11-person");
    const tabContents = document.querySelectorAll(".section2");
    
    tabButtons.forEach(button => {
        button.addEventListener("click", function () {
            const tabId = this.getAttribute("data-tab");
            // 隱藏所有內容
            tabContents.forEach(content => {
                content.style.display = "none";
            });
            // 顯示所選內容
            const selectedTab = document.getElementById(tabId);
            selectedTab.style.display = "block";
             });
        });
    });

    // 獲取所有打開框架的按钮
    const openModalButtons = document.querySelectorAll(".music-btn");
    // 為每個按钮添加點擊事件
    openModalButtons.forEach(button => {
        button.addEventListener("click", function() {
            const targetModalId = this.getAttribute("data-target");
            const targetModal = document.getElementById(targetModalId);

            if (targetModal) {
                 targetModal.style.display = "block";
            }
        });
    });


