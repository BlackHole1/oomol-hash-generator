import { writeFile } from "fs/promises";
import { join } from "path";

export default async function(params, context) {
  const p = join(context.sessionDir, "output.txt");

  writeFile(p, "oomol", {
    encoding: "utf-8",
  });
  return { output: p };
}