//首頁音樂播放器
const audioPlayer = document.getElementById('audio-playerr');
const playlist = document.getElementById('playlist');
const songs = playlist.querySelectorAll('li');

songs.forEach(song => {
    song.addEventListener('click', () => {
        const src = song.getAttribute('data-src');
        audioPlayer.src = src;
        audioPlayer.play();
    });
});

//歌單播放器
const audioPlayer1 = document.getElementById('audio-player1');
const playlist1 = document.getElementById('playlist1');
const songs1 = playlist1.querySelectorAll('li');

songs1.forEach(song => {
    song.addEventListener('click', () => {
        const src = song.getAttribute('data-src');
        audioPlayer1.src = src;
        audioPlayer1.play();
    });
});

//創作音樂播放器
const audioPlayer2 = document.getElementById('audio-player2');
const playlist2 = document.getElementById('playlist2');
const songs2 = playlist2.querySelectorAll('li');

songs2.forEach(song => {
    song.addEventListener('click', () => {
        const src = song.getAttribute('data-src');
        audioPlayer2.src = src;
        audioPlayer2.play();
    });
});