import axios from "axios";

const API = "http://127.0.0.1:8000";

export const searchDocuments = async (query) => {
  const response = await axios.get(`${API}/search`, {
    params: {
      query,
      top_k: 5,
    },
  });

  return response.data;
};