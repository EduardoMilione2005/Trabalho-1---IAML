function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    const userMsg = document.createElement("p");
    userMsg.textContent = "Você: " + message;

    chatBox.appendChild(userMsg);

    input.value = "";
}