// Send message to server and receive response
function sendPrompt() {
    const inputField = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const userText = inputField.value.trim();
    inputField.value = '';

    // Add message to the chat box
    if (userText) {
        const userDiv = document.createElement('div');
        userDiv.textContent = userText;
        userDiv.className = 'chat-message user-message';
        chatBox.appendChild(userDiv);
        scrollToBottom(chatBox);

        // Send message to server and handle response
        fetch('/send_prompt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: userText })
        })
        .then(response => response.json())
        .then(data => {
            const replyDiv = document.createElement('div');
            replyDiv.textContent = data.message;
            replyDiv.className = 'chat-message admin-message';
            chatBox.appendChild(replyDiv);
            scrollToBottom(chatBox);
        })
        .catch(error => console.error('Error:', error));
    }
}

// Keep the chat scrolled to the bottom
function scrollToBottom(element) {
    element.scrollTop = element.scrollHeight;
}

// Send pressing enter
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendPrompt();
    }
});

