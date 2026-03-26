async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    if (!message) return;

    addMessage("Você", message);
    input.value = "";

    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    addMessage("Bot", data.response);
}

function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");

    const msg = document.createElement("p");
    msg.textContent = `${sender}: ${text}`;

    chatBox.appendChild(msg);
}