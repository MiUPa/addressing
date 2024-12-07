let score = 0;
let timer = 0;
let gameInterval;
let currentQuote = '';
let player;

const quoteDisplay = document.getElementById('quote-display');
const quoteInput = document.getElementById('quote-input');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');
const characterName = document.getElementById('character-name');
const startButton = document.getElementById('start-btn');
const toggleMusic = document.getElementById('toggle-music');

// YouTube Player APIの準備
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        videoId: 'ulfeM8JGq7s', // Addict MVのID
        playerVars: {
            'autoplay': 0,
            'controls': 0,
            'showinfo': 0,
            'rel': 0,
            'loop': 1,
            'playlist': 'ulfeM8JGq7s',
            'mute': 1
        },
        events: {
            'onReady': onPlayerReady
        }
    });
}

function onPlayerReady(event) {
    toggleMusic.addEventListener('click', () => {
        const state = player.getPlayerState();
        if (state === YT.PlayerState.PLAYING) {
            player.pauseVideo();
        } else {
            player.playVideo();
        }
    });
}

async function getNewQuote() {
    const response = await fetch('/get-quote');
    const data = await response.json();
    currentQuote = data.text;
    characterName.textContent = data.character;
    quoteDisplay.textContent = currentQuote;
    quoteInput.value = '';
}

function startGame() {
    score = 0;
    timer = 0;
    scoreDisplay.textContent = score;
    getNewQuote();
    quoteInput.disabled = false;
    
    player.playVideo();
    
    clearInterval(gameInterval);
    gameInterval = setInterval(() => {
        timer++;
        timerDisplay.textContent = timer;
    }, 1000);
}

quoteInput.addEventListener('input', () => {
    if (quoteInput.value === currentQuote) {
        score += 100;
        scoreDisplay.textContent = score;
        getNewQuote();
    }
});

startButton.addEventListener('click', startGame);