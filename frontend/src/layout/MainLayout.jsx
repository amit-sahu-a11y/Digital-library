import { Outlet } from "react-router-dom";

const MainLayout = () => {
  return (
    <div className="app-layout">
      <Outlet />
    </div>
  );
};

export default MainLayout;