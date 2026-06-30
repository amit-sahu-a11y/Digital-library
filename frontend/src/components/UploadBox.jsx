import { FaCloudUploadAlt } from "react-icons/fa";

export default function UploadBox() {
  return (
    <section className="upload-section">

      <h2>Upload Your Documents</h2>

      <p>
        Upload books, PDFs and research papers.
      </p>

      <div className="upload-card">

        <FaCloudUploadAlt className="upload-icon"/>

        <h3>Drag & Drop PDF Here</h3>

        <p>or click to browse files</p>

        <button className="upload-btn">
          Select PDF
        </button>

      </div>

    </section>
  );
}