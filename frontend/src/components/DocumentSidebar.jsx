import { FiPlus } from "react-icons/fi";

const DocumentSidebar = ({ documents }) => {

    return (

        <aside className="document-sidebar">

            <div className="sidebar-header">

                <h2>Documents</h2>

                <button>

                    <FiPlus />

                </button>

            </div>

            <div className="document-list">

                {

                    documents.map((doc, index) => (

                        <div
                            key={index}
                            className="document-card active"
                        >

                            📘 {doc.filename}

                        </div>

                    ))

                }

            </div>

        </aside>

    );

};

export default DocumentSidebar;