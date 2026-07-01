import { useRef, useState } from "react";
import { FiUploadCloud } from "react-icons/fi";
import { motion } from "framer-motion";
import { uploadPDF } from "../services/uploadService";

const UploadZone = ({ setDocuments }) => {

    const fileInputRef = useRef(null);

    const [loading, setLoading] = useState(false);

    const handleClick = () => {
        fileInputRef.current.click();
    };

    const handleFile = async (e) => {

        const file = e.target.files[0];

        if (!file) return;

        try {

            setLoading(true);

            const response = await uploadPDF(file);
            console.log(response);

            // Add uploaded document to sidebar
            setDocuments((prev) => {
            const updated = [...prev, response];
            console.log("Documents:", updated);
            return updated;
            });

            // console.log(response);

            alert("✅ PDF uploaded successfully!");

        } catch (err) {

            console.error(err);

            alert("❌ Upload failed!");

        } finally {

            setLoading(false);

        }

    };

    return (

        <motion.div
            className="upload-box"
            whileHover={{ scale: 1.02 }}
        >

            <FiUploadCloud className="upload-icon" />

            <h2 className="upload-title">
                Drag & Drop your PDF
            </h2>

            <p className="upload-subtitle">
                Click below to browse your computer
            </p>

            <button
                className="upload-button"
                onClick={handleClick}
                disabled={loading}
            >
                {loading ? "Uploading..." : "Upload Document"}
            </button>

            <input
                type="file"
                accept=".pdf"
                hidden
                ref={fileInputRef}
                onChange={handleFile}
            />

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