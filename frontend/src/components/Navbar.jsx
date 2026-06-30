import { FaRobot } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <FaRobot />
        <span>ScholarSync AI</span>
      </div>

      <div className="menu">
        <a href="#">Home</a>
        <a href="#">Documents</a>
        <a href="#">Chat</a>
      </div>
    </nav>
  );
}