function buildStrip(id) {
    const strip = document.getElementById(id);
    const count = Math.ceil(window.innerWidth / 34) + 2;
    for (let i = 0; i < count; i++) {
        const hole = document.createElement('div');
        hole.className = 'film-hole';
        strip.appendChild(hole);
    }
}
buildStrip('strip-top');
buildStrip('strip-bottom');

document.querySelectorAll('.suggestion-chip').forEach(chip => {
    chip.addEventListener('click', function () {
        const text = Array.from(chip.childNodes)
            .filter(n => n.nodeType === Node.TEXT_NODE)
            .map(n => n.textContent.trim())
            .filter(Boolean)
            .join('');
        document.getElementById('user-input').value = text;
        document.getElementById('user-input').focus();
    });
});

document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    addMessage('user', message);
    input.value = '';

    const typingRow = showTyping();

    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        typingRow.remove();
        addMessage('bot', data.response);
    } catch {
        typingRow.remove();
        addMessage('bot', '⚠️ Não consegui conectar ao servidor. Tente novamente em instantes.');
    }
}

function addMessage(sender, text) {
    const chatBox = document.getElementById('chat-box');

    const row = document.createElement('div');
    row.className = `message-row ${sender === 'user' ? 'user-row' : ''}`;

    const av = document.createElement('div');
    av.className = `msg-avatar ${sender === 'user' ? 'user-av' : 'bot-av'}`;
    av.textContent = sender === 'user' ? '👤' : '🎬';

    const msg = document.createElement('div');
    msg.className = `message ${sender === 'user' ? 'user-msg' : 'bot-msg'}`;
    msg.textContent = text;

    row.appendChild(av);
    row.appendChild(msg);
    chatBox.appendChild(row);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping() {
    const chatBox = document.getElementById('chat-box');

    const row = document.createElement('div');
    row.className = 'message-row';

    const av = document.createElement('div');
    av.className = 'msg-avatar bot-av';
    av.textContent = '🎬';

    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.className = 'typing-dot';
        indicator.appendChild(dot);
    }

    row.appendChild(av);
    row.appendChild(indicator);
    chatBox.appendChild(row);
    chatBox.scrollTop = chatBox.scrollHeight;
    return row;
}