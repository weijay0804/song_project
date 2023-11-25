//首頁音樂播放器
const indexAudioPlayer = document.getElementById('audio-playerr');
const playlist = document.getElementById('playlist');
const songs = playlist.querySelectorAll('li');

songs.forEach(song => {
    song.addEventListener('click', () => {
        const src = song.getAttribute('data-src');
        indexAudioPlayer.src = src;
        indexAudioPlayer.play();
    });
});

// 推薦歌曲播放器
const recommendAudioPlayer = document.getElementById('recommend-audio-player');
const recommend_list = document.getElementById('recommend-list');
const recommend_song = recommend_list.querySelectorAll('li');

recommend_song.forEach(song => {
    song.addEventListener('click', () => {
        console.log("test")
        const src = song.getAttribute('data-src');
        recommendAudioPlayer.src = src;
        recommendAudioPlayer.play();
    });
});

//歌單播放器
const audioPlayer1 = document.getElementById('audio-player1');
const playlist1 = document.getElementById('playlist1');
const songs1 = playlist1.querySelectorAll('li');

songs1.forEach(song => {
    song.addEventListener('click', () => {
        console.log("test")
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