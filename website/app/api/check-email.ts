import { NextApiRequest, NextApiResponse } from "next";
import fs from "fs";
import path from "path";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "POST") {
    const { email } = req.body;
    const filePath = path.join(process.cwd(), "data.csv");
    const fileContent = fs.readFileSync(filePath, "utf-8");
    const lines = fileContent.split("\n");
    
    // Check if email exists in the CSV
    const emailExists = lines.some(line => line.includes(email));
    
    if (emailExists) {
      res.status(200).json({ success: true });
    } else {
      res.status(404).json({ success: false });
    }
  } else {
    res.setHeader("Allow", ["POST"]);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
} 