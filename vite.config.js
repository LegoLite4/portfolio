import { rmSync } from "node:fs";
import { join } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  server: {
    host: "127.0.0.1",
    port: 5173,
  },
  plugins: [
    {
      name: "omit-certificates",
      closeBundle() {
        rmSync(join("dist", "certificates"), { recursive: true, force: true });
      },
    },
  ],
});
