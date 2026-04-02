const input = document.getElementById("user-input");

input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {
    const message = input.value;

    if (!message) return;

    addMessage("user", message);
    input.value = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        addMessage("bot", data.response);

    } catch (error) {
        addMessage("bot", "Erro: Não foi possível conectar ao servidor.");
    }
}

function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");

    const msg = document.createElement("div");
    msg.classList.add("message");
    msg.classList.add(sender);
    msg.textContent = text;

    chatBox.appendChild(msg);

    chatBox.scrollTop = chatBox.scrollHeight;
}