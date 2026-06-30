import TopBar from "../components/TopBar";
import DocumentSidebar from "../components/DocumentSidebar";
import ChatArea from "../components/ChatArea";
import SourcePanel from "../components/SourcePanel";

const Workspace = () => {
  return (
    <div className="workspace">

      <TopBar />

      <div className="workspace-body">

        <DocumentSidebar />

        <ChatArea />

        <SourcePanel />

      </div>

    </div>
  );
};

export default Workspace;