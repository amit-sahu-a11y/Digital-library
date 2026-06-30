import { useState } from "react";

import TopBar from "../components/TopBar";
import DocumentSidebar from "../components/DocumentSidebar";
import EmptyWorkspace from "../components/EmptyWorkspace";
import ChatArea from "../components/ChatArea";
import SourcePanel from "../components/SourcePanel";

const Workspace = () => {

    const [documents, setDocuments] = useState([]);

    return (

        <div className="workspace-page">

            <TopBar />

            <div className="workspace-body">

                <DocumentSidebar
                    documents={documents}
                />

                <div className="workspace-center">

                    {documents.length === 0 ? (

                        <EmptyWorkspace
                            setDocuments={setDocuments}
                        />

                    ) : (

                        <ChatArea />

                    )}

                </div>

                <SourcePanel />

            </div>

        </div>

    );

};

export default Workspace;