import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

const ChatArea = ({
  messages,
  setMessages,
  setSources,
  loading,
  setLoading
}) => {

  return (

    <div className="chat-area">

      <div className="chat-messages">

        {messages.length === 0 ? (

          <div className="empty-chat">

            <h2>👋 Welcome to ScholarSync AI</h2>

            <p>
              Ask anything about the uploaded documents.
            </p>

          </div>

        ) : (

          messages.map((message, index) => (

            <MessageBubble
              key={index}
              message={message}
            />

          ))

        )}

      </div>

      <ChatInput
        setMessages={setMessages}
        setSources={setSources}
        loading={loading}
        setLoading={setLoading}
      />

    </div>

  );

};

export default ChatArea;