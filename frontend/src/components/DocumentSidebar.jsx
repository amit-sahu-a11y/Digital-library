import { FiFolder, FiPlus } from "react-icons/fi";

const DocumentSidebar = () => {
  return (
    <aside className="document-sidebar">

      <div className="sidebar-header">

        <h2>Documents</h2>

        <button>
          <FiPlus />
        </button>

      </div>

      <div className="document-list">

        <div className="document-card active">
          📘 Machine Learning.pdf
        </div>

        <div className="document-card">
          +
          Upload New PDF
        </div>

      </div>

    </aside>
  );
};

export default DocumentSidebar;