const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

async function sendMessage() {
  const text = userInput.value.trim();
  if (text === "") return;
//hi
  addMessage(text, "user");
  userInput.value = "";

  // Thinking indicator
  addMessage("Thinking...", "bot");

  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: text
      })
    });

    const data = await response.json();

    // Remove "Thinking..."
    chatBox.lastChild.remove();

    addMessage(data.response, "bot");

  } catch (error) {
    chatBox.lastChild.remove();
    addMessage("Backend not running ⚠️", "bot");
  }
}

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Enter key supportl
userInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
