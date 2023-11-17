document.addEventListener("DOMContentLoaded", function () {
    const openModalBtn = document.getElementById("openModalBtn");
    const closeModalBtn = document.getElementById("closeModalBtn");
    const closeModalAndMaskBtn = document.getElementById("closeModalAndMaskBtn");
    const modal = document.getElementById("myModal");

    const creationSongName = document.getElementById("creation_song_name");
    const creationSongSelect = document.getElementById("creation_song_select");


    openModalBtn.addEventListener("click", function () {
        if (creationSongSelect.value === "null") {
            alert("至少選擇一個人聲");
            return;
        }

        if (creationSongName.value.trim() === '') {
            alert("歌曲名稱不能空白");
            return;
        }

        document.getElementById("creation_song_form").submit();

        modal.style.display = "block";

    });

    closeModalBtn.addEventListener("click", closeModal);
    closeModalAndMaskBtn.addEventListener("click", closeModal);

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    function closeModal() {
        modal.style.display = "none";
    }
});