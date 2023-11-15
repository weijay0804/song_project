const recordButton = document.getElementById("record-button");
const audioPlayer = document.getElementById("audio-player");

let mediaRecorder;
let audioChunks = [];
recordButton.addEventListener("click", (event) => {
    event.preventDefault(); // 阻止按钮的默認行为
    if (isRecording) {
        mediaRecorder.stop();
        recordButton.textContent = "開始錄音";
    } else {
        audioChunks = [];
        startRecording();
        recordButton.textContent = "停止錄音";
    }
});
async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPlayer.src = audioUrl;
            audioPlayer.style.display = "block";
        };

        mediaRecorder.start();
    } catch (error) {
        console.error("錄音失敗：" + error);
    }
}

recordButton.addEventListener("click", () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        recordButton.textContent = "開始錄音";
    } else {
        audioChunks = [];
        startRecording();
        recordButton.textContent = "停止錄音";
    }
});