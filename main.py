import subprocess
import os

def run_script(script_name):
    print(f"\n🔄 Running {script_name}...\n")
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {script_name} completed successfully!")
    else:
        print(f"❌ Error in {script_name}:\n{result.stderr}")
        exit(1)

def main():
    run_script("preprocess_alchemy_csv.py")
    run_script("music_matching.py")
    run_script("generate_embeddings.py")
    run_script("value_matching.py")
    run_script("build_graph.py")
    run_script("attendees.py")

    if os.path.exists("graphData.json"):
        print("\nMatching complete!")
    else:
        print("\n❌ `graphData.json` not found! Something went wrong.")

if __name__ == "__main__":
    main()