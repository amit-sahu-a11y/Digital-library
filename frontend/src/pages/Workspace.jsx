import TopBar from "../components/TopBar";
import DocumentSidebar from "../components/DocumentSidebar";
import ChatArea from "../components/ChatArea";
import EmptyWorkspace from "../components/EmptyWorkspace";

const Workspace = () => {
  return (
    <div className="workspace-page">

      <TopBar />

      <div className="workspace-body">

        <DocumentSidebar />

        <div className="workspace-center">
          <EmptyWorkspace />
          {/* Later this becomes ChatArea */}
        </div>

        <ChatArea />

      </div>

    </div>
  );
};

export default Workspace;