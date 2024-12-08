let player;
let isReady = false;

// デバッグ用のログ追加
console.log('Script loaded');

function onYouTubeIframeAPIReady() {
    console.log('YouTube API Ready');
    player = new YT.Player('player', {
        height: '0',
        width: '0',
        videoId: '3JWTaaS7LdU',
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
    console.log('Player is ready');
    isReady = true;
    player.setVolume(50);
}

function onPlayerStateChange(event) {
    console.log('Player state changed:', event.data);
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded');
    const editor = document.getElementById('editor');

    editor.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && isReady) {
            console.log('Enter pressed, attempting to play');
            player.seekTo(77);
            player.playVideo();
        }
    });
});