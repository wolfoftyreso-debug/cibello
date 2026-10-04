import { createFileRoute, Navigate } from "@tanstack/react-router";

export const Route = createFileRoute("/kitchen")({
  component: () => <Navigate to="/" />,
});
