import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Workspace from "./pages/Workspace";
import MainLayout from "./layout/MainLayout";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />} />

        <Route element={<MainLayout />}>
          <Route path="/workspace" element={<Workspace />} />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;