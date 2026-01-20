const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", e=>{
  if(e.key==="Enter") sendMessage();
});

function sendMessage(){
  const message = userInput.value.trim();
  if(!message) return;

  addMessage(message,"user");
  userInput.value="";

  addMessage("Typing...","bot",true);

  fetch("/chat",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({message})
  })
  .then(r=>r.json())
  .then(d=>{
    removeTyping();
    addMessage(d.response,"bot");
  })
  .catch(e=>{
    removeTyping();
    addMessage("Something went wrong 😔","bot");
    console.error(e);
  });
}

function addMessage(text,sender,isTyping=false){
  const div=document.createElement("div");
  div.classList.add("message",sender);
  if(isTyping) div.id="typing";
  div.innerText=text;
  chatBox.appendChild(div);
  chatBox.scrollTop=chatBox.scrollHeight;
}

function removeTyping(){
  const typing=document.getElementById("typing");
  if(typing) typing.remove();
}
