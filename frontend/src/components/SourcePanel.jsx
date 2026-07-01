const SourcePanel = ({ sources }) => {

  return (

    <aside className="sources-panel">

      <h2>📚 Sources</h2>

      {sources.length === 0 ? (

        <p>No sources yet.</p>

      ) : (

        sources.map((source, index) => (

          <div
            key={index}
            className="source-card"
          >

            <h4>{source.book_name}</h4>

            <p>📄 Page {source.page_number}</p>

            <p>⭐ Similarity {source.score}%</p>

          </div>

        ))

      )}

    </aside>

  );

};

export default SourcePanel;