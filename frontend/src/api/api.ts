import axios from "axios";

const API_URL = "http://localhost:8000";

export async function createUser(data) {
  const res = await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.detail || "Failed to create user");
  }

  return res.json();
}

export const login = async (data: any) => {
  // FastAPI OAuth2 standard expects form-data, not raw JSON
  const params = new URLSearchParams();
  params.append("username", data.email);
  params.append("password", data.password);

  // Axios throws an error automatically if status is 4xx or 5xx
  const response = await axios.post(`${API_URL}/auth/login`, params, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response.data; // This will contain access_token and token_type
};

// export async function login(data) {
//   const res = await fetch(`${API_URL}/auth/login`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(data),
//   });
//   return res.json();
// }

export function authHeaders() {
  const token = localStorage.getItem("token");
  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

export async function getBalances() {
  const res = await fetch(`${API_URL}/balances`, {
    headers: authHeaders(),
  });
  return res.json();
}
