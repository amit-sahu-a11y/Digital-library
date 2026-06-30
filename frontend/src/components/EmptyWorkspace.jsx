import UploadZone from "./UploadZone";
import { motion } from "framer-motion";

// const EmptyWorkspace = () => {
const EmptyWorkspace = ({ setDocuments }) => {
  return (
    <div className="empty-workspace">

      <motion.div
        className="hero-card"
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >

        <h1>📚 ScholarSync AI</h1>

        <p>
          Transform your books into an AI-powered knowledge assistant.
          Upload PDFs, ask questions in natural language, and receive
          accurate answers with page references in seconds.
        </p>

        <UploadZone
    setDocuments={setDocuments}
/>

      </motion.div>

    </div>
  );
};

export default EmptyWorkspace;