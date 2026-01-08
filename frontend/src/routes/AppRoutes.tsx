import { Routes, Route } from "react-router-dom";
import { ProtectedRoutes } from "./ProtectedRoutes";
import { Login } from "./Login";
import { Home } from "./protected-routes/Home";
import { Page } from "./protected-routes/Page";

export const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/protected" element={<ProtectedRoutes />}>
        <Route path="/protected/home" element={<Home />} />
        <Route path="/protected/page" element={<Page />} />
      </Route>
    </Routes>
  );
};
