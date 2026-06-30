import Navbar from "../components/Navbar";

export default function Home() {
  return (
    <>
      <Navbar />

      <section
        style={{
          height: "85vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          textAlign: "center"
        }}
      >
        <h1
          style={{
            fontSize: "65px",
            fontWeight: "700",
            marginBottom: "20px"
          }}
        >
          ScholarSync AI
        </h1>

        <p
          style={{
            fontSize: "22px",
            color: "#cbd5e1",
            width: "700px",
            lineHeight: "40px"
          }}
        >
          Upload your academic books, research papers and PDFs.
          Ask questions in natural language and receive AI-powered
          answers with page references.
        </p>
      </section>
    </>
  );
}