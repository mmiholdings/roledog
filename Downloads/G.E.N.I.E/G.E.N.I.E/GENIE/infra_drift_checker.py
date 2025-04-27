
import subprocess

def check_drift():
    result = subprocess.run(["terraform", "plan", "-detailed-exitcode"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ No drift detected.")
    elif result.returncode == 2:
        print("⚠️ Drift detected! Changes needed:")
        print(result.stdout)
    else:
        print("❌ Terraform error:")
        print(result.stderr)

if __name__ == "__main__":
    check_drift()
