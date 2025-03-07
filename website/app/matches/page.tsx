import { useRouter } from "next/navigation";
import { motion } from "framer-motion"; // Import motion from Framer Motion

const Matches = () => {
  const router = useRouter();
  const { email } = router.query;

  // Logic to fetch matches based on email
  // This is a placeholder for the actual implementation
  const matches = [
    { name: "Match 1", description: "Description for Match 1", house: "House A" },
    { name: "Match 2", description: "Description for Match 2", house: "House B" },
    { name: "Match 3", description: "Description for Match 3", house: "House C" },
  ];

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Your Matches for {email}</h1>
      <motion.ul
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="space-y-4"
      >
        {matches.map((match, index) => (
          <motion.li
            key={index}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.3, delay: index * 0.1 }}
            className="border p-4 rounded shadow-md"
          >
            <h2 className="text-xl font-semibold">{match.name}</h2>
            <p>{match.description}</p>
            <p className="font-medium">House: {match.house}</p>
          </motion.li>
        ))}
      </motion.ul>
    </div>
  );
};

export default Matches; 