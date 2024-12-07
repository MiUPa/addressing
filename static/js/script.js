let player;
let isReady = false;

// YouTube IFrame Player APIの準完了時に呼ばれる
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '0',
        width: '0',
        videoId: '3JWTaaS7LdU', // 公式動画のIDに変更
        playerVars: {
            'autoplay': 0,
            'controls': 0
        },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    isReady = true;
    // 音量を50%に設定
    player.setVolume(50);
}

function onPlayerStateChange(event) {
    // 必要に応じて再生状態の変更を処理
}

document.addEventListener('DOMContentLoaded', function() {
    const editor = document.getElementById('editor');

    editor.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && isReady) {
            // サビの部分から再生（約1分17秒）
            player.seekTo(77);
            player.playVideo();
        }
    });
}); 