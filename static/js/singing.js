var imageGroups = document.querySelectorAll(".one-group");

imageGroups.forEach(function (group) {
  var clickableImage = group.querySelector(".singimg2");
  var hiddenImage = group.querySelector(".check");
  var h4_title = group.querySelector(".singer-name");
  hiddenImage.style.display = "none"; // 隱藏初始狀態

  clickableImage.addEventListener("click", function () {
    if (hiddenImage.style.display === "none") {
      hiddenImage.style.display = "block"; // 顯示

      addToFavoriteSingerSelect(h4_title.getAttribute("option-index"))

    } else {
      removeFromFavoriteSingerSelect(h4_title.getAttribute("option-index"))
      hiddenImage.style.display = "none"; // 隱藏
    }
  });
});

// 控制最愛歌手表單送出動作
// 會驗證選取的資料是否有三個
function favoriteSingerSubmit() {
  var selectElement = document.getElementById("favorite_singers_select");

  var selectedOptionsCount = Array.from(selectElement.selectedOptions).length;

  if (selectedOptionsCount >= 3) {
    document.getElementById("page2").submit();
  } else {
    alert("至少選擇三個！");
  }
}

// 將選取的歌手加入至表單的 select 選取元素中
function addToFavoriteSingerSelect(option_index) {
  const selectElement = document.getElementById("favorite_singers_select");

  selectElement.options[option_index].selected = true;
}

// 將選取的歌手移除表單的 select 選取元素中
function removeFromFavoriteSingerSelect(option_index) {
  const selectElement = document.getElementById("favorite_singers_select");

  selectElement.options[option_index].selected = false;
}

// 獲取 Modal 元素
const registerModal = document.getElementById('id01');
// 設置註冊步驟的索引
let registerStepIndex = 1;

//document.getElementById('page2').style.display = 'none';

// 顯示下一步註冊步驟
function showNextStep() {
  if (registerStepIndex === 1) {
    document.getElementById('page1').style.display = 'none';
    document.getElementById('page2').style.display = 'block';
    registerStepIndex = 2;
  };
}

// 獲取關閉按鈕和 modal 元素
const closeButton = document.getElementById('closeButton');
const modal = document.getElementById('id02'); // 假設 modal 的 id 是 "myModal"
// 添加事件監聽器來關閉 modal
closeButton.addEventListener('click', closeModal);
// 關閉 modal 的函數
function closeModal() {
  modal.style.display = 'none';
} 