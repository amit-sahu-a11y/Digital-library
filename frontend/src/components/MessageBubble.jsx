const MessageBubble = ({ message }) => {

  const isUser = message.role === "user";

  return (

    <div
      className={`message-row ${isUser ? "user" : "assistant"}`}
    >

      <div
        className={`message-bubble ${isUser ? "user-bubble" : "assistant-bubble"}`}
      >

        {message.text}

      </div>

    </div>

  );

};

export default MessageBubble;