import { FaBookOpen, FaRobot, FaSearch } from "react-icons/fa";

export default function Hero() {
  return (
    <section className="hero">

      <div className="hero-left">

        <span className="badge">
          AI Powered Research Assistant
        </span>

        <h1>
          Chat with your
          <br />
          Academic Books
        </h1>

        <p>
          Upload research papers, books and PDFs.
          Ask questions in natural language and receive
          accurate AI-generated answers with citations.
        </p>

        <div className="hero-buttons">
          <button className="primary-btn">
            Upload PDF
          </button>

          <button className="secondary-btn">
            View Demo
          </button>
        </div>

      </div>

      <div className="hero-right">

        <div className="glass-card">

          <div className="feature">

            <FaBookOpen />

            <div>

              <h3>Smart PDF Search</h3>

              <p>Semantic document retrieval</p>

            </div>

          </div>

          <div className="feature">

            <FaRobot />

            <div>

              <h3>AI Answers</h3>

              <p>Gemini powered generation</p>

            </div>

          </div>

          <div className="feature">

            <FaSearch />

            <div>

              <h3>Page Citations</h3>

              <p>Every answer includes sources</p>

            </div>

          </div>

        </div>

      </div>

    </section>
  );
}