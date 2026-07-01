import { useState } from "react";

import TopBar from "../components/TopBar";
import DocumentSidebar from "../components/DocumentSidebar";
import EmptyWorkspace from "../components/EmptyWorkspace";
import ChatArea from "../components/ChatArea";
import SourcePanel from "../components/SourcePanel";

const Workspace = () => {

    const [documents, setDocuments] = useState([]);
    const [messages, setMessages] = useState([]);
    const [sources, setSources] = useState([]);
    const [loading, setLoading] = useState(false);

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

                        <ChatArea
                            messages={messages}
                            setMessages={setMessages}
                            setSources={setSources}
                            loading={loading}
                            setLoading={setLoading}
                        />

                    )}

                </div>

                <SourcePanel
                    sources={sources}
                />

            </div>

        </div>

    );

};

export default Workspace;