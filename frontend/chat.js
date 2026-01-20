const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});

function sendMessage() {
  const message = userInput.value.trim();
  if (message === "") return;

  // Show user message
  addMessage(message, "user");

  userInput.value = "";

  // Show typing
  addMessage("Typing...", "bot", true);

  fetch("https://mindstack-student-backend.onrender.com/chat", { ... }), {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message : message })
})

    .then(response => response.json())
    .then(data => {
      removeTyping();
      addMessage(data.response, "bot");
    })
    .catch(error => {
      removeTyping();
      addMessage("Something went wrong 😔", "bot");
      console.error(error);
    });
}

function addMessage(text, sender, isTyping = false) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender);

  if (isTyping) {
    msgDiv.id = "typing";
  }

  msgDiv.innerText = text;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById("typing");
  if (typing) {
    typing.remove();
  }
}
