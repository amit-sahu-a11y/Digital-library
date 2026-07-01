import axios from "axios";

const API = "http://127.0.0.1:8000";

export const askQuestion = async (
    question,
    top_k = 5,
    documentId = null
) => {

    const response = await axios.get(
        `${API}/search`,
        {
            params: {
                query: question,
                top_k: top_k,
                document_id: documentId
            }
        }
    );

    return response.data;
};