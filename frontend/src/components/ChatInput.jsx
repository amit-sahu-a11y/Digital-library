import { FiSend } from "react-icons/fi";

const ChatInput = ({ value, setValue, onSend }) => {
  return (
    <div className="chat-input">

      <input
        type="text"
        placeholder="Ask anything about your uploaded PDF..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            onSend();
          }
        }}
      />

      <button onClick={onSend}>
        <FiSend />
      </button>

    </div>
  );
};

export default ChatInput;