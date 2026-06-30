import { FiUploadCloud } from "react-icons/fi";
import { motion } from "framer-motion";

const UploadZone = () => {
  return (
    <motion.div
      className="upload-box"
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
    >

      <FiUploadCloud className="upload-icon" />

      <h2 className="upload-title">
        Drag & Drop your PDF
      </h2>

      <p className="upload-subtitle">
        or click below to browse your computer
      </p>

      <button className="upload-button">
        Upload Document
      </button>

      <br />

      <small
        style={{
          display: "block",
          marginTop: "18px",
          color: "#94a3b8"
        }}
      >
        Supports PDF • Max 100 MB
      </small>

    </motion.div>
  );
};

export default UploadZone;