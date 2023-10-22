// 使用本地存儲保存當前選項卡状态
window.onload = function () {
    var activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
        showTab(activeTab);
    }
};

function showTab(tabNumber) {
    // 隐藏所有選項卡内容
    var tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(function(content) {
        content.style.display = 'none';
    });

    // 显示所选择的選項卡内容
    var selectedTabContent = document.getElementById('content' + tabNumber);
    selectedTabContent.style.display = 'block';

    // 保存當前選項卡狀態到本地儲存
    localStorage.setItem('activeTab', tabNumber);
}

// 其餘的JavaScript保持不變