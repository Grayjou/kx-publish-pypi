import subprocess
import sys
import os
TEST = True  # Set to False for production publish
# Path to your PowerShell script
ps1_path = "publish.ps1" if not TEST else "publish_test.ps1" 
script_path = os.path.join(os.path.dirname(__file__), 'publish.ps1')

print("\n🚀 Ready to build and publish twitch_checker.")
print("⚠ WARNING: This will increment the version if you've updated it in pyproject.toml.\n")

confirm = input("Do you want to proceed? (yes/no): ").strip().lower()

if confirm not in ["yes", "y"]:
    print("❌ Publishing aborted.")
    sys.exit(0)

# Build the PowerShell command
command = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]

try:
    subprocess.run(command, check=True)
    print("\n✅ Publish process completed successfully.")
except subprocess.CalledProcessError as e:
    print("\n❌ An error occurred during publishing.")
    sys.exit(e.returncode)
