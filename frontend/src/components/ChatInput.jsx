import { useState } from "react";
import { FiSend } from "react-icons/fi";
import { searchDocuments } from "../services/searchService";

const ChatInput = ({
  setMessages,
  setSources,
  loading,
  setLoading,
}) => {

  const [question, setQuestion] = useState("");

  const handleSend = async () => {

    if (!question.trim()) return;

    const currentQuestion = question;

    // Show user's message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        text: currentQuestion,
      },
    ]);

    setQuestion("");

    try {

      setLoading(true);

      const response = await searchDocuments(currentQuestion);

      // Show AI response
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: response.answer,
        },
      ]);

      // Update Sources Panel
      setSources(response.sources || []);

    } catch (error) {

      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "❌ Sorry, something went wrong while searching.",
        },
      ]);

    } finally {

      setLoading(false);

    }

  };

  return (

    <div className="chat-input">

      <input
        type="text"
        placeholder="Ask anything about your documents..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button
        onClick={handleSend}
        disabled={loading}
      >
        {loading ? "Thinking..." : <FiSend />}
      </button>

    </div>

  );

};

export default ChatInput;